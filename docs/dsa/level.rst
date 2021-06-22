.. default-role:: literal
.. _level:

Brandos lygiai
==============

Duomenų brandos lygis nurodomas :data:`level` stulpelyje.

Duomenų brandos lygis atitinka `5 ★ Open Data`_ skalę, tačiau adaptuota duomenų
struktūros aprašo kontekstui. Papildomai įtrauktas nulinis lygis, kai duomenys
nekaupiami, tačiau yra reikalingi ir yra parengtas jų :term:`duomenų struktūros
aprašas <DSA>`.

.. _5 ★ Open Data: https://5stardata.info/


.. describe:: level

    .. describe:: 0

        **Nekaupiama**

        Duomenys nekaupiami. Duomenų rinkinys užregistruotas atvirų duomenų
        portale. Užpildyta :data:`dataset` eilutė.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-0`.

    .. describe:: 1

        **Publikuojama**

        Duomenys publikuojami bet kokia forma. Užpildyta :data:`resource`
        eilutė.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-1`.

    .. describe:: 2

        **Struktūruota**

        Duomenys kaupiami struktūruota, mašininiu būdu nuskaitoma forma, bet
        kokiu formatu. Užpildytas :data:`property.source` stulpelis.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-2`.

    .. describe:: 3

        **Standartizuota**

        Duomenys saugomi atviru, standartiniu formatu. Užpildytas
        :data:`property.type` stulpelis ir duomenys atitinka nurodytą tipą.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-3`.

    .. describe:: 4

        **Identifikuojama**

        Duomenų objektai turi aiškius, unikalius identifikatorius. Užpildyti
        :data:`model.ref` ir :data:`property.ref` stulpeliai.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-4`.

    .. describe:: 5

        **Susieta su išoriniu žodynu**

        Modeliai iš įstaigų duomenų rinkinių vardų erdvės susieti su modeliais
        iš standartų vardų erdvės, užpildytas :data:`base` eilutė. Standartų
        vardų erdvėje esantiems :term:`modeliams <modelis>` ir jų
        :term:`savybėms <savybė>` užpildytas :data:`uri` stulpelis.

        Daugiau apie vardų erdves skaitykite skyrelyje: :ref:`vardų-erdvės`.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-5`.

Daugeliu atveju brandos lygis gali būti nustatomas automatiškai pagal tai ar yra
užpildyti tam tikri stulpeliai. Automatiškai brandos lygio negalima nustatyti
tarp `2` ir `3` brandos lygio, todėl automatinės priemonės visada turėtų
parinkti žemesnį `2` brandos lygį, jei nenurodyta kitaip.

Jei žemesnėje dimensijoje nėra nurodytas joks brandos lygis, jis yra paveldimas
iš aukštesnės dimensijos.
