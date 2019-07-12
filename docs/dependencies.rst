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

   name: pavyzdziai/priklausomybes
   type: dataset
   resources:
     salys:
       type: json
       source: https://example.com/salys/
       objects:
         geografija/salis:
           source: resources
           properties:
             id:
               type: pk
               source: code
             kodas:
               type: string
               source: code
             pavadinimas:
               type: string
               source: country
     miestai:
       type: json
       source: https://example.com/salys/{salis.kodas}/miestai/
       objects:
         geografija/miestas:
           source: resources
           dependencies:
             salis: geografija/salis/:dataset/pavyzdziai/priklausomybes
           properties:
             id:
               type: pk
               source: city
             salis:
               type: ref
               object: geografija/salis
               dependency: salis.id
             pavadinimas:
               type: string
               source: city

Šioje vietoje, panaudojant priklausomybę:

.. code-block:: yaml

   dependencies:
      salis: geografija/salis/:dataset/pavyzdziai/priklausomybes

Prieš kreipiantis į miestų :term:`prieigos tašką <prieigos taškas>` vykdoma
užklausa::

   /geografija/salis/:dataset/pavyzdziai/priklausomybes

Tada kviečiamas miestų :term:`prieigos taškas` tiek kartų, kiek yra kiek
užklausa grąžino eilučių. Miestų :term:`prieigos taško <prieigos taškas>` URL
adrese esantis `{salis.kodas}` pakeičiamas į užklausos eilutėje esančią
reikšme. Tokiu būdu, gauname visus miestus.

Papildomai, `geografija/miestas` savybė `salis`, reikšmę gauna ne iš `source`,
o iš `dependency: salis.id`, tokiu būdu susiejant miestą su šalimi.

Galutiniame rezultate gauname tokias dvi lenteles:

**geografija/salis**

==========  ===========
id          pavadinimas
==========  ===========
`552c4c24`  Lietuva
==========  ===========

**geografija/miestas**

==========  ==========  ===========
id          salis       pavadinimas
==========  ==========  ===========
`8e65fec0`  `552c4c24`  Vilnius
`4fe80490`  `552c4c24`  Kaunas
==========  ==========  ===========

Atkreipkite dėmesį, kad visuose pavyzdžiuose, nepriklausomai nuo duomenų
šaltinio, naudodami vieningą žodyną visą laiką gauname tuose pačius duomenis,
tokios pačios struktūros ir tokiais pačiais objektų ir laukų pavadinimais.
