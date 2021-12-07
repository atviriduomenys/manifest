.. default-role:: literal

.. _duomenų-šaltiniai:

Duomenų šaltiniai
#################

SQL
===

Tarkime turime PostgreSQL duomenų bazę, kurioje yra dvi lentelės:

=======  =========  ===========
SALIS
-------------------------------
ID       KODAS      PAVAD
=======  =========  ===========
100      lt         Lietuva
101      lv         Latvija
102      ee         Estija
=======  =========  ===========

=======  =========  ===========
MIESTAS
-------------------------------
ID       SALIS_ID   PAVAD
=======  =========  ===========
204      100        Vilnius
205      100        Kaunas
206      100        Klaipėda
207      101        Ryga
208      102        Talinas
=======  =========  ===========

Tarkime, kad mes norime atverti tik Lietuvos duomenis, ignoruojant kitų šalių
duomenis.

:term:`Duomenų aprašas <DSA>` atrodys taip:

+----+---+---+---+---+-------------+---------+---------+--------------------------------+-------------------+---------+
| id | d | r | b | m | property    | type    | ref     | source                         | prepare           | access  |
+====+===+===+===+===+=============+=========+=========+================================+===================+=========+
|    | datasets/example/sql        |         |         |                                |                   |         |
+----+---+---+---+---+-------------+---------+---------+--------------------------------+-------------------+---------+
|    |   | db                      | sql     |         | \postgresql://user@host/dbname |                   |         |
+----+---+---+---+---+-------------+---------+---------+--------------------------------+-------------------+---------+
|    |   |   |   | country         |         | id      | SALIS                          | code="lt"         |         |
+----+---+---+---+---+-------------+---------+---------+--------------------------------+-------------------+---------+
|    |   |   |   |   | id          | integer |         | ID                             |                   | private |
+----+---+---+---+---+-------------+---------+---------+--------------------------------+-------------------+---------+
|    |   |   |   |   | code        | string  |         | KODAS                          |                   | open    |
+----+---+---+---+---+-------------+---------+---------+--------------------------------+-------------------+---------+
|    |   |   |   |   | name        | string  |         | PAVAD                          |                   | open    |
+----+---+---+---+---+-------------+---------+---------+--------------------------------+-------------------+---------+
|    |   |   |   | city            |         | id      | MIESTAS                        | country.code="lt" |         |
+----+---+---+---+---+-------------+---------+---------+--------------------------------+-------------------+---------+
|    |   |   |   |   | id          | integer |         | ID                             |                   | private |
+----+---+---+---+---+-------------+---------+---------+--------------------------------+-------------------+---------+
|    |   |   |   |   | country     | ref     | country | SALIS_ID                       |                   | open    |
+----+---+---+---+---+-------------+---------+---------+--------------------------------+-------------------+---------+
|    |   |   |   |   | name        | string  |         | PAVAD                          |                   | open    |
+----+---+---+---+---+-------------+---------+---------+--------------------------------+-------------------+---------+

Reliacinės duomenų bazės (RDBVS) yra populiariausias duomenų saugojimo būdas.
Tačiau taip pat RDBVS struktūra yra lengviausiai aprašoma, didelė dalis
metaduomenų saugoma pačioje RDBVS, todėl nesunkiai galima generuoti gan išsamias
:term:`DSA` lenteles automatiškai.

Atkreipkite dėmesį, kad `id` :term:`savybės <savybė>` pažymėtos `private`
prieigos žyme. Taip rekomenduojama daryti tam, kad nebūtų atskleisti vidiniai
duomenų bazės identifikatoriai. Dažniausiai tokie identifikatoriai yra naudingi
tik duomenų bazės viduje ir išorėje neturi naudos. Be to, tam tikromis
situacijomis, pasinaudojant vidiniais identifikatoriais galima atskleisti
konfidencialius duomenis.

Kadangi išsikėlėme reikalavimą atverti tik Lietuvos duomenis,
:data:`model.prepare` stulpelyje nurodėme atveriamų duomenų filtrus. Dažniausiai
tokie filtrai naudojami asmens duomenų filtravimui arba skaidant lenteles į
kelis atskirus :term:`medelius <modelis>`.

