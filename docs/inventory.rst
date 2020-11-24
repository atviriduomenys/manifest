.. default-role:: literal

.. _inventory:

Inventorizacija
###############

Inventorizaciją yra procesas kurio metu parengiami metaduomenys apie duomenis,
prieš atveriant pačius duomenis. Inventorizacija atliekama tokiais etapais:

1. Sudaromas preliminarus duomenų rinkinių sąrašas.

2. Parengiamas detalus :term:`duomenų struktūros aprašas <DSA>` (DSA).

Šioje dokumentacijoje aptariamas tik antrasis, detalusis inventorizacijos
etapas.

Duomenų šaltinio inventorizacija atliekama :term:`DSA` lentelės pagalba.
Daugeliu atveju :term:`DSA` lentelę galima generuoti automatiškai iš duomenų
šaltinio.

Jei duomenys jau atverti, tada būtina parengti atvertų duomenų :term:`ADSA`
lentelė. Jei duomenys dar nėra atverti, rekomenduojama pirmiausiai parengti
pirminio duomenų šaltinio :term:`ŠDSA` lentelę, o tada :term:`ŠDSA`
transformuoti į :term:`ADSA`.

:term:`DSA` leidžia aprašyti duomenis saugomus įvairiuose duomenų šaltiniuose,
plačiau apie tai galima pasiskaityti skyriuje :ref:`sources`, tačiau kaip
pavyzdį galime panagrinėti Oracle duomenų bazės duomenų šaltinį, kuriam yra
viena lentelė:

====  ========  ===============
\oracle://localhost/salys
-------------------------------
id    kodas     salis
====  ========  ===============
1     lt        Lietuva
2     lv        Latvija
3     ee        Estija
====  ========  ===============


Pirminis ŠDSA
=============

Tai tokių duomenų :term:`ŠDSA` lentelė atrodys taip:

.. table:: Pirminis šaltinio duomenų struktūros aprašas (:term:`ŠDSA`)

    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+
    | id | d | r | b | m | property | type    | ref   | source                    | prepare | level | access | uri | title | description |
    +====+===+===+===+===+==========+=========+=======+===========================+=========+=======+========+=====+=======+=============+
    |  1 |   | salys                | sql     |       | \oracle://localhost/salys |         |       |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+
    |  2 |   |   |   | salis        |         | id    |                           |         |       |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+
    |  3 |   |   |   |   | id       | integer |       | id                        |         | 4     |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+
    |  4 |   |   |   |   | kodas    | string  |       | kodas                     |         | 2     |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+
    |  5 |   |   |   |   | salis    | string  |       | salis                     |         | 2     |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+

Tokia automatiškai generuota :term:`DSA` lentelė vadinama pirmine :term:`ŠDSA`
lentele, kadangi ji yra generuota automatiškai ir neredaguota.

Deja, automatinėmis priemonėmis galima nuspėti tik dalį metaduomenų reikšmių.
Tai kas neįveikiama automatinėms priemonėms, pildoma rankiniu būdu.

Norint užbaigti duomenų inventorizaciją būtina patikslinti šiuos dalykus:

- Užpildyti :data:`access` stulpelį, nurodant duomenų :ref:`prieigos lygį
  <access>`.

- Jei reikia, pakeisti šaltinio modelių ir savybių pavadinimus, nenorint
  atskleisti vidinio šaltinio duomenų struktūros.

- Suskirstyti metaduomenis į duomenų rinkinius, vadovaujantis preliminariu
  duomenų rinkinių sąrašu. Jei reikia, preliminarus duomenų rinkinių sąrašas
  gali būti tikslinamas. Jei duomenų rinkinys jau aprašytas :term:`ADK`, tada
  :data:`dataset.ref` stulpelyje nurodomas rinkinio numeris.


Darbinis ŠDSA
=============

Baigus inventorizaciją, darbinė :term:`ŠDSA` lentelė turėtu atrodyti taip:

.. table:: Darbinis šaltinio duomenų struktūros aprašas (:term:`ŠDSA`)

    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    | id | d | r | b | m | property   | type    | ref   | source                    | prepare | level | access  | uri | title | description |
    +====+===+===+===+===+============+=========+=======+===========================+=========+=======+=========+=====+=======+=============+
    |  6 | datasets/example/countries |         | 1     |                           |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    |  1 |   | salys                  | sql     |       | \oracle://localhost/salys |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    |  2 |   |   |   | country        |         | id    |                           |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    |  3 |   |   |   |   | id         | integer |       | id                        |         | 4     | private |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    |  4 |   |   |   |   | code       | string  |       | kodas                     |         | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    |  5 |   |   |   |   | name       | string  |       | salis                     |         | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+

