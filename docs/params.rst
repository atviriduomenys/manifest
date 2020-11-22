.. default-role:: literal

.. _parametrizacija:

Parametrizacija
###############

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
           {
                "code": "lt",
                "country": "Lietuva"
            }
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


+---+---+---+-------------+----------------------------------------------------+---------------------+---------+---------+
| d | r | m | property    | source                                             | prepare             | type    | ref     |
+===+===+===+=============+====================================================+=====================+=========+=========+
| datasets/example/params |                                                    |                     |         |         |
+---+---+---+-------------+----------------------------------------------------+---------------------+---------+---------+
|   | countries           | \https://example.com/salys/                        |                     | json    |         |
+---+---+---+-------------+----------------------------------------------------+---------------------+---------+---------+
|   |   | country         | resources                                          |                     |         | code    |
+---+---+---+-------------+----------------------------------------------------+---------------------+---------+---------+
|   |   |   | code        | code                                               |                     | string  |         |
+---+---+---+-------------+----------------------------------------------------+---------------------+---------+---------+
|   |   |   | name        | country                                            |                     | string  |         |
+---+---+---+-------------+----------------------------------------------------+---------------------+---------+---------+
|   | cities              | \https://example.com/salys/{country.code}/miestai/ |                     | json    |         |
+---+---+---+-------------+----------------------------------------------------+---------------------+---------+---------+
|   |   |   |             | country                                            |                     | param   | country |
+---+---+---+-------------+----------------------------------------------------+---------------------+---------+---------+
|   |   | city            | resources                                          |                     |         | code    |
+---+---+---+-------------+----------------------------------------------------+---------------------+---------+---------+
|   |   |   | country     |                                                    | param(country).code | ref     | country |
+---+---+---+-------------+----------------------------------------------------+---------------------+---------+---------+
|   |   |   | name        | city                                               |                     | string  |         |
+---+---+---+-------------+----------------------------------------------------+---------------------+---------+---------+

Šioje :term:`DSA` lentelėje panaudotas :data:`param`, kuriam suteiktas
pavadinimas `country`, įrašytas į :data:`param.ref` stulpelį.
:data:`param.source` stulpelyje nurodyta, kad parametro reikšmės imamos iš
`/datasets/example/params/country` modelio duomenų.

Skaitant duomenis, pirmiausiai bus surinkti šalių duomenys, o po to, miestų.
Renkant miestų duomenys, pirmiausiai bus panaudoti visi iki šiol surinkti
šalių duomenys, nes tai yra apibrėžta `countries` parametre. Tada su
kiekvienu šalies įrašu, bus skaitomi miestai, pakeičiant `{country.code}` į
kiekvienos šalies kodą. Tokiu būdu, parametrų dėka, galima aprašyti dinaminių
API duomenis.

Papildomai, parametrus galima naudoti ir kitose vietose, kaip tai y ra padaryta
`city` modelio, `country` savybės :data:`property.prepare` stulpelyje, kuriame
nurodyta, kad šio miesto šalies kodas yra `param(country).code`.

Galutiniame rezultate gauname tokias dvi lenteles:

====  ========  ===============
datasets/example/params/country
-------------------------------
_id   code      name
====  ========  ===============
1     lt        Lietuva
====  ========  ===============

====  ========  ============
datasets/example/params/city
----------------------------
_id   country   name
====  ========  ============
1     1         Vilnius
2     1         Kaunas
====  ========  ============

Atkreipkite dėmesį, kad visuose pavyzdžiuose, nepriklausomai nuo duomenų
šaltinio, naudodami vieningą žodyną visą laiką gauname tuose pačius duomenis,
tokios pačios struktūros ir tokiais pačiais objektų ir laukų pavadinimais.