Atlikus visas :term:`DSA` lentelėje aprašytas transformacijas gausime tokias
duomenų lenteles:

====  ===========  =================
datasets/example/sql/country
------------------------------------
_id   code         name
====  ===========  =================
1     lt           Lietuva
2     lv           Latvija
3     ee           Estija
====  ===========  =================

====  ===========  =================
datasets/example/sql/city
------------------------------------
_id   country      name
====  ===========  =================
3     1            Vilnius
4     1            Kaunas
5     1            Klaipėda
====  ===========  =================

Taip pat skaitykite: :ref:`duomenų-atranka`, :ref:`resource-type-sql`.


CSV
===

Tarkime turime tokius duomenis CSV formatu. Kad nebūtu viskas taip paprasta, CSV
failai pateikti ZIP archyve, adresu \https://example.com/data.zip. Ir kad dar
butų sunkiau, CSV faile reikšmės atskirtos ne įprastiniu `,` simboliu, o `;`
simboliu. Archyvo viduje yra tokios lentelės:

=======  =========  ==============
salys.csv
==================================
ID       KODAS      PAVADINIMAS
100      lt         Lietuva
101      lv         Latvija
102      ee         Estija
=======  =========  ==============

=======  =========  ==============
miestai.csv
==================================
ID       ŠALIS      PAVADINIMAS
204      100        Vilnius
205      100        Kaunas
206      100        Klaipėda
207      101        Ryga
208      102        Talinas
=======  =========  ==============


:term:`Duomenų aprašas <DSA>` atrodys taip:

+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+
| id | d | r | b | m | property | type    | ref       | source                        | prepare           | access  |
+====+===+===+===+===+==========+=========+===========+===============================+===================+=========+
|  1 | datasets/example/csv     |         |           |                               |                   |         |
+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+
|  2 |   | salys_zip            | zip     |           | \https://example.com/data.zip |                   |         |
+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+
|  3 |   | salys                | csv     | salys_zip | {}.csv                        | tabular(sep: ";") |         |
+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+
|  4 |   |   |   | Country      |         | id        | salys                         | code="lt"         |         |
+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+
|  5 |   |   |   |   | id       | integer |           | ID                            |                   | private |
+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+
|  6 |   |   |   |   | code     | string  |           | KODAS                         |                   | open    |
+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+
|  7 |   |   |   |   | name     | string  |           | PAVADINIMAS                   |                   | open    |
+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+
|  8 |   |   |   | City         |         | id        | miestai                       | country.code="lt" |         |
+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+
|  9 |   |   |   |   | id       | integer |           | ID                            |                   | private |
+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+
| 10 |   |   |   |   | country  | ref     | Country   | ŠALIS                         |                   | open    |
+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+
| 11 |   |   |   |   | name     | string  |           | PAVADINIMAS                   |                   | open    |
+----+---+---+---+---+----------+---------+-----------+-------------------------------+-------------------+---------+

Kadangi CSV failai yra sudėti į ZIP archyvą, reikia nurodyti, kad prieš skaitant
duomenis, CSV failai turi būti išskleisti iš archyvo, tam naudojam
:func:`func.extract` funkciją. Prieš skaitant duomenis, :func:`tabular.sep`
nurodo, kad CSV faile naudojamas nestandartinis reikšmių skirtukas,
kabliataškis.

Visa kita aprašoma lygiai taip pat, kaip ir SQL atveju.


JSON
====

Tarkime JSON atveju turime API kuris atrodo taip:


::

    https://example.com/salys/

.. code-block:: json

      {
         "šalys": [
            {"id": 100, "kodas": "lt", "šalis": "Lietuva"},
            {"id": 101, "kodas": "lv", "šalis": "Latvija"},
            {"id": 102, "kodas": "ee", "šalis": "Estija"}
         ]
      }

::

    https://example.com/miestai/lt

.. code-block:: json

      {
         "miestai": [
            {"id": 204, "miestas": "Vilnius"},
            {"id": 205, "miestas": "Kaunas"},
            {"id": 206, "miestas": "Klaipėda"}
         ]
      }

::

    https://example.com/miestai/lv

.. code-block:: json

      {
         "miestai": [
            {"id": 207, "miestas": "Ryga"}
         ]
      }

::

    https://example.com/miestai/ee

.. code-block:: json

      {
         "miestai": [
            {"id": 208, "miestas": "Talinas"}
         ]
      }

Tokio API duomenų struktūrą galima aprašyti sekančios :term:`DSA` lentelės
pagalba:

+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
| id | d | r | b | m | property | type    | ref     | source                   | prepare             | access  |
+====+===+===+===+===+==========+=========+=========+==========================+=====================+=========+
|  1 | datasets/example/json    |         |         |                          |                     |         |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
|  2 |   | api                  | json    |         | \https://example.com/{}/ |                     |         |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
|  3 |   | salys                | json    | api     | salys                    |                     |         |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
|  4 |   |   |   | Country      |         | id      | šalys                    |                     |         |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
|  5 |   |   |   |   | id       | integer |         | id                       |                     | private |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
|  6 |   |   |   |   | code     | string  |         | kodas                    |                     | open    |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
|  7 |   |   |   |   | name     | string  |         | šalis                    |                     | open    |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
|  8 |   | miestai              | json    |         | miestai/{country.code}   |                     |         |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
|  9 |   |   |   |   |          | param   | country | Country                  | select()            |         |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
| 10 |   |   |   | City         |         | id      | miestai                  |                     |         |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
| 11 |   |   |   |   | id       | integer |         | id                       |                     | private |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
| 12 |   |   |   |   | country  | ref     | Country |                          | param("country").id | open    |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+
| 13 |   |   |   |   | name     | string  |         | miestas                  |                     | open    |
+----+---+---+---+---+----------+---------+---------+--------------------------+---------------------+---------+

Šį kartą turime reikalą su dinaminiu API, kuris neleidžia gauti visų miestų
vienos užklausos pagalba. Norint gauti visus miestus, pirmiausia gauti visų
šalių kodus, o tada turint šalies kodą, galima gauti tos šalies miestų duomenis.

Kad užduotis nebūtų per daug lengva, šį kartą aprašome visų šalių duomenis,
ne tik Lietuvos.

:data:`model.source` stulpelyje nurodyti JSON atributų pavadinimai, iš kurių
skaitomi duomenys.

8-oje eilutėje, `miestai` :data:`resource` kontekste įtrauktas :ref:`param`
pavadinimu `country`, kuris generuoja parametrus, skaitant duomenis iš 3-ioje
eilutėje aprašyto `Country` :term:`modelio <modelis>`. Tokiu būdu gauname visų
šalių sąrašą ir 7-oje eilutėje :data:`resource.source` galime nurodyti URI su
šalies kodu, gautu iš `country` :ref:`param`.

11-oje eilutėje, `country` reikšmę gauname iš `country` parametro, kadangi
miesto duomenyse, nei miesto kodo, nei `id` nėra.

Galiausiai gauname tokius duomenis:

====  ===========  =================
datasets/example/json/country
------------------------------------
_id   code         name
====  ===========  =================
1     lt           Lietuva
2     lv           Latvija
3     ee           Estija
====  ===========  =================

====  ===========  =================
datasets/example/json/city
------------------------------------
_id   country      name
====  ===========  =================
3     1            Vilnius
4     1            Kaunas
5     1            Klaipėda
6     2            Ryga
7     3            Talinas
====  ===========  =================


XML
===

Tarkime turime XML failą, kuris pasiekiamas adresu
`https://example.com/countries.xml`, failo turinys yra toks:

.. code-block:: xml

    <root>
        <country id="100" code="lt" name="Lietuva">
            <city id="204" name="Vilnius" />
            <city id="205" name="Kaunas" />
            <city id="206" name="Klaipėda" />
        </country>
        <country id="101" code="lv" name="Latvija">
            <city id="207" name="Ryga" />
        </country>
        <country id="102" code="ee" name="Estija">
            <city id="208" name="Talinas" />
        </country>
    </root>

Šio XML failo :term:`DSA` atrodys taip:

+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+
| id | d | r | b | m | property | type    | ref     | source                      | prepare | access  |
+====+===+===+===+===+==========+=========+=========+=============================+=========+=========+
|  1 | datasets/example/xml     |         |         |                             |         |         |
+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+
|  2 |   | api                  | xml     |         | \https://example.com/{}.xml |         |         |
+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+
|  3 |   | countries            | xml     | api     | countries                   |         |         |
+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+
|  4 |   |   |   | country      |         | id      | /root/country               |         |         |
+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+
|  5 |   |   |   |   | id       | integer |         | @id                         |         | private |
+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+
|  6 |   |   |   |   | code     | string  |         | @code                       |         | open    |
+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+
|  7 |   |   |   |   | name     | string  |         | @name                       |         | open    |
+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+
|  8 |   |   |   | city         |         | id      | /root/country/city          |         |         |
+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+
|  9 |   |   |   |   | id       | integer |         | @id                         |         | private |
+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+
| 10 |   |   |   |   | country  | ref     | country | parent::country/@id         |         | open    |
+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+
| 11 |   |   |   |   | name     | string  |         | @name                       |         | open    |
+----+---+---+---+---+----------+---------+---------+-----------------------------+---------+---------+

Šiuo atveju, visi duomenys pateikti viename XML faile, todėl aprašomas tik
vienas :data:`resource`. :data:`model.source` ir :data:`property.source`
stulpelyje pateikiamas `XPath <https://en.wikipedia.org/wiki/XPath>`_ reikšmė,
kuri, jei :data:`prepare` neužpildytas, vykdoma su :func:`xml.xpath` funkcija.

Galutiniame rezultate gauname tokius duomenis:

====  ===========  =================
datasets/example/xml/country
------------------------------------
_id   code         name
====  ===========  =================
1     lt           Lietuva
2     lv           Latvija
3     ee           Estija
====  ===========  =================

====  ===========  =================
datasets/example/xml/city
------------------------------------
_id   country      name
====  ===========  =================
3     1            Vilnius
4     1            Kaunas
5     1            Klaipėda
6     2            Ryga
7     3            Talinas
====  ===========  =================


XLSX
====

Tarkime yra XLSX failas, patalpintas adresu `https://example.com/SALYS.XLSX`,
kuriame yra tokios dvi lentelės:

=========  ==============
ŠALYS
=========================
KODAS      PAVADINIMAS
lt         Lietuva
lv         Latvija
ee         Estija
=========  ==============

=========  ==============
MIESTAI
=========================
ŠALIS      PAVADINIMAS
lt         Vilnius
lt         Kaunas
lt         Klaipėda
lv         Ryga
ee         Talinas
=========  ==============

:term:`Duomenų aprašas <DSA>` atrodys taip:

+----+---+---+---+---+-------------+---------+---------+---------------------------------+-------------------+---------+
| id | d | r | b | m | property    | type    | ref     | source                          | prepare           | access  |
+====+===+===+===+===+=============+=========+=========+=================================+===================+=========+
|    | datasets/example/sql        |         |         |                                 |                   |         |
+----+---+---+---+---+-------------+---------+---------+---------------------------------+-------------------+---------+
|    |   | lentele                 | xlsx    |         | \https://example.com/SALYS.XLSX |                   |         |
+----+---+---+---+---+-------------+---------+---------+---------------------------------+-------------------+---------+
|    |   |   |   | country         |         | code    | ŠALYS                           |                   |         |
+----+---+---+---+---+-------------+---------+---------+---------------------------------+-------------------+---------+
|    |   |   |   |   | code        | string  |         | KODAS                           |                   | open    |
+----+---+---+---+---+-------------+---------+---------+---------------------------------+-------------------+---------+
|    |   |   |   |   | name        | string  |         | PAVADINIMAS                     |                   | open    |
+----+---+---+---+---+-------------+---------+---------+---------------------------------+-------------------+---------+
|    |   |   |   | city            |         | id      | MIESTAI                         |                   |         |
+----+---+---+---+---+-------------+---------+---------+---------------------------------+-------------------+---------+
|    |   |   |   |   | id          | array   |         |                                 | country, name     | private |
+----+---+---+---+---+-------------+---------+---------+---------------------------------+-------------------+---------+
|    |   |   |   |   | country     | ref     | country | ŠALIS                           |                   | open    |
+----+---+---+---+---+-------------+---------+---------+---------------------------------+-------------------+---------+
|    |   |   |   |   | name        | string  |         | PAVADINIMAS                     |                   | open    |
+----+---+---+---+---+-------------+---------+---------+---------------------------------+-------------------+---------+

