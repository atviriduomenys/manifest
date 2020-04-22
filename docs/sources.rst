.. default-role:: literal

.. _sources:

Duomenų šaltiniai
#################

Duomenų šaltinių aprašai leidžia automatizuoti duomenų surinkimą iš įvairių
šaltinių, juos patikrinti ir konvertuoti į kitus formatus.

Šaltinio duomenų struktūros aprašas YAML formatu atrodo taip:

.. code-block:: yaml

   # <rinkinys>.dataset.yml
   type: dataset
   name: <rinkinys>
   resources:
     <resursas>:
       type: <šaltinio tipas>
       source: <resurso šaltinis>

.. code-block:: yaml

   # <modelis>.yml
   type: model
   name: <modelis>
   base:
     model: <bazinis modelis>
     pk: <identifikatorius>
   source:
     dataset: <rinkinys>
     resource: <resursas>
     name: <modelio šaltinis>
     pk: <identifikatorius>
   properties:
     <savybė>:
       type: <savybės tipas>
       source: <savybės šaltinis>

.. code-block:: yaml

   # <bazinis modelis>.yml
   type: model
   name: <bazinis modelis>
   properties:
     <savybė>:
       type: <savybės tipas>

Šis aprašas yra suderinamas su DCAT_ žodynu, tačiau DCAT_ žodyno elementai
sudaro tik nedidelę dalį. Šaltinio aprašas yra išplėstas ir leidžia aprašyti ne
tik duomenų rinkinio ir resurso metaduomenis, bet ir detalią objektų ir savybių
struktūrą, duomenų šaltinius, susieti pavadinimus su vieningu žodynu ir pan.

.. _DCAT: https://www.w3.org/TR/vocab-dcat/

Šaltinio duomenų aprašo pagrindą sudaro:

- rinkinys
- resursas
- modelis
- savybė

Žemiau pateikiami išsamesni apraše naudojamų elementų pažymėtų `<>` žymėmis
aprašymai.

rinkinys
   Duomenių rinkinio :term:`sisteminis pavadinimas`. Duomenų rinkinys jungia
   vieną ar kelis duomenų išteklius (resursus).

resursas
   Resurso pavadinimas gali būti bet koks, tačiau prasminga jį sieti su duomenų
   bazės ar duomenų failo pavadinimu.

šaltinio tipas
   Šiuo metu palaikomi tokie šaltinio tipai:

   - `csv`
   - `html`
   - `json`
   - `sql`
   - `xlsx`
   - `xml`

   Priklausomai nuo šaltinio tipo keičiasi visų kitų elementu interpretavimas.

resurso šaltinis
   Gali būti duomenų bazė, JSON, XML ar skaičiuoklės failas. Priklauso nuo
   šaltinio tipo.

modelis
   Modelio pavadinimas gali būti bet koks pavadinimas, tačiau rekomenduojama
   duomenų rinkinio pavadinimą formuoti iš rinkinio pavadinimo, pavyzdžiui
   `<rinkinys>/<modelis>`.

objekto šaltinis
   Priklausomai nuo duomenų šaltinio, gali būti duomenų bazės lentelė, CSV
   failas, JSON elemento kelias, XPath ar skaičiuoklės lapo pavadinimas.

savybė
   Objekto savybės pavadinimas.

savybės tipas
   Šiuo metu paliekami šie duomenų tipai:

   - `pk` - pirminis raktas
   - `ref` - ryšys su kitu objektu
   - `backref` - atgalinis ryšys su kitu objektu
   - `generic` - ryšis su kitu neapibrėžtu objektu
   - `array` - masyvas, kuris gali būti sudarytas iš bet kokių kitų tipų reikšmių
   - `object` - objektas, kuris gali būti sudarytas iš bet kokių kitų tipų
     reikšmių
   - `string` - bet kokio ilgio simbolių eilutė
   - `binary` - dvejetainiai duomenys
   - `integer` - sveikas skaičius, gali būti neigiamas
   - `number` - racionalusis skaičius
   - `boolean` - loginis tipas
   - `date` - data
   - `datetime` - data ir laikas
   - `spatial` - erdviniai duomenys, gali būti taškas, linija arba plokštuma
   - `file` - failas
   - `image` - paveiksliukas
   - `url` - URL adresas

