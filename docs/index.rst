.. default-role:: literal

Atvirų duomenų manifestas
#########################

Atvirų duomenų manifestas yra visų Lietuvos duomenų metaduomenų visuma.
Metaduomenys aprašomi :term:`duomenų struktūros aprašų <DSA>` lentelių pagalba.

Lietuvos :term:`atvirų duomenų kataloge <ADK>` (ADK) taip pat saugomi visų
Lietuvos duomenų metaduomenys. Tačiau ADK metaduomenys yra suskirstyti į duomenų
rinkinius, tuo tarpu manifestas metaduomenis skirsto pagal :term:`duomenų
modelius <modelis>`, panaikinant duomenų suskirstymą į duomenų rinkinius. Visi
manifeste aprašyti duomenys tampa vienu dideliu duomenų rinkiniu.

Metaduomenys leidžia automatizuoti duomenų valdymą įdarbinant robotus, kurie
automatizuotų didelę dalį veiklų susijusių su duomenų valdymu.

.. image:: static/spinta.png

Į šio projekto apimtį įeina ne tik informacija kaip aprašyti metaduomenis, bet
teikiami įrankiai metaduomenų ir duomenų valdymui.

Duomenų atvėrimo procesas
=========================

.. image:: static/process-overview.svg
    :width: 200%


Inventorizacija
---------------

Manifesto sudarymo procesas vadinamas duomenų :ref:`inventorizacija
<inventory>`. Kiekviena įstaiga atliekanti savo kaupiamų duomenų inventorizaciją
aprašo turimų duomenų metaduomenis :term:`DSA` lentelėse. Tarkime, kaip pavyzdį,
galime panagrinėti išgalvotos įstaigos „Duomenų centras“ sutrumpintai vadinamos
DC duomenis. DC duomenų bazėje yra lentelė techniniu pavadinimu `COUNTRIES`,
lentelės turinys atrodo taip:

=======  ========  ===========
COUNTRIES
------------------------------
ID       CODE      COUNTRY
=======  ========  ===========
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ===========

Įstaiga „Duomenų centras“ nori atverti duomenis. Pirmas žingsnis būtų duomenų
inventorizacija. Pirmas inventorizacijos žingsnis yra preliminaraus duomenų
rinkinių sąrašo sudarymas. Tačiau norint atlikti pilną inventorizaciją reikia
:term:`DSA` lentelėje aprašyti ir duomenų struktūras. Duomenų inventorizacijos
metu sudaromi įstaigoje esančių :term:`duomenų modelių <modelis>` ir jų
:term:`savybių <savybė>` sąrašas, kuris :term:`DSA` lentelėje atrodo taip:

+----+---+---+---+---+-----------+---------+------+-----------+-------+
| id | d | r | b | m | property  | type    | ref  | source    | level |
+====+===+===+===+===+===========+=========+======+===========+=======+
|  1 | datasets/gov/dc/countries |         |      |           |       |
+----+---+---+---+---+-----------+---------+------+-----------+-------+
|  2 |   | db                    | sql     |      |           |       |
+----+---+---+---+---+-----------+---------+------+-----------+-------+
|  3 |   |   |   | countries     |         | id   | COUNTRIES |       |
+----+---+---+---+---+-----------+---------+------+-----------+-------+
|  4 |   |   |   |   | id        | integer |      | ID        | 4     |
+----+---+---+---+---+-----------+---------+------+-----------+-------+
|  5 |   |   |   |   | code      | string  |      | CODE      | 2     |
+----+---+---+---+---+-----------+---------+------+-----------+-------+
|  6 |   |   |   |   | name      | string  |      | COUNTRY   | 2     |
+----+---+---+---+---+-----------+---------+------+-----------+-------+

Tokią pirminę inventorizacijos lentelę daugeliu atveju galima generuoti
automatiškai iš duomenų šaltinio.

Deja ne viską galima automatizuoti, toliau prasideda rankinis darbas su
lentele:

- :data:`access` stulpelyje surašomas duomenų prieinamumas,

- :data:`level` stulpelyje tikslinamas duomenų brandos lygis,

- :data:`ref` stulpelyje įvardinami :term:`objektų <objektas>` identifikatoriai,

- esant poreikiui, keičiami :data:`model` ir :data:`property` pavadinimai.

Galiausiai užbaigus inventorizaciją, gausime tokią :term:`ŠDSA` lentelę:

+----+---+---+---+---+-----------+---------+------+-----------+-------+---------+
| id | d | r | b | m | property  | type    | ref  | source    | level | access  |
+====+===+===+===+===+===========+=========+======+===========+=======+=========+
|  1 | datasets/gov/dc/countries |         |      |           |       |         |
+----+---+---+---+---+-----------+---------+------+-----------+-------+---------+
|  2 |   | db                    | sql     |      |           |       |         |
+----+---+---+---+---+-----------+---------+------+-----------+-------+---------+
|  3 |   |   |   | countries     |         | id   | COUNTRIES |       |         |
+----+---+---+---+---+-----------+---------+------+-----------+-------+---------+
|  4 |   |   |   |   | id        | integer |      | ID        | 4     | private |
+----+---+---+---+---+-----------+---------+------+-----------+-------+---------+
|  5 |   |   |   |   | code      | string  |      | CODE      | 3     | open    |
+----+---+---+---+---+-----------+---------+------+-----------+-------+---------+
|  6 |   |   |   |   | name      | string  |      | COUNTRY   | 3     | open    |
+----+---+---+---+---+-----------+---------+------+-----------+-------+---------+