Šioje lentelėje buvo atlikti tokie pataisymai:

- Atsirado nauja eilutė 6, kurioje nurodytas duomenų rinkinys,
  :data:`dataset.ref` stulpelyje nurodytas :term:`ADK` duomenų rinkinio numeris.

- Užpildytas :data:`access` stulpelis.

- Pakeisti :data:`model` ir :data:`property` pavadinimai.

- Pataisytas `id` savybės brandos lygis :data:`level` stulpelyje.


Preliminarus ADSA
=================

Galiausiai, toks publikavimui parengtas :term:`ŠDSA` gali būti konvertuojamas
į :term:`ADSA`, kuris atrodys taip:

.. table:: Planuojamų atverti duomenų struktūros aprašas (:term:`ADSA`)

    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    | id | d | r | b | m | property   | type    | ref   | source                    | prepare | level | access  | uri | title | description |
    +====+===+===+===+===+============+=========+=======+===========================+=========+=======+=========+=====+=======+=============+
    |  6 | datasets/example/countries |         | 1     |                           |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    |  1 |   | salys                  | sql     |       |                           |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    |  2 |   |   |   | country        |         | _id   |                           |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    |  4 |   |   |   |   | code       | string  |       |                           |         | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    |  5 |   |   |   |   | name       | string  |       |                           |         | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+

:term:`ADSA` lentelėje buvo padaryti tokie pakeitimai:

- Pašalinti pirminio duomenų šaltinio metaduomenys iš :data:`source` stulpelio.

- Pašalintos visos eilutės, kurio :data:`access` nėra `public` arba `open`.

- Pašalintas `country` pirminis raktas buvo pakeistas `_id` pirminiu raktu.

Jei atliekant detalią duomenų inventorizaciją preliminarus duomenų rinkinių
sąrašas nėra sudarytas, tada :term:`DSA` lentelę galima suskirstyti į duomenų
rinkinius, nenurodant :data:`dataset.ref` reikšmės, tačiau tada reikėtu
užpildyti :data:`dataset.title` ir :data:`dataset.description` stulpelius.

Paskelbus tokias :term:`DSA` lenteles :term:`ADK`, dar prieš atveriant pačius
duomenis, duomenų naudotojams suteikiama galimybė pasisakyti kokie duomenys
jiems yra labiausiai aktualūs. Plačiau apie tai skaitykite skyrelyje
:ref:`poreikio-deklaravimas`.


Galutinis ADSA
==============

Jei duomenys jau yra atverti, tada galima praleisti :term:`ŠDSA` lentelės
rengimą ir iš karto parengti :term:`ADSA` lentelę, kaip duomenų šaltinį nurodant
atvertus duomenis.

Jei :term:`ADSA` buvo konvertuotas iš :term:`ŠDSA`, tada po to, kai patys
duomenys publikuojami, reikia dar kartą atnaujinti :term:`ADSA` pateikianti
šaltinio metaduomenis, kur publikuojami atverti duomenys.

Galutinis :term:`ADSA` lenelės variantas, turėtu atrodyti taip:

.. table:: Atvertų duomenų struktūros aprašas (:term:`ADSA`)

    +----+---+---+---+---+------------+---------+-------+------------------------------------+---------+-------+---------+-----+-------+-------------+
    | id | d | r | b | m | property   | type    | ref   | source                             | prepare | level | access  | uri | title | description |
    +====+===+===+===+===+============+=========+=======+====================================+=========+=======+=========+=====+=======+=============+
    |  6 | datasets/example/countries |         | 1     |                                    |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------------------------------+---------+-------+---------+-----+-------+-------------+
    |  1 |   | salys                  | spinta  |       | \http://raw.data.gov.lt            |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------------------------------+---------+-------+---------+-----+-------+-------------+
    |  2 |   |   |   | country        |         | _id   | datasets/example/countries/country |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------------------------------+---------+-------+---------+-----+-------+-------------+
    |  4 |   |   |   |   | code       | string  |       | code                               |         | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------------------------------+---------+-------+---------+-----+-------+-------------+
    |  5 |   |   |   |   | name       | string  |       | name                               |         | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------------------------------+---------+-------+---------+-----+-------+-------------+

Atlikus duomenų inventorizaciją, sekantis darbas, inventorizuotų duomenų
:ref:`brandos-lygio-kėlimas`.