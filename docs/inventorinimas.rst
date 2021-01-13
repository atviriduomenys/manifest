.. default-role:: literal

.. _inventory:

Inventorizacija
###############

Inventorizaciją yra procesas kurio metu parengiami metaduomenys apie duomenis,
prieš atveriant pačius duomenis. Duomenų inventorizacija reikia atlikti tam, kad
geriau suprasti kokius duomenis įstaiga turi ir atrinkti kuriuos duomenis galima
atverti.

Inventorizacija atliekama tokiais etapais:

1. Sudaromas preliminarus :term:`duomenų rinkinių <duomenų rinkinys>` sąrašas.

2. Parengiamas detalus :term:`duomenų struktūros aprašas (DSA) <DSA>`.

Preliminarus :term:`duomenų rinkinių <duomenų rinkinys>` sąrašas parengiamas,
apytiksliai įvardinant duomenų rinkinių pavadinimus, pateikiant trumpą aprašymą,
priskiriant kategorijai, žymes ir pateikiant kitus metaduomenis :term:`atvirų
duomenų kataloge <ADK>`.

Detali inventorizacija yra sudėtingesnė ir reikalauja daugiau laiko ir bazinių
žinių apie `duomenų modeliavimą`__. Daugeliu atveju pirminę :term:`DSA` lentelės
variantą galima generuoti automatiškai iš duomenų šaltinio, o vėliau papildyti.

.. __: https://en.wikipedia.org/wiki/Data_modeling

Jei duomenys jau atverti, tada sudaroma atvertų duomenų :term:`ADSA` lentelė.
Jei duomenys dar nėra atverti, rekomenduojama pirmiausiai parengti pirminio
duomenų šaltinio :term:`ŠDSA` lentelę, o tada :term:`ŠDSA` transformuoti į
:term:`ADSA`.

:term:`DSA` galima aprašyti duomenis saugomus įvairiuose duomenų šaltiniuose,
plačiau apie tai galima pasiskaityti skyriuje :ref:`sources`, tačiau kaip
pavyzdį galime panagrinėti išgalvotą Oracle duomenų bazės duomenų šaltinį,
kuriame yra viena lentelė:

====  ========  ===============
\oracle://localhost/salys
-------------------------------
id    kodas     salis
====  ========  ===============
1     lt        Lietuva
2     lv        Latvija
3     ee        Estija
====  ========  ===============

.. _šdsa:

ŠDSA
====

Šaltinio duomenų struktūros aprašas (ŠDSA), tariamas kaip „šadsa“. Tai yra
:term:`DSA` variantas, neskirtas viešinimui, aprašantis vidinių duomenų bazių
ar kitų vidinių šaltinių duomenų struktūras. ŠDSA leidžia geriau suprasti
turimus duomenis, tuos duomenis suskirstyti į duomenų rinkinius ir pažymėti,
kurie duomenys gali būti atverti.


.. _pirminis-šdsa:

Pirminis
--------

Oracle, kaip ir kitos duomenų bazių valdymo sistemos jau turi pakankamai
metaduomenų, kad iš jų būtų galima automatiškai generuoti pirminį
:term:`ŠDSA` lentelės variantą, kuris šiuo atveju atrodys taip:

.. table:: Pirminis šaltinio duomenų struktūros aprašas (:term:`ŠDSA`)

    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+
    | id | d | r | b | m | property | type    | ref   | source                    | prepare | level | access | uri | title | description |
    +====+===+===+===+===+==========+=========+=======+===========================+=========+=======+========+=====+=======+=============+
    |  1 |   | salys                | sql     |       | \oracle://localhost/salys |         |       |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+
    |  2 |   |   |   | Salis        |         | id    |                           |         |       |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+
    |  3 |   |   |   |   | id       | integer |       | id                        |         | 4     |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+
    |  4 |   |   |   |   | kodas    | string  |       | kodas                     |         | 2     |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+
    |  5 |   |   |   |   | salis    | string  |       | salis                     |         | 2     |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+---------------------------+---------+-------+--------+-----+-------+-------------+

Tokia automatiškai generuota :term:`DSA` lentelė vadinama pirmine :term:`ŠDSA`
lentele, kadangi ji yra generuota automatiškai ir neredaguota.

Keičiantis pirminio duomenų šaltinio struktūrai :term:`ŠDSA` galima automatiškai
atnaujinti, net jei :term:`ŠDSA` papildomas naujais metaduomenimis.

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


.. _darbinis-šdsa:

Darbinis
--------

Baigus inventorizaciją, darbinė :term:`ŠDSA` lentelė turėtu atrodyti taip:

.. table:: Darbinis šaltinio duomenų struktūros aprašas (:term:`ŠDSA`)

    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    | id | d | r | b | m | property   | type    | ref   | source                    | prepare | level | access  | uri | title | description |
    +====+===+===+===+===+============+=========+=======+===========================+=========+=======+=========+=====+=======+=============+
    |  6 | datasets/example/countries |         | 1     |                           |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    |  1 |   | salys                  | sql     |       | \oracle://localhost/salys |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+---------------------------+---------+-------+---------+-----+-------+-------------+
    |  2 |   |   |   | Country        |         | id    |                           |         |       |         |     |       |             |
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

- Pakeisti :data:`model` ir :data:`property` kodiniai pavadinimai.


.. _adsa:

ADSA
====

Atvertų duomenų struktūros aprašas (ADSA). Tai yra :term:`DSA` variantas,
skirtas viešinimui, aprašantis planuojamų atverti arba jau atvertų duomenų
struktūras. ADSA pagrindu yra generuojamas atvertų duomenų API, o taip pat ADSA
leidžia duomenų naudotojams susipažinti atvertų duomenų struktūrą, teikti
pasiūlymus ir pastabas.


.. _preliminarus-adsa:

Preliminarus
------------

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
    |  2 |   |   |   | Country        |         | _id   |                           |         |       |         |     |       |             |
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


.. _galutinis-adsa:

Galutinis
---------

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
    |  2 |   |   |   | Country        |         | _id   | datasets/example/countries/Country |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------------------------------+---------+-------+---------+-----+-------+-------------+
    |  4 |   |   |   |   | code       | string  |       | code                               |         | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------------------------------+---------+-------+---------+-----+-------+-------------+
    |  5 |   |   |   |   | name       | string  |       | name                               |         | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------------------------------+---------+-------+---------+-----+-------+-------------+

Atlikus duomenų inventorizaciją, sekantis darbas, inventorizuotų duomenų
:ref:`brandos-lygio-kėlimas`.
