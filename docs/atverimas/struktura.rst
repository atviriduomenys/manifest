.. default-role:: literal

.. _detali-inventorizacija:

##########################
Duomenų struktūros aprašas
##########################

.. image:: /static/zingsnis_3.png

Duomenų struktūros aprašas rengiamas tada, kai atsiranda prašymas atverti
duomenis arba savo nuožiūra įvertinus duomenų paklausos potencialą.

Kas yra duomenų struktūros aprašas?
***********************************

.. image:: /static/struktura.png

Duomenų struktūros apraše pateikiama duomenų struktūros išklotinė išvardinant
visus duomenų laukus, kurie bus atverti.

Duomenų struktūros apraše pateikiama pilna duomenų laukų išklotinė.

Duomenų laukai yra skirstomi į modelius. **Modelio** ir **savybės** tiksli
prasmė priklauso nuo aprašomo duomenų šaltinio:

========  =======  =========
Šaltinis  Modelis  Savybė
========  =======  =========
SQL       Lentelė  Stulpelis
CSV       Lentelė  Stulpelis
XLSX      Lentelė  Stulpelis
JSON      Masyvas  Atributas
XML       Masyvas  Atributas
RDF       Klasė    Savybė
========  =======  =========

Duomenų struktūros apraše galima aprašyti įvairių duomenų šaltinių turinį
vieningu sutartiniu būdu.


.. _sdsa-gavimas:

Iš kur gauti ŠDSA?
******************

.. image:: /static/sdsa-gavimas.png

1. :ref:`paruošimo-sutartis`
2. :ref:`šdsa-paruošimas`
3. :ref:`šdsa-suderinimas`
4. :ref:`atvėrimo-sutartis`
5. :ref:`adsa-publikavimas`

.. _paruošimo-sutartis:

Infrastruktūros paruošimo sutartis
==================================

Atliekant duomenų atvėrimo darbus gali būti reikalingos dvi sutartys. viena
yra reikalinga infrastruktūros paruošimui, o kita :ref:`duomenų atvėrimui
<atvėrimo-sutartis>`.

Infrastruktūros parengimo procedūroms dažnai reikalinga pilna prieiga prie
duomenų šaltinio ir administratoriaus teisės kompiuteryje ar serveryje,
kuriame bus diegiamos duomenų atvėrimo priemonės.

Tuo tarpu duomenų atvėrimo sutartis nereikalauja jokios prieigos prie duomenų
šaltinio.

Infrastruktūros paruošimo sutartis yra reikalinga tik tuo atveju, jei Teikėjas
neturi jokios duomenų šaltinio priežiūros sutarties ir negali infrastruktūros
paruošimo darbų atlikti savarankiškai.

Infrastruktūros paruošimo darbus gali atlikti ir Atvėrėjas.

Apibendrinant, Administratorius atsakingas už infrastruktūros paruošimą gali
būti:

- pats Teikėjas, jei turi reikalingas technines kompetencijas,
- esamas Administratorius atliekantis duomenų šaltinio priežiūros ir palaikymo
  paslaugas,
- Administratorius su kuriuo atskirai sudaroma sutartis tik infrastruktūros
  duomenų atvėrimui paruošimo prie priežiūros paslaugoms,
- Atvėrėjas, sudarius atskirą sutartį gali teikti Administratoriaus paslaugas.

Infrastruktūros paruošimui reikia atlikti šiuos darbus:

- Kompiuterio ar serverio, kuriame bus diegiamos duomenų atvėrimo priemonės,
  diegimas ir konfigūravimas.

- Prieigos prie duomenų šaltinio konfigūravimas.

- Priemonių reikalingų duomenų atvėrimui diegimas ir konfigūravimas.

- Nestandartinių duomenų šaltinių transformavimas į standartinius formatus.

- Šaltinio duomenų struktūros aprašo generavimas arba parengimas.

- Duomenų atvėrimo priemonių stebėsena ir palaikymas, atsiradusių trikdžių
  šalinimas.

Administratorius turėtu naudoti standartines, prižiūrinčios institucijos
prižiūrimas duomenų atvėrimo priemones.


Reikalavimai infrastruktūrai
============================