savybės šaltinis
   Priklausomai nuo šaltinio, gali būti duomenų bazės lentelės laukas, JSON
   objekto savybė, reliatyvus XPath, skaičiuoklės lapo stulpelis.

Resurso, objekto ir savybės šaltiniai (`source/name` parametras) priklauso nuo
šaltinio tipo, žemiau pateikti visų palaikomų šaltinių aprašymai su
paaiškinimais kaip interpretuojamas `source/name` kiekvienam iš jų.

Visuose pavyzdžiuose naudojama tie patys šalies duomenys, tik duomenys
pateikiami skirtingais formatais, tačiau galutinis rezultatas visais atvejais
yra identiškas.


Visų žemiau pateiktų duomenų rinkinių inventorizacijos lentelė atrodo taip:

+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
| id | d | r | b | m | property    | source                             | prepare | type    | ref   | level | access  | uri | title        | description     |
+====+===+===+===+===+=============+====================================+=========+=========+=======+=======+=========+=====+==============+=================+
|    | datasets/pavyzdys/sql       |                                    |         |         |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   | sql                     | postgresql://user@host/dbname      |         | sql     |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   | geografija/salis    |                                    |         |         | kodas |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   | salis           | COUNTRY                            |         |         | id    |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | id          | id                                 |         | integer |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | kodas       | code                               |         | string  |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | pavadinimas | country                            |         | string  |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    | datasets/pavyzdys/csv       |                                    |         |         |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   | csv                     | https://example.com/               |         | csv     |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   | geografija/salis    |                                    |         |         | kodas |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   | salis           | countries.csv                      |         |         | id    |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | id          | id                                 |         | integer |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | kodas       | code                               |         | string  |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | pavadinimas | country                            |         | string  |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    | datasets/pavyzdys/json      |                                    |         |         |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   | json                    | https://example.com/countries.json |         | json    |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   | geografija/salis    |                                    |         |         | kodas |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   | salis           | countries                          |         |         | id    |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | id          | id                                 |         | integer |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | kodas       | code                               |         | string  |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | pavadinimas | country                            |         | string  |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    | datasets/pavyzdys/xml       |                                    |         |         |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   | xml                     | https://example.com/countries.xml  |         | xml     |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   | geografija/salis    |                                    |         |         | kodas |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   | salis           | xpath('/root/country')             |         |         | id    |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | id          | id                                 |         | integer |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | kodas       | code                               |         | string  |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | pavadinimas | text()                             |         | string  |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    | datasets/pavyzdys/xlsx      |                                    |         |         |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   | xlsx                    | https://example.com/countries.xlsx |         | xlsx    |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   | geografija/salis    |                                    |         |         | kodas |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   | salis           | COUNTRIES                          |         |         | id    |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | id          | id                                 |         | integer |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | kodas       | code                               |         | string  |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+
|    |   |   |   |   | pavadinimas | country                            |         | string  |       |       |         |     |              |                 |
+----+---+---+---+---+-------------+------------------------------------+---------+---------+-------+-------+---------+-----+--------------+-----------------+

Žodyno lentelė atrodo taip:

+----+---+---+--------------+--------+---------+---------+-----+-------+--------+-----------------------+---------------------+-------------+
| id | b | m | property     | source | prepare | type    | ref | level | access | uri                   | title               | description |
+====+===+===+==============+========+=========+=========+=====+=======+========+=======================+=====================+=============+
|    |   | geografija/salis |        |         |         |     |       |        | schema:Country        | Šalis               |             |
+----+---+---+--------------+--------+---------+---------+-----+-------+--------+-----------------------+---------------------+-------------+
|    |   |   | kodas        |        |         | string  |     |       |        | esco:isoCountryCodeA2 | ISO 3166-1 A2 kodas |             |
+----+---+---+--------------+--------+---------+---------+-----+-------+--------+-----------------------+---------------------+-------------+
|    |   |   | pavadinimas  |        |         | string  |     |       |        | og:country-name       | Pavadinimas         |             |
+----+---+---+--------------+--------+---------+---------+-----+-------+--------+-----------------------+---------------------+-------------+


SQL
===

SQL arba reliacinės duomenų bazių valdymo sistemos.

