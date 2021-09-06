.. default-role:: literal

.. _poreikio-deklaravimas:

Duomenų naudotojams
###################

:term:`ADK` svetainėje duomenų naudotojai `gali teikti pasiūlymus`__ dėl jiems
reikalingų duomenų. Galima apytiksliai įvardinti pageidaujamo duomenų rinkinio
pavadinimą ir aprašymą, tačiau galima duomenų poreikį įvardinti labai tiksliai,
poreikio formoje įkeliant :term:`DSA` lentelę CSV formatu.

.. __: https://data.gov.lt/requests/new

Iš jau publikuojamų :term:`ADSA` lentelių, galima atsirinkti dominančius
duomenis ir susirašyti juos į savo poreikio :term:`DSA` lentelę.

Kaip pavyzdį galime panagrinėti skyrelyje :ref:`atvėrimas` naudotą :term:`ADSA`
lentelę, kuri atrodo taip:

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

Tokią lentelę galima atsisiųsti ir atsidaryti su bet kuria skaičiuoklės programa
ir ją papildyti trūkstamais metaduomenimis, kurie jums yra reikalingi.

Pavyzdžiui tokia papildyta poreikio :term:`ADSA` lentelė gali atrodyti taip:

.. table:: Pageidaujamų duomenų struktūros aprašas (:term:`ADSA`)

    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+--------+------------------------------------+-------+-------------------------------------+
    | id | d | r | b | m | property   | type    | ref   | source | prepare | level | access | uri                                | title | description                         |
    +====+===+===+===+===+============+=========+=======+========+=========+=======+========+====================================+=======+=====================================+
    |  8 |   |   |   |   |            | prefix  | esco  |        |         |       |        | \http://data.europa.eu/esco/model# |       |                                     |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+--------+------------------------------------+-------+-------------------------------------+
    |  6 | datasets/example/countries |         | 1     |        |         |       |        |                                    |       |                                     |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+--------+------------------------------------+-------+-------------------------------------+
    |  1 |   | salys                  | sql     |       |        |         |       |        |                                    |       |                                     |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+--------+------------------------------------+-------+-------------------------------------+
    |  2 |   |   |   | Country        |         | _id   |        |         |       |        |                                    |       |                                     |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+--------+------------------------------------+-------+-------------------------------------+
    |  4 |   |   |   |   | code       | string  |       |        |         | 5     | open   | esco:isoCountryCodeA2              |       |                                     |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+--------+------------------------------------+-------+-------------------------------------+
    |  5 |   |   |   |   | name       | string  |       |        |         | 2     | open   |                                    |       |                                     |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+--------+------------------------------------+-------+-------------------------------------+
    |  9 |   |   |   |   |            | comment |       |        |         |       |        |                                    |       | Kokia kalba pateiktas šalies kodas? |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+--------+------------------------------------+-------+-------------------------------------+
    |  6 |   |   |   |   | continent  | string  |       |        |         | 3     | open   |                                    |       |                                     |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+--------+------------------------------------+-------+-------------------------------------+
    |  7 |   |   |   |   | population | string  |       |        |         | 3     | open   |                                    |       |                                     |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+--------+------------------------------------+-------+-------------------------------------+

Šioje lentelėje, buvo pateikti tokie pageidavimai dėl duomenų:

- Pasiūlyta padidinti `code` savybės brandos lygį nuo 2 iki 5, pateikiant
  šios savybės sąsają su `esco:isoCountryCodeA2` išoriniu žodynu, kuriame
  įvardinta, kad šalies kodas turi atitikti ISO 3166 šalių kodų standartą.

  Papildomai buvo įtrauktas naujas URI prefiksas 8-oje eilutėje.

- Pateiktas paklausimas `name` savybei įtraukiant papildomą :data:`comment`
  dimensiją, apie tai, kokia kalba pateikti šalių pavadinimai.

- Pasiūlyta įtraukti dvi naujas `country` savybes, `continent` ir
  `population`, nurodant, kad pageidaujamas šių savybių brandos lygis turėtu
  būti ne mažesnis, nei 3.

Duomenų naudotojai turi galimybę ne tik teikti pageidavimus, bet ir prisidėti
prie atvertų duomenų brandos lygio kėlimo. Pageidavimo formoje įkelti
:term:`DSA` gali būti papildyti pakeitimais :ref:`didinančiais duomenų brandos
lygį <brandos-lygio-kėlimas>`.