Reikalavimai infrastruktūrai priklauso nuo to, koks variantas labiausiai tinka
konkretaus Teikėjo atvejui. Toliau aptarsime kelis galimus variantus, tačiau
variantų gali būti ir daugiau.

Atskira virtuali mašina
-----------------------

Šis variantas yra rekomenduojamas.

Teikėjo infrastruktūroje reikia paleisti naują virtualią mašiną, kurioje būtų
įdiegta Linux operacinė sistema ir suteikta prieiga prie duomenų šaltinio.

Rekomenduojame naudoti Red Hat, Ubuntu arba Debian Linux distribucijas.

Jei duomenys pateikiami duomenų failuose, tuomet katalogas, kuriame yra
saugomi failai, prie virtualios mašinos prijungimas NFS_ arba SMBFS_ pagalba.
Arba galima failus periodiškai kopijuoti į virtualią mašiną rsync_ pagalba.

.. _NFS: https://en.wikipedia.org/wiki/Network_File_System
.. _SMBFS: https://en.wikipedia.org/wiki/Samba_(software)
.. _rsync: https://en.wikipedia.org/wiki/Rsync

Jei duomenų atvėrimui naudosite VDV IS duomenų jungtį, tuomet, virtualioje
mašinoje reikia panašiai tiek pat vietos, kiek užima visi atvėrimui
reikalingi duomenys, kadangi VDV IS duomenų jungtis, prieš perduodant
duomenis, pasidaro perduodamų duomenų kopiją.

Jei duomenų atvėrimui naudosite standartinę priemonę :ref:`spinta`, tuomet
duomenų perdavimui reikalinga tiek vietos, kiek užima visų atveriamų duomenų
identifikatoriai. Kiek tiksliai identifikatoriams reikės vietos labai
priklauso nuo duomenų šaltinio duomenų.


.. _šdsa-paruošimas:

ŠDSA paruošimas
===============

Administratorius, naudodamasis Prižiūrinčios institucijos patvirtintomis
priemonėmis, parengiam duomenų šaltinio struktūros aprašą (ŠDSA).

ŠDSA yra lentelė sudaryta iš 15 stulpelių, kurioje pateikiamas pilnas duomenų
šaltinyje esančių duomenų laukų sąrašas su duomenų tipais, ryšiais tarp
duomenų objektų ir aprašymais.

Tokią lentelę daugeliu atveju galima sugeneruoti automatiškai naudojant
standartines priemones, jei duomenų šaltinis palaikomas. Jei standartinės
priemonės duomenų šaltinio nepalaiko, tuomet, Administratorius parengia ŠDSA
savaranki6kai.

Tokį pradinį ŠDSA variantą Administratorius perduoda Teikėjui.

Po tam tikro laiko, kai duomenų šaltinio struktūra keičiasi, reikia
atnaujinti ir ŠDSA, tačiau išlaikant visus keitimus, kuriuos yra padaręs
Teikėjas. Atnaujinant ŠDSA reikia užtikrinti, kad duomenų struktūra,
kuri jau buvo publikuota, išliktų nepakitusi. Turi būti užtikrinamas
publikuotos duomenų struktūros stabilumas.

Tam tikra apimtimi standartinės priemonės užtikrina ŠDSA atnaujinimą, tačiau
sudėtingesniais struktūros pasikeitimo atvejais, gali tekti sugeneruoti naują
ŠDSA variantą ir lyginant su anksčiau generuoti ir taisytu variantu palyginti
ir atnaujinti rankiniu būdu.

Šaltinio duomenų struktūros aprašas gali būti generuojamas įvairiais būdais,
kelis iš jų aptarsime sekančiuose skyreliuose.

Tiesioginis generavimas
-----------------------

Tiesioginis generavimas iš duomenų šaltinio reikalauja tiesioginės prieigos
prie duomenų šaltinio. ŠDSA generavimo priemonė jungiasi prie duomenų
šaltinio, nuskaito duomenų šaltinio struktūrą ir generuoja ŠDSA.