Baigus inventorizacija, :term:`ŠDSA` lentelė konvertuojama į :term:`ADSA`
lentelę. :term:`ADSA` lentelė publikuojama :term:`ADK` duomenų naudotojų
susipažinimui, dar neatvėrus duomenų.


Brandos lygio kėlimas
---------------------

Duomenų naudotojai :term:`ADK` svetainėje gali :ref:`pasisakyti
<poreikio-deklaravimas>` kokie duomenys jiems labiausiai aktualūs, taip
formuodami duomenų atvėrimo ir brandos lygio kėlimo prioritetus.

Bendradarbiaujant ir atsižvelgiant į duomenų naudotojų atsiliepimus, tęsiamas
darbas su :term:`ŠDSA` lentele, :ref:`keliant duomenų brandos lygį
<brandos-lygio-kėlimas>`. Baigus duomenų brandos lygio kėlimo darbus gauname dar
pilnesnę ir išsamesnę :term:`ŠDSA` lentelę, kuri atrodo taip:

+----+---+---+---+---+-----------+---------+------+-----------+------+---------+------------------------------------+--------------+-----------------+
| id | d | r | b | m | property  | type    | ref  | source    |level | access  | uri                                | title        | description     |
+====+===+===+===+===+===========+=========+======+===========+======+=========+====================================+==============+=================+
|  8 |   |   |   |   |           | prefix  | esco |           |      |         | \http://data.europa.eu/esco/model# |              |                 |
+----+---+---+---+---+-----------+---------+------+-----------+------+---------+------------------------------------+--------------+-----------------+
|  9 |   |   |   |   |           | prefix  | og   |           |      |         | \http://ogp.me/ns#                 |              |                 |
+----+---+---+---+---+-----------+---------+------+-----------+------+---------+------------------------------------+--------------+-----------------+
|  1 | datasets/gov/dc/countries |         | 1    |           |      |         |                                    |              |                 |
+----+---+---+---+---+-----------+---------+------+-----------+------+---------+------------------------------------+--------------+-----------------+
|  2 |   | db                    | sql     |      |           |      |         |                                    |              |                 |
+----+---+---+---+---+-----------+---------+------+-----------+------+---------+------------------------------------+--------------+-----------------+
|  7 |   |   | /esco/country     |         | code |           |      |         |                                    |              |                 |
+----+---+---+---+---+-----------+---------+------+-----------+------+---------+------------------------------------+--------------+-----------------+
|  3 |   |   |   | countries     |         | id   | COUNTRIES |      |         | esco:Country                       | Šalis        |                 |
+----+---+---+---+---+-----------+---------+------+-----------+------+---------+------------------------------------+--------------+-----------------+
|  4 |   |   |   |   | id        | integer |      | ID        | 4    | private |                                    |              |                 |
+----+---+---+---+---+-----------+---------+------+-----------+------+---------+------------------------------------+--------------+-----------------+
|  5 |   |   |   |   | code_a2   | string  |      | CODE      | 3    | open    | esco:isoCountryCodeA2              | Šalies kodas | Dviejų simbolių |
|    |   |   |   |   |           |         |      |           |      |         |                                    |              | šalies kodas    |
+----+---+---+---+---+-----------+---------+------+-----------+------+---------+------------------------------------+--------------+-----------------+
|  6 |   |   |   |   | name      | string  |      | COUNTRY   | 3    | open    | og:country-name                    | Pavadiniams  |                 |
+----+---+---+---+---+-----------+---------+------+-----------+------+---------+------------------------------------+--------------+-----------------+

Atnaujinus :term:`ŠDSA` lentelę, atnaujinama ir :term:`ADSA` lentelė, kuri
yra viešai publikuojama :term:`ADK` svetainėje. Kadangi :term:`ŠDSA` lentelė
gali turėti konfidencialios informacijos, ji nėra viešinama.

Galiausiai, baigus metaduomenų paruošimo darbus, atveriami duomenys naudojant
automatizuotas duomenų atvėrimo priemones, veikiančias :term:`DSA` lentelių
pagrindu. Atvėrus duomenis, dar kartą atnaujinama :term:`ADSA` lentelė papildant
ją informacija apie šaltinį, kuriame publikuojami atverti duomenys, o taip pat
atnaujinami ir :term:`ADK` metaduomenys.

Praktiškai visos duomenų atvėrimo veiklos yra automatizuojamos, išskyrus
:term:`DSA` lentelių rengimą, priemonių diegimą ir konfigūravimą.


Duomenų naudojimas
==================

Baigus duomenų atvėrimo darbus, didelė dalis duomenų bus importuojami į vieną
centralizuotą duomenų saugyklą, kurioje duomenys bus teikiam įvairiais
formatais, per lankstų API. API suteikia galimybę ne tik gauti duomenis
įvairiais formatais, bet juos filtruoti, apjungti ir atlikti kitas operacijas
su duomenimis.

Kartu su duomenimis teikiama ir duomenų schemos dokumentacija, generuojama iš
:term:`DSA` lentelių :data:`title` ir :data:`description` stulpeliuose pateiktos
informacijos.

Duomenis galima naudoti tiesiogiai per API, atsisiųsti visus duomenis vienu
kartu ar susikurti savo duomenų saugyklos veidrodį, nuolat sinchronizuojant
visus pasikeitimus iš centrinės duomenų saugyklos.

Kad būtų lengviau suprasti, kaip naudoti duomenis, pateikiamos pavyzdinės
užklausos.


Turinys
=======

.. toctree::
   :maxdepth: 2

   inventory
   demand
   maturity
   sources
   norm
   params
   vocabulary
   formulas
   api
   spec
   glossary
   contributing
