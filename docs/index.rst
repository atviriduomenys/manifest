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

   name: pavyzdziai/salys
   type: dataset
   resources:
     countries:
       type: csv
       objects:
         geografija/salis:
           source: https://example.com/countries.csv
           properties:
             id:
               type: pk
               source: code
             kodas:
               type: string
               source: code
             pavadinimas:
               type: string
               source: country

Šio duomenų aprašo dėka galima automatiškai importuoti duomenis iš įvairių
:ref:`šaltinių <sources>` vėliau juos eksportuoti įvairiais formatais.

========  =======  ===========
id        kodas    pavadinimas
========  =======  ===========
552c4c24  lt       Lietuva
b5dcb868  lv       Latvija
68de1c04  ee       Estija
========  =======  ===========


Funkcijos
=========

Toks duomenų struktūros aprašas turi pakankamai informacijos, kad galėtume
automatiškai atlikti dalykus išvardintus žemiau.

- Importuoti duomenis iš įvairių :ref:`šaltinių <sources>`.

- Patikrinti šaltinio duomenų kokybę.

- Patikrinti ar duomenų aprašas tikrai atitinka duomenų šaltinį.

- Eksportuoti duomenis įvairiais kitais formatais.

- Susieti įvairių šaltinių duomenis naudojant vieningą :ref:`žodyną <vocab>`.

- Valdyti duomenis naudojant :ref:`API <api>`.

- :ref:`Normalizuoti <norm>` denormalzuotas duomenų struktūras.


Turinys
=======

.. toctree::
   :maxdepth: 2

   sources.rst
   pk.rst
   norm.rst
   dependencies.rst
   vocabulary.rst
   api.rst
   glossary.rst