Šiuo atveju, generavimo priemonė turi turėti pilną prieigą prie duomenų
šaltinio ir įprastiniu atveju ją turėtu leisti Administratorius, kuris yra
sudaręs infrastruktūros paruošimo sutartį su Teikėju. Generavimas
turėtu vykti Teikėjo infrastruktūroje.


Generavimas iš schemos
----------------------

Jei duomenų šaltinis tai palaiko, galima eksportuoti duomenų šaltinio schemą
ir ją perduoti Atvėrėjui, kuris iš schemos parengs ŠDSA.

Šaltinio schema gali būti pateikta SQL DDL ar kitu formatu, kurį palaiko
standartinės priemonės.

Šiuo atveju, nereikia diegti jokių papildomų priemonių, tačiau reikalinga
Rangovo pagalba eksportuojant duomenų šaltinio schema.


Rankinis paruošimas
-------------------

Tam tikrais atvejais, kai duomenų šaltinis yra labai nedidelės apimties arba
duomenų brandos lygis yra labai žemas, šaltinio duomenų struktūros aprašą
galima parengti ir rankiniu būdu, užpildant ŠDSA lentelę.


.. _šdsa-suderinimas:

ŠDSA suderinimas atvėrimui
==========================

Turinti paruoštą pradinį ŠDSA variantą, Teikėjas savarankiškai, su
Atvėrėjo pagalba parengia ŠDSA atvėrimui.

Ruošiant ŠDSA atvėrimui, nurodoma kurie duomenų laukai bus atveriami,
nurodomi filtrai, jei duomenys atveriami ne pilna apimtimi, sutvarkomi
kodiniai pavadinimai, kad atitiktų atveriamiems duomenis keliamus
reikalavimus, pateikiami trūkstami metaduomenys. Plačiau apie ŠDSA paruošimą
atvėrimui skaitykite skyriuje :ref:`detali-inventorizacija`.


.. _atvėrimo-sutartis:

Duomenų atvėrimo sutartis
=========================

Atvėrimui paruoštas ŠDSA variantas teikiamas derinimui Atvėrėjui. Atvėrėjas
patikrina ar ŠDSA paruoštas tinkamai ir informuoja Teikėją apie aptiktas
klaidas.

Pasirašant duomenų atvėrimo sutartį, suderintas ŠDSA variantas pateikiamas,
kaip sutarties priedas.


.. _adsa-publikavimas:

ADSA publikavimas
=================

Pasirašius sutartį, Teikėjas perduoda Atvėrėjui Katalogo API raktą, kad
Atvėrėjas galėtų automatiškai atnaujinti atveriamo duomenų rinkinio
metaduomenis.

Atvėrėjas ŠDSA pagrindu generuoja ADSA variantą, kuriame pašalinami visi
atveriamo duomenų šaltinio metaduomenys ir paliekama tik ta dalis, kuri skirta
publikavimui. Atvėrėjas publikuoja ADSA Kataloge per :ref:`Katalogo partnerių
API <partnerių-api>`.

Publikavus ADSA Kataloge, ADSA taip pat perduodamas ir į  atvirų duomenų
Saugyklą, ko pasekoje Saugykla paruošiama duomenų priėmimui, kurie atitinka
ADSA pateiktus metaduomenis.

Kataloge užtikrinama, kad įkeltas ADSA neturi struktūros pakeitimų, kurie
nėra suderinami su prie6 tai publikuota ADSA versija, atlieka pilną
metaduomenų patikrinimą.


Kaip pildyti ŠDSA?
******************

Duomenų struktūros aprašo rengimas susideda iš tokių žingsnių:

1. Duomenų šaltinio administratorius pateikia šaltinio :ref:`duomenų struktūros
   išklotinę (ŠDSA) <dsa>`.

2. Duomenų srities ekspertai su duomenų šaltinio administratoriaus pagalba
   pateikia trūkstamus metaduomenis duomenų struktūros aprašo lentelėje.

Jei pirminio duomenų struktūros aprašo varianto sugeneruoti iš duomenų
šaltinio neįmanoma, pavyzdžiui, jei duomenys yra labai žemo brandos lygio,
tuomet duomenų struktūros aprašas pildomas nuo nulio naudojant :download:`aprašo
lentelės šabloną </static/sablonai/dsa.xlsx>`.