resurso šaltinis
   SQL resurso šaltinis nurodo duomenų bazę, kurios duomenų struktūra aprašoma.

   Dažniausiai duomenų bazės prisijungimai nėra nurodomas duomenų struktūros
   apraše, kadangi duomenų bazės prisijungimai negali būti viešinami. Duomenų
   bazės prisijungimai turi būti perduodami per :term:`aplinkos kintamuosiuos
   <aplinkos kintamasis>` arba konfigūracijos failus.

   :term:`Aplinkos kintamasis <aplinkos kintamasis>` formuojamas taip::

      SPINTA_DATASETS_{manifest.name}_{dataset.name}_{resource.name}

   `{manifest.name}` dažniausiai bus `default`, nebent naudojante kelis
   manifestų katalogus.

   Duomenų bazės šaltinis aprašomas naudojant tokią URL schemą::

      <db>+<valdiklis>://<naudotojas>:<slaptažodis>@<serveris>:<prievadas>/<pavadinimas>

   db
      Duomenų bazės rūšis:

      - `sqlite`
      - `postgresql`
      - `mysql`
      - `mssql`

   valdiklis
      Konkretus duomenų bazės valdiklis (angl. *driver*) naudojamas
      komunikacijai su duomenų baze.

   naudotojas, slaptažodis
      Duomenų bazės naudotojas ir jo slaptažodis.

   serveris, prievadas
      Serveris ir serverio prievadas kur veikia duomenų bazė.

   pavadinimas
      Duomenų bazės pavadinimas.


objekto šaltinis
   Duomenų bazės lentelės pavadinimas.

savybės šaltinis
   Lentelės lauko pavadinimas.


Pavyzdys
--------

Tarkime turime PostgreSQL duomenų bazę, kurioje yra lentelę pavadinimu
`COUNTRY`, lentelėje yra tokie duomenys:

=======  ========  ===========
id       code      country
=======  ========  ===========
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ===========

Šios lentelės duomenų aprašas atrodys taip:

.. code-block:: yaml

   # datasets/pavyzdys/sql.dataset.yml
   type: dataset
   name: datasets/pavyzdys/sql
   resources:
     sql:
       type: sql
       source: postgresql://user@host/dbname

.. code-block:: yaml

   # datasets/pavyzdys/sql/salis.yml
   type: model
   name: datasets/pavyzdys/sql/salis
   base:
     model: geografija/salis
     pk: kodas
   source:
     dataset: datasets/pavyzdys/sql
     resource: sql
     name: COUNTRY
     pk: id
   properties:
     id:
       type: integer
       source: id
     kodas:
       type: string
       source: code
     pavadinimas:
       type: string
       source: country

.. code-block:: yaml

   # geografija/salis.yml
   type: model
   name: geografija/salis
   properties:
     kodas:
       type: string
       source: code
     pavadinimas:
       type: string
       source: country
     

Pavyzdyje duomenų šaltinis nurodytas tiesiogiai pačiame YAML faile, tačiau
šaltinį galima nurodyti ir :term:`aplinkos kintamojo <aplinkos kintamasis>`
pagabla::

      SPINTA_DATASETS_DEFAULT_PAVYZDZIAI_SQL_DUOMBAZE=postgresql://user@host/dbname

Rezultate gauname atvertus duomenis, kuriuos galima pasiekti per šiuos prieigos
taškus::

  /geografija/salis

Atverta lentelė atrodys taip:

====================================  ===========  =================
_id                                   kodas        pavadinimas
====================================  ===========  =================
52d2c389-a909-4241-9a7c-91f108f7b0bb  lt           Lietuva
9bbcbd34-7d9a-471c-a434-e73d63e01e01  lv           Latvija
3680df71-aea6-490b-ab66-1b26e4923259  ee           Estija
====================================  ===========  =================

Taip pat galima pasiekti ir pirminius šaltinio duomenis::

  /datasets/pavyzdys/sql/salis


CSV
===

Kableliais atskirti failai.

resurso šaltinis
   Gali būti nenurodomas, o jei nurodomas naudojamas kaip URL bazė objekto
   šaltiniui.

objekto šaltinis
   Pilnas URL iki CSV failo arba reliatyvus kelias iki CSV failo, jei nurodytas
   resurso šaltinis.

savybės šaltinis
   Stulpelio pavadinimas iš CSV failo.


Pavyzdys
--------

Tarkime turime CSV failą, kuris pasiekiamas adresu
`https://example.com/countries.csv`, failo turinys yra toks::

   id,code,country
   1,lt,Lietuva
   2,lv,Latvija
   3,ee,Estija

