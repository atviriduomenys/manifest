.. manifest documentation master file, created by
   sphinx-quickstart on Sun Jul  7 15:44:01 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. default-role:: literal

Atvirų duomenų manifestas
#########################

Atvirų duomenų manifestas yra visų Lietuvos duomenų rodyklė. Kitais žodžiais
tai yra metaduomenys (duomenys apie duomenis). 

Pavyzdžiui, jei visi Lietuvos duomenys būtų sukrauti į didelę spintą ir
didžioji dalis spintos turinio būtų skolinta iš kitų spintų, tai atvirų duomenų
manifestas būtų lapelis užkabintas ant spintos durų, kuriame surašyta kas, kur,
kada, iš ko pasiskolino, kada grąžinti ir pan.

Metaduomenys leidžia automatizuoti duomenų valdymą įdarbinant robotus, kurie
automatizuotų didelę dalį veiklų susijusių su duomenų valdymu.

.. image:: static/spinta.png

Į šio projekto apimtį įeina ne tik informacija kaip aprašyti metaduomenis, bet
teikiami įrankiai, kurie metaduomenų pagrindu automatizuoja daugelį duomenų
atvėrimo ir pateikimo naudojimui veiklų.

Manifesto (lapelis ant spintos) sudarymo procesas vadinamas duomenų
`inventorizacija <inventorying>`:ref:. Tarkime, kaip pavyzdį, galime panagrinėti
išgalvotos įstaigos „Duomenų centras“ sutrumpintai vadinamos DC duomenis. DC
duomenų bazėje yra lentelė techniniu pavadinimu `COUNTRIES`, lentelės
turinys atrodo taip:

=======  ========  ===========
COUNTRIES
------------------------------
id       code      country
=======  ========  ===========
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ===========

Įstaiga „Duomenų centras“ nori atverti duomenis. Pirmas žingsnis būtų duomenų
inventorizacija. Duomenų inventorizacijos metu sudaromi įstaigoje esančių
duomenų laukų sąrašai, kurie atrodo taip:

+---+---+---+---+-----------+-----------+---------+-----+-------+--------+-------+-------------+
| d | r | b | m | property  | source    | type    | ref | level | access | title | description |
+===+===+===+===+===========+===========+=========+=====+=======+========+=======+=============+
| datasets/gov/dc/countries |           |         |     |       |        |       |             |
+---+---+---+---+-----------+-----------+---------+-----+-------+--------+-------+-------------+
|   | sql                   |           |         |     |       |        |       |             |
+---+---+---+---+-----------+-----------+---------+-----+-------+--------+-------+-------------+
|   |   |                   |           |         |     |       |        |       |             |
+---+---+---+---+-----------+-----------+---------+-----+-------+--------+-------+-------------+
|   |   |   | countries     | COUNTRIES |         | id  |       |        |       |             |
+---+---+---+---+-----------+-----------+---------+-----+-------+--------+-------+-------------+
|   |   |   |   | id        | id        | integer |     | 4     |        |       |             |
+---+---+---+---+-----------+-----------+---------+-----+-------+--------+-------+-------------+
|   |   |   |   | code      | code      | string  |     | 2     |        |       |             |
+---+---+---+---+-----------+-----------+---------+-----+-------+--------+-------+-------------+
|   |   |   |   | name      | country   | string  |     | 2     |        |       |             |
+---+---+---+---+-----------+-----------+---------+-----+-------+--------+-------+-------------+

Tokią pirminę inventorizacijos lentelę daugeliu atveju galima sugeneruoti
automatiškai iš duomenų šaltinio.

Deja ne viską galima automatizuoti, toliau prasideda rankinis darbas su
lentele:

- `access` stulpelyje surašomas duomenų prieinamumas

- `level` stulpelyje pateikiamas duomenų brandos lygis

- `source` stulpelyje vykdoma duomenų atranka ir transformacija

- `ref` stulpelyje tvarkomi objektų identifikatoriai ir ryšiai tarp lentelių

- `base` stulpelyje duomenų šaltinio modelis „verčiamas“ arba siejamas su baziniu modeliu

- `property` stulpelyje „verčiami“ modelio laukų pavadinimai, kad atitiktų
  bazinio modelio laukų pavadinimus.

