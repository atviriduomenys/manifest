.. default-role:: literal

.. _deps:

Priklausomybės
##############

Dažnai duomenys teikiami :term:`web servisų <web servisas>` pagalba,
nesuteikiant galimybės gauti visų vienos lentelės duomenų vienu kartu.
Pavyzdžiui, tarkime turime tokį :term:`web servisą <web servisas>`, kuris
teikia duomenis apie miestus ir šalis. Visų šalių sąrašą galima gauti
kviečiant šį :term:`prieigos tašką <prieigos taškas>`::

   htts://example.com/salys/

Šis prieigos taškas grąžina duomenis JSON formatu:

.. code-block:: json

   {
       "resources": [
           {"code": "lt", "country": "Lietuva"}
       ]
   }

Miestų sąrašą galima gauti tik turinti šalies kodą, pavyzdžiui::

   htts://example.com/salys/lt/miestai/

Šis miestų prieigos taškas grąžina:


.. code-block:: json

   {
       "resources": [
           {"city": "Vilnius"},
           {"city": "Kaunas"}
       ]
   }

Tokio duomenų šaltinio duomenų struktūros aprašas atrodo taip:

.. code-block:: yaml

   type: dataset
   name: datasets/pavyzdziai/priklausomybes
   resources:
     salys:
       type: json
       pull: https://example.com/salys/
     miestai:
       type: json
       pull: https://example.com/salys/{salis.kodas}/miestai/

.. code-block:: yaml

   type: model
   name: datasets/pavyzdziai/priklausomybes/salis
   source:
     dataset: datasets/pavyzdziai/priklausomybes
     resource: salys
     name: resources
     pk: kodas
   properties:
     kodas:
       type: string
       source: code
     pavadinimas:
       type: string
       source: country

.. code-block:: yaml

   type: model
   name: datasets/pavyzdziai/priklausomybes/miestas
   source:
     dataset: datasets/pavyzdziai/priklausomybes
     resource: miestai
     name: resources
     pk: pavadinimas
     params:
       - salis: query('datasets/pavyzdziai/priklausomybes/salis')
   properties:
     salis:
       type: ref
       model: datasets/pavyzdziai/priklausomybes/salis
       source:
         name: param(salis)._id
         ref: _id
     pavadinimas:
       type: string
       source: city

Šioje vietoje, panaudojant priklausomybę:

.. code-block:: yaml

   using:
     salis: query('datasets/pavyzdziai/priklausomybes/salis')

Prieš kreipiantis į miestų :term:`prieigos tašką <prieigos taškas>` vykdoma
užklausa::

   query('datasets/pavyzdziai/priklausomybes/salis')

Tada kviečiamas miestų :term:`prieigos taškas` tiek kartų, kiek yra kiek
užklausa grąžino eilučių. Miestų :term:`prieigos taško <prieigos taškas>` URL
adrese esantis `{salis.kodas}` pakeičiamas į užklausos eilutėje esančią
reikšme. Tokiu būdu, gauname visus miestus.

Modelio `datasets/pavyzdziai/priklausomybes/miestas` savybė `salis`, reikšmę
gauna iš kintamojo `param(salis)._id`. Pagal nutylėjimą lauko `source.name`
reikšmė atitinka siejamo modelio `source.pk` reikšmę, pagal kurią gaunamas
tikrasis identifikatorius. Tačiau šiuo atveju identifikatorius jau šinomas,
todėl papildomai nurodome, kad šiuo atveju `source.name` rodo į `_id` lauką.

Galutiniame rezultate gauname tokias dvi lenteles:

**datasets/pavyzdziai/priklausomybes/salis**

====================================  ===========
id                                    pavadinimas
====================================  ===========
cb379696-76f7-43d8-8a72-57ac4e9914d0  Lietuva
====================================  ===========

**datasets/pavyzdziai/priklausomybes/miestas**

====================================  ====================================  ===========
id                                    salis                                 pavadinimas
====================================  ====================================  ===========
164973fa-7a8f-439b-8b26-cfade23c6bc7  cb379696-76f7-43d8-8a72-57ac4e9914d0  Vilnius
00dd95e6-7c40-43d7-8429-50c9ca0b3c76  cb379696-76f7-43d8-8a72-57ac4e9914d0  Kaunas
====================================  ====================================  ===========

Atkreipkite dėmesį, kad visuose pavyzdžiuose, nepriklausomai nuo duomenų
šaltinio, naudodami vieningą žodyną visą laiką gauname tuose pačius duomenis,
tokios pačios struktūros ir tokiais pačiais objektų ir laukų pavadinimais.