Šio CSV failo duomenų aprašas atrodys taip:

.. code-block:: yaml

   # datasets/pavyzdys/csv.dataset.yml
   type: dataset
   name: datasets/pavyzdys/csv
   resources:
     csv:
       type: csv
       source: https://example.com/


.. code-block:: yaml

   # datasets/pavyzdys/csv/salis.csv
   type: model
   name: datasets/pavyzdys/csv/salis
   base:
     model: geografija/salis:
     pk: kodas
   source:
     dataset: datasets/pavyzdys/csv
     resource: csv
     name: countries.csv
     pk: id
   properties:
     id:
       type: integer
       source: id
     kodas:
       type: string
       source: code
     pavadinimas:
       type: string
       source: country

.. code-block:: yaml

   # geografija/salis.yml
   type: model
   name: geografija/salis
   properties:
     kodas:
       type: string
     pavadinimas:
       type: string

Rezultate gauname atvertus duomenis, kuriuos galima pasiekti per šį prieigos
tašką::

   /geografija/salis

Atverta lentelė atrodys taip:

====================================  ===========  =================
_id                                   kodas        pavadinimas
====================================  ===========  =================
52d2c389-a909-4241-9a7c-91f108f7b0bb  lt           Lietuva
9bbcbd34-7d9a-471c-a434-e73d63e01e01  lv           Latvija
3680df71-aea6-490b-ab66-1b26e4923259  ee           Estija
====================================  ===========  =================

Taip pat galima pasiekti ir pirminius šaltinio duomenis::

  /datasets/pavyzdys/csv/salis


JSON
====

resurso šaltinis
   URL iki JSON failo.

objekto šaltinis
   Kelias iki konkretaus elemento JSON duomenyse. Pavyzdžiui, jei turime tokį
   JSON failą:

   .. code-block:: json

      {
         "foo": {
            "bar": [
               {"baz": 1},
               {"baz": 2},
               {"baz": 3}
            ]
         }
      }

   Tada objekto šaltinis gali būti `foo.bar`, kas nurodo, kad skaitomas tik
   `foo.bar` esantis masyvas.

   Jei objekto šaltinis nenurodytas, tada savybės skaitomos iš šakninio JSON
   objekto.

savybės šaltinis
   JSON objekto atributas.


Pavyzdys
--------

Tarkime turime JSON failą, kuris pasiekiamas adresu
`https://example.com/countries.json`, failo turinys yra toks:

.. code-block:: json

   {
       "countries": [
           {"id": 1, "code": "lt", "name": "Lietuva"},
           {"id": 1, "code": "lv", "name": "Latvija"},
           {"id": 1, "code": "ee", "name": "Estija"}
       ]
   }

Šio JSON failo duomenų aprašas atrodys taip:

.. code-block:: yaml

   # datasets/pavyzdys/json.dataset.yml
   type: dataset
   name: datasets/pavyzdys/json
   resources:
     json:
       type: json
       source: https://example.com/countries.json

.. code-block:: yaml

   # datasets/pavyzdys/json/salis.yml
   type: model
   name: datasets/pavyzdys/json/salis
   base:
     model: geografija/salis:
     pk: kodas
   source:
     dataset: datasets/pavyzdys/json
     resource: json
     name: countries
     pk: id
   properties:
     id:
       type: integer
       source: id
     kodas:
       type: string
       source: code
     pavadinimas:
       type: string
       source: name

.. code-block:: yaml

   # geografija/salis.yml
   type: model
   name: geografija/salis
   properties:
     kodas:
       type: string
     pavadinimas:
       type: string

Rezultate gauname atvertus duomenis, kuriuos galima pasiekti per šį prieigos
tašką::

   /geografija/salis

Atverta lentelė atrodys taip:

====================================  ===========  =================
_id                                   kodas        pavadinimas
====================================  ===========  =================
52d2c389-a909-4241-9a7c-91f108f7b0bb  lt           Lietuva
9bbcbd34-7d9a-471c-a434-e73d63e01e01  lv           Latvija
3680df71-aea6-490b-ab66-1b26e4923259  ee           Estija
====================================  ===========  =================

Taip pat galima pasiekti ir pirminius šaltinio duomenis::

  /datasets/pavyzdys/json/salis


XML
===

resurso šaltinis
   URL iki XML failo.

