.. manifest documentation master file, created by
   sphinx-quickstart on Sun Jul  7 15:44:01 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. default-role:: literal

Atvirų duomenų manifestas
#########################

Kas yra manifestas?
===================

:term:`Manifestas` yra YAML failų rinkinys, kuriuose aprašomos duomenų struktūros.
Manifestas yra vidinis komunikacijos protokolas, skirtas susikalbėti duomenų
tiekėjams, duomenų naudotojams ir centriniam atvirų duomenų portalui.

:term:`Manifestas` turi pakankamai daug :term:`metaduomenų <metaduomenys>`
(metaduomenys yra duomenys apie duomenis) apie duomenų rinkinį jį sudarančias
duomenų struktūras. Tai leidžia automatizuoti duomenų importavimą į atvirų
duomenų portalą, duomenų kokybės patikrinimą, duomenų eksportavimą į kitus
formatus ir pan.

Pats savaime Manifestas nėra dar vienas standartas, tai yra vidinei
komunikacijai skirtas protokolas, kurio pagrindu sudaroma galimybė
tranformatuoti duomenis į įvairius formatus. Pats Manifestas yra aktualus tik
tiekėjams norintiems atverti duomenis.


Kaip tai veikia?
================

Kad geriau suprasti, kaip visa tai veikia, pabandykime aprašyti CSV failo
duomenų struktūrą. Tarkime turime tokį CSV faile, kuris pasiekiamas adresu
`https://example.com/countries.csv`, šio CSV failo turinys atrodo taip::

   code,country
   lt,Lietuva
   lv,Latvija
   ee,Estija

Šiam CSV failui Manifesto duomenų struktūros aprašas atrodytų taip:

.. code-block:: yaml

   type: dataset
   name: example/data
   resources:
     countries:
       type: csv
       objects:
         geografija/salis:
           source: https://example.com/countries.csv
           properties:
             kodas:
               type: string
               source: code
             pavadinimas:
               type: string
               source: country

Šiame duomenų apraše yra pakankamai informacijos, kad galėtume automatiškai
atlikti šiuose dalykus:

- galima automatiškai importuoti duomenis iš nurodyto šaltinio `source:
  https://example.com/countries.csv`,

- galima automatiškai patikrinti duomenis, kadangi nurodyti duomenų tipai,

- galima automatiškai patikrinti ar duomenų aprašas tikrai atitinka duomenis,
  kadangi aprašas yra susietas su duomenų šaltiniu,

- galima konvertuoti CSV failo duomenis į įvairius kitus duomenų formatus,
  kadangi turime detalų duomenų struktūros aprašą, duomenų tipus ir pan.,

- galima susieti duomenų šaltinyje naudojamą žodyną su atvirų duomenų portalo
  naudojamu žodynu, šiuo atveju atlikami tokie susiejimai::

    countries.csv -> geografija/salis
    code          -> kodas
    country       -> pavadinimas


Kas yra žodynas?
================

Duomenų kontekste, žodynas yra tiesiog pavadinimų rinkinys, kuriais vadinami
objektai ir objektų savybės. Iš mūsų `countries.csv` pavyzdžio, duomenų
šaltinis naudoja vienokius laukų pavadinimus, tačiau importuojant duomenis
nurodome kitokius pavadinimus.

Aprašant duomenų struktūras nebūtina laikytis vieningo žodyno. Jei naudojami
pavadinimai yra ne iš žodyno, tada prieš pavadinima turi būti rašomas taško
simbolis (`.`). Po taško galima naudoti lygiai tokius pačius laukų pavadinimas
arba bet kokius kitus pavadinimus. Tačiau vieningas atvirų duomenų portale
naudojamas žodynas padeda geriau suvaldyti duomenis ir didina atvertų duomenų
brandos lygį.

Tikriausiai iškyla klausimas, kas sudaro žodynus ir kaip žinoti kokie
pavadinimai yra naudojami atvirų duomenų portalo žodyne? Mūsų `countries.csv`
pavyzdyje duomenų aprašo tipas yra `dataset`, yra dar vienas duomenų aprašo
tipas pavadinimu `model`. Mūtend `model` aprašuose ir aprošomi atvirų duomenų
portalo žodyno pavadinimai. Štai pavyzdys, kaip toks aprašas atrodo:

.. code-block:: yaml

   type: model
   name: geografija/salis
   properties:
     kodas:
       type: string
     pavadinimas:
       type: string

Dažniausiai visi `model` aprašai saugomi `models/` kataloge ir failas iki YAML
failo atitinka modelio pavadinimą, tai šuo atveju šis modelis turūtų būti
išsaugotas `models/geografija/salis.yml` faile. Toks katalogas padeda langviau
naviguoti tarp modelių aprašų ir naudoti tuos pačius pavadinimus aprašant
duomenų šaltinius.


Turinys
=======

.. toctree::
   :maxdepth: 2

   sources.rst
   pk.rst
   norm.rst
   glossary.rst