Duomenų struktūros aprašas yra lentelė susidedanti iš 15 stulpelių, kuriuose
aprašoma duomenų struktūra. Tarkime, turint tokius duomenis:

====  ========  =======  ===============
ŠALIS
----------------------------------------
ID    KODAS     ŽEMYNAS  ŠALIS
====  ========  =======  ===============
1     lt        eu       Lietuva
2     lv        eu       Latvija
3     ee        eu       Estija
====  ========  =======  ===============

Duomenų struktūra aukšiau pateiktiems duomenims atrodys taip:

.. table:: Duomenų struktūros aprašas

    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    | id | d | r | b | m | property   | type    | ref   | source     | prepare        | level | access  | uri | title | description |
    +====+===+===+===+===+============+=========+=======+============+================+=======+=========+=====+=======+=============+
    |    | datasets/example/countries |         |       |            |                |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   | salys                  | sql     |       | \sqlite:// |                |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   |   |   | Country        |         | id    | ŠALIS      | continent="eu" |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   |   |   |   | id         | integer |       | ID         |                | 4     | private |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   |   |   |   | code       | string  |       | KODAS      |                | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   |   |   |   | continent  | string  |       | ŽEMYNAS    |                | 2     | private |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   |   |   |   | name       | string  |       | ŠALIS      |                | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+

.. note::

    Siekiant padidinti duomenų struktūros aprašo lentelės skaitomumą, kai
    kurie stulpelių pavadinimai yra sutrumpinti:

    | **d** - dataset - duomenų rinkinio kodinis pavadinimas.
    | **r** - resource - duomenų šaltinio kodinis pavadinimas.
    | **b** - base - modelio bazės kodinis pavadinimas.
    | **m** - model - modelio kodinis pavadinimas.

Duomenų struktūros aprašo lentelė susideda iš :ref:`5 dimensijų
<dimensijos-stulpeliai>` (dataset, resource, base, model, property) ir :ref:`9
metaduomenų stulpelių <metaduomenų-stulpeliai>`, kurių prasmė priklauso nuo
vienos iš 5 dimensijų.

.. image:: /static/dsa.png
    :align: center

Plačiau apie tai, ką reiškia kiekvienas stulpelis galite skaityti skyriuje
:ref:`dsa-lentelės-struktūra`.

:term:`ŠDSA` lentelėje reikia pateikti tokius duomenis:

.. image:: /static/dsa-pildymas.png
    :align: center

1. :ref:`Duomenų rinkiniui <dataset>` suteikti :ref:`kodinį pavadinimą
   <kodiniai-pavadinimai>`.

2. Pateikti duomenų šaltinio pavadinimą, :ref:`tipą ir adresą <resource>`.

3. Užpildyti :data:`uri` stulpelį, nurodant kuriose vietose yra :ref:`asmens
   duomenys <pii>`.

4. Užpildyti :data:`property.access`, nurodant duomenų :ref:`prieigos lygį
   <access>`.

5. Užpildyti :data:`model.prepare`, jei duomenys atveriami ne pilna apimtimi ir
   reikia juos :ref:`filtruoti <duomenų-atranka>`.

6. :data:`property.level` stulpelyje nurodyti esamą duomenų laukų :ref:`brandos
   lygį <level>`.

7. Užpildyti :data:`title` ir :data:`description` stulpelius pateikiant
   :data:`model` ir :data:`property` pavadinimus ir aprašymus.

Galiausiai, toks duomenų struktūros aprašas gali būti naudojamas
:ref:`automatizuotam duomenų atvėrimui ir publikavimui
<automatinis-atvėrimas>` arba naudojamas kaip sutarties priedas, jei įstaiga
duomenis atveria su rangovo ar Vyriausybės paskirtos įstaigos pagalba.

Jei įstaiga jau yra atvėrusi duomenis ir juos publikuoja savo infrastruktūroje,
tuomet į atvirų duomenų portalą turi būti įkeliamas, ne :term:`ADSA`, o
:term:`ŠDSA`, kuriame aprašyti įstaigos infrastruktūroje publikuojami duomenys.
