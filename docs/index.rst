.. default-role:: literal

Duomenų atvėrimo vadovas
########################

Šis išsamus duomenų atvėrimo vadovas skirtas tiek įstaigoms, įmonėms ar
rangovams atveriantiems duomenis, tiek duomenų naudotojams, naudojantiems
atvertus duomenis.

Pateikta informacija skirta duomenų specialistams vykdantiems duomenų
atvėrimo darbus ar naudojantiems duomenis.


.. image:: static/spinta.png


Dokumentacija sudaryta iš šių esminių dalių:

- Informacija duomenų tiekėjams apie tai, kaip atlikti turimų duomenų
  :ref:`inventorizaciją <inventory>` ir inventorizuotų duomenų :ref:`brandos
  lygio kėlimą <brandos-lygio-kėlimas>`.

- Informacija duomenų naudotojams, apie tai, kaip :ref:`teikti pageidavimus
  ir pastabas <poreikio-deklaravimas>` dėl duomenų ir kaip :ref:`gauti pačius
  duomenis <api>`.

- :ref:`Duomenų struktūros aprašo specifikacija <dsa>`, kurioje rasite detalią
  informaciją apie tai kaip rašyti ir skaityti :term:`DSA` lenteles.

- Informacija diegėjams apie tai, kaip diegti ir konfigūruoti :ref:`priemones
  <priemonės>` skirtas darbui su duomenimis ir :term:`DSA` lentelėmis.

.. warning::

    Atkreipkite dėmesį, kad šis vadovas yra aktyvaus vystymo stadijoje. Tačiau
    pats :ref:`DSA <dsa>` lentelės formatas yra stabilus ir didesnių lentelės
    formato pakeitimų daryti nenumatoma, todėl duomenų struktūras galima
    aprašinėti jau dabar, o įrankiai ir dokumentacija bus pilnai parengti iki
    antrojo lietuvos duomenų atvėrimo etapo pabaigos, 2023 metais.


.. toctree::
    :caption: Vadovas
    :maxdepth: 2

    ivadas
    inventorinimas
    poreikio-deklaravimas
    brandos-lygio-kelimas/index
    asmens-duomenys
    duomenu-saltiniai

.. toctree::
    :caption: Žinynas
    :maxdepth: 3

    dsa/index
    api/index
    priemones/index
    priemones/katalogas/index
    savokos

- :ref:`Rodyklė <genindex>`