objekto šaltinis
   XPath užklausa iki elemento iš kurio norime imti duomenis.

savybės šaltinis
   XPath užklausa, kuri vykdoma objekto šaltinio elementų kontekste.


Pavyzdys
--------

Tarkime turime XML failą, kuris pasiekiamas adresu
`https://example.com/countries.xml`, failo turinys yra toks:

.. code-block:: xml

   <root>
      <country id="1" code="lt">Lietuva</country>
      <country id="2" code="lv">Latvija</country>
      <country id="3" code="ee">Estija</country>
   </root>

Šio XML failo duomenų aprašas atrodys taip:

.. code-block:: yaml

   # datasets/pavyzdys/json.dataset.yml
   type: dataset
   name: datasets/pavyzdys/xml
   resources:
     xml:
       type: xml
       source: https://example.com/countries.xml

.. code-block:: yaml

   # datasets/pavyzdys/json/salis.yml
   type: model
   name: datasets/pavyzdys/json/salis
   base:
     model: geografija/salis:
     pk: kodas
   source:
     dataset: datasets/pavyzdys/json
     resource: json
     name: xpath('/root/country')
     pk: id
   properties:
     id:
       type: integer
       source: id
     kodas:
       type: string
       source: code
     pavadinimas:
       type: string
       source: text()

.. code-block:: yaml

   # geografija/salis.yml
   type: model
   name: geografija/salis
   properties:
     kodas:
       type: string
     pavadinimas:
       type: string

Rezultate gauname atvertus duomenis, kuriuos galima pasiekti per šį prieigos
tašką::

   /geografija/salis

Atverta lentelė atrodys taip:

====================================  ===========  =================
_id                                   kodas        pavadinimas
====================================  ===========  =================
52d2c389-a909-4241-9a7c-91f108f7b0bb  lt           Lietuva
9bbcbd34-7d9a-471c-a434-e73d63e01e01  lv           Latvija
3680df71-aea6-490b-ab66-1b26e4923259  ee           Estija
====================================  ===========  =================

Taip pat galima pasiekti ir pirminius šaltinio duomenis::

  /datasets/pavyzdys/xml/salis


XLSX
====

resurso šaltinis
   URL iki XLSX failo.

objekto šaltinis
   Skaičiuoklės lapo pavadinimas.

savybės šaltinis
   Skaičiuoklės lentelės stulpelio pavadinimas.


Pavyzdys
--------

Tarkime turime XLSX failą, kuris pasiekiamas adresu
`https://example.com/countries.xlsx`, šiame skaičiuoklės faile yra lapas
pavadinimu `COUNTRIES`, o lapo turinys atrodo taip:

=======  ========  ===========
id       code      country
=======  ========  ===========
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ===========

Šios lentelės duomenų aprašas atrodys taip:

.. code-block:: yaml

   # datasets/pavyzdys/xlsx.dataset.yml
   type: dataset
   name: datasets/pavyzdys/xlsx
   resources:
     xlsx:
       type: xlsx
       source: https://example.com/countries.xlsx

.. code-block:: yaml

   # datasets/pavyzdys/xlsx/salis.yml
   type: model
   name: datasets/pavyzdys/xlsx/salis
   base:
     model: geografija/salis:
     pk: kodas
   source:
     dataset: datasets/pavyzdys/xlsx
     resource: json
     name: COUNTRIES
     pk: id
   properties:
     id:
       type: integer
       source: id
     kodas:
       type: string
       source: code
     pavadinimas:
       type: string
       source: country

.. code-block:: yaml

   # geografija/salis.yml
   type: model
   name: geografija/salis
   properties:
     kodas:
       type: string
     pavadinimas:
       type: string

Rezultate gauname atvertus duomenis, kuriuos galima pasiekti per šį prieigos
tašką::

   /geografija/salis

Atverta lentelė atrodys taip:

====================================  ===========  =================
_id                                   kodas        pavadinimas
====================================  ===========  =================
52d2c389-a909-4241-9a7c-91f108f7b0bb  lt           Lietuva
9bbcbd34-7d9a-471c-a434-e73d63e01e01  lv           Latvija
3680df71-aea6-490b-ab66-1b26e4923259  ee           Estija
====================================  ===========  =================

Taip pat galima pasiekti ir pirminius šaltinio duomenis::

  /datasets/pavyzdys/xlsx/salis