- `title` ir `description` stulpeliuose pateikiami pavadinimai ir aprašymai,
  kad būtų aiškiau kaip naudoti duomenis

- galiausiai tvarkomi baziniai modeliai, „verčiami“ į pasaulinius žodynus

Galiausiai atlikus visus išvardintus žingsnius gauname tokią pilnai sutvarkytą
inventorizacijos lentelę:

+---+---+---+---+-----------+-----------+---------+------+-------+---------+--------------+-----------------+
| d | r | b | m | property  | source    | type    | ref  | level | access  | title        | description     |
+===+===+===+===+===========+===========+=========+======+=======+=========+==============+=================+
| datasets/gov/dc/countries |           |         |      |       |         | Šalys        |                 |
+---+---+---+---+-----------+-----------+---------+------+-------+---------+--------------+-----------------+
|   | sql                   |           |         |      |       |         | Duomenų bazė |                 |
+---+---+---+---+-----------+-----------+---------+------+-------+---------+--------------+-----------------+
|   |   | place/country     |           |         | code |       |         | Šalis        |                 |
+---+---+---+---+-----------+-----------+---------+------+-------+---------+--------------+-----------------+
|   |   |   | country       | COUNTRIES |         | id   |       |         | Šalis        |                 |
+---+---+---+---+-----------+-----------+---------+------+-------+---------+--------------+-----------------+
|   |   |   |   | id        | id        | integer |      | 5     | private |              |                 |
+---+---+---+---+-----------+-----------+---------+------+-------+---------+--------------+-----------------+
|   |   |   |   | code      | code      | string  |      | 5     | open    | Šalies kodas | Dviejų simbolių |
|   |   |   |   |           |           |         |      |       |         |              | šalies kodas.   |
+---+---+---+---+-----------+-----------+---------+------+-------+---------+--------------+-----------------+
|   |   |   |   | name      | country   | string  |      | 5     | open    | Pavadinimas  |                 |
+---+---+---+---+-----------+-----------+---------+------+-------+---------+--------------+-----------------+

Ši inventorizacijos lentelė yra susieta su baziniais modeliais. Baziniai
modeliai sudaro vidinį manifesto žodyną ir yra susieti su pasauliniais
žodynais. Galutinė bazinių modelių lentelė atrodo taip:

+---+-----------------+--------+-----+-----------------------+---------------------+-------------+
| m | property        | type   | ref | uri                   | title               | description |
+===+=================+========+=====+=======================+=====================+=============+
| place/country       |        |     | schema:Country        | Šalis               |             |
+---+-----------------+--------+-----+-----------------------+---------------------+-------------+
|   | code            | string |     | esco:isoCountryCodeA2 | ISO 3166-1 A2 kodas |             |
+---+-----------------+--------+-----+-----------------------+---------------------+-------------+
|   | name            | string |     | og:country-name       | Pavadinimas         |             |
+---+-----------------+--------+-----+-----------------------+---------------------+-------------+


Manifestas
----------

Inventorizacijos lentelė yra tik patogesnė priemonė metaduomenų valdymui.
Tačiau, pagrindinis metaduomenų formatas yra manifesto YAML failai.

Darbas su inventorizacijos lentele yra patogus ir paprastas, tačiau deja kai
kurios sudėtingesnės automatizavimo veiklos reikalauja žymiai daugiau
metaduomenų. O turėti didelį kiekį metaduomenų vienoje lentelėje yra tiesiog
nepraktiška.  Todėl paprasti dalykai ir pirminė inventorizacija daroma
lentelėse, sudėtingesni dalykai ir pilnas duomenų aprašas yra YAML failuose.

Visi įrankiai dirba su YAML failais. YAML failus galima nuskaityti mašininiu
būdu, tačiau YAML sintaksė yra lengvai suprantama ir žmonėms. Štai kaip
atrodytų mūsų inventorizacijos lentelė YAML formatu:

.. code-block:: yaml

   # datasets/gov/dc/countries.dataset.yml
   type: dataset
   name: datasets/gov/dc/countries
   title: Šalys
   resources:
     countries:
       type: sql
       title: Duomenų bazė
       source: postgresql://user:password@host/dbname