Šiuo atveju, turime problemą, kad lentelėje nėra pateikti aiškūs
identifikatoriai. Šalių atveju, kaip identifikatorių galima naudoti `KODAS`
stulpelį, tačiau miestų atveju, darant prielaidą, kad skirtingose šalyse gali
būti miestai tokiais pačiai pavadinimais, pirminį raktą formuojame iš šalies
kodo ir miesto pavadinimo, tam įtraukiame naują `id` stulpelį, kuris kuriamas iš
`country` ir `name` reikšmių.


Galutiniame rezultate gauname tokius duomenis.

====  ===========  =================
datasets/example/xml/country
------------------------------------
_id   code         name
====  ===========  =================
1     lt           Lietuva
2     lv           Latvija
3     ee           Estija
====  ===========  =================

====  ===========  =================
datasets/example/xml/city
------------------------------------
_id   country      name
====  ===========  =================
3     1            Vilnius
4     1            Kaunas
5     1            Klaipėda
6     2            Ryga
7     3            Talinas
====  ===========  =================

Spinta
======

Last data source example using same data source to transfer all country and
city data from all other data sources into on globale data source under

Paskutinis pavyzdys atliekant transformaciją tos pačios duomenų saugyklos
viduje. Visi duomenys aukščiau aprašytuose pavyzdžiuose bus apjungiami ir
perkelti į standartų vardų erdvę. Tokiu būdu, turėsime vieną aiškią duomenų
struktūrą, visiems iki šilo aprašytiems duomenų šaltiniams.

Tokia transformacijų :term:`DSA` atrodo taip:

== == == == ======== ======== ============= ==========================
d  r  b  m  property type     ref           source
== == == == ======== ======== ============= ==========================
geo                  ns
-------------------- -------- ------------- --------------------------
\        Country
-- -- -- ----------- -------- ------------- --------------------------
\           code     string
\           name     string
\        City
-- -- -- ----------- -------- ------------- --------------------------
\           country  ref      Country
\           name     string
transformations/geo
-------------------- -------- ------------- --------------------------
\  data              spinta                 \https://example.com/
-- ----------------- -------- ------------- --------------------------
\     /geo/Country   proxy    code
-- -- -------------- -------- ------------- --------------------------
\        Country                            /datasets/example/{source}
-- -- -- ----------- -------- ------------- --------------------------
\                    param    source        sql
\                                           csv
\                                           json
\                                           xml
\                                           xlsx
\           code     string                 code
\           name     string                 name
\     /geo/City      proxy    country, name
-- -- -------------- -------- ------------- --------------------------
\        City
-- -- -- ----------- -------- ------------- --------------------------
\           country  ref      Country       country
\           name     string                 name
== == == == ======== ======== ============= ==========================

Pirmiausiai apibrėžiame `geo` standarto duomenų struktūrą, toliau nurodome
duomenų šaltinį `spinta`, kurio :data:`resource.source` sutampa su saugyklos
adresu.

`source` parametrui priskiriame sąrašą visų iki šiol aprašytų duomenų rinkinių
ir šio parametro pagalba skaitome visų šaltinių duomenis ir :data:`base.type`
`proxy` pagalba siunčiame visus juos į `geo` vardų erdvę.

:data:`base.ref` stulpelyje nurodome, kaip bus identifikuojami :term:`objektai
<objektas>`, kad neatsirastu dublikatų.

Galutiniame rezultate, gausime tokius duomenis:

====  ===========  =================
geo/country
------------------------------------
_id   code         name
====  ===========  =================
1     lt           Lietuva
2     lv           Latvija
3     ee           Estija
====  ===========  =================

====  ===========  =================
geo/city
------------------------------------
_id   country      name
====  ===========  =================
3     1            Vilnius
4     1            Kaunas
5     1            Klaipėda
6     2            Ryga
7     3            Talinas
====  ===========  =================