.. code-block:: yaml

   # datasets/gov/dc/countries/country.yml
   type: model
   name: datasets/gov/dc/countries/country
   title: Šalys
   base:
     model: place/country
     pk: code
   pull:
     dataset: datasets/gov/dc/countries
     resource: countries
     source: COUNTRIES
     pk: id
   properties:
     id:
       type: integer
       pull: id
       level: 5
       access: private
     code:
       type: string
       pull: code
       level: 5
       access: open
       title: Šalies kodas
       description: Dviejų simbolių šalies kodas.
     name:
       type: string
       pull: country
       level: 5
       access: open
       title: Pavadinimas

.. code-block:: yaml

   # place/country.yml
   type: model
   name: place/country
   title: Šalis
   uri: schema:Country
   properties:
     code:
       type: string
       uri: esco.isoCountryCodeA2
       title: ISO 3166-1 A2 kodas
       unique: true
       required: true
       prepare:
         - check(len() = 2, "Šalies kodas turi būti dviejų simbolių ilgio.")
         - lower()
     name:
       type: string
       uri: og.country-name
       title: Pavadinimas
       required: true
       prepare:
         - check(len() > 0)

Tokie duomenų aprašai leidžia pateikti daug daugiau informacijos apie duomenų
šaltinį, tačiau failo formatas yra kiek sudėtingesnis, nei inventorizacijos
lentelės. Todėl pirminė inventorizacija atliekama lentelės pagalba, o
išplėstinė, YAML failų pagalba.

Tarpinė duomenų saugykla
------------------------

Pasidarius tokią inventorizaciją, automatinėmis priemonėmis, duomenys
kopijuojami iš pirminio duomenų šaltinio į tarpinę duomenų saugyklą. Tarpinė
duomenų saugykla nėra prieinama iš išorės ir turėtų veikti įstaigos
atveriančios duomenis infrastruktūroje.

Tarpinėje duomenų saugykloje atliekami visi nuasmeninimo, transformacijos,
vertimo į manifesto žodyną ir kiti darbai. Kad neatskleisti jautrios
informacijos, visi šie darbai turi būti atliekami tarpinėje saugykloje, kad
duomenys, kol dar nėra iki galo paruošti, nepaliktų įstaigos infrastruktūros
ribų.

Galiausiai ištestuoti ir patvirtinti atvėrimui duomenų rinkiniai keliauja į
viešąją duomenų saugyklą, kuri yra pasiekiama adresu https://atviriduomenys.lt.

Viešoji duomenų saugykla leidžia duomenis atsisiųsti įvairiais formatais,
suteikia vieningą API duomenų integracijai ir suteikia įvairias priemones
darbui su duomenimis. Duomenų naudotojai gali rašyti užklausas, jungti duomenis
tarpusavyje, sekti pasikeitimus duomenyse, matyti kokios klaidos įvyko
apdorojant duomenis ir pan.

Tiek vidinėje saugykloje, tiek viešojoje saugykloje, pagrindinis integracijos
taškas yra manifesto YAML failai. Atvėrus duomenis iš tarpinės duomenų
saugyklos, vidiniai YAML failai transformuojami į viešai prieigai tinkantį
pavidalą, kur yra paslėpti vidinių duomenų bazių pavadinimai, transformacijų
aprašai ir pan. Šis viešasis manifesto variantas skelbiamas
`atviriduomenys/manifest`_ kodo repozitorijoje.

.. _atviriduomenys/manifest: https://gitlab.com/atviriduomenys/manifest

Duomenų naudotojai, pastebėję klaidas, gali užregistruoti pranešimą `užduočių
valdymo sistemoje`__. Užduočių valdymo sistema yra atvira ir integruota su kodo
repozitorija. Viešoji manifesto dalis yra atviro kodo, todėl visi gali
įsitraukti ir tiksliai matyti kas vyksta.

.. __: https://gitlab.com/atviriduomenys/manifest/issues

Paskutinis žingsnis - suformuotas duomenų rinkinys užregistruojamas atvirų
duomenų vitrinoje adresu https://data.gov.lt, kad duomenų naudotojai galėtų
rasti duomenis.


Turinys
=======

.. toctree::
   :maxdepth: 2

   inventorying
   sources
   pk
   norm
   dependencies
   vocabulary
   api
   glossary
   contributing
