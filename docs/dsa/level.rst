.. default-role:: literal
.. _brandos-lygiai:

Brandos lygiai
==============

Duomenų brandos lygis nurodomas :data:`level` stulpelyje.

Duomenų brandos lygis atitinka `5 ★ Open Data`_ skalę, tačiau adaptuota duomenų
struktūros aprašo kontekstui. Papildomai įtrauktas nulinis lygis, kai duomenys
nekaupiami, tačiau yra reikalingi ir yra parengtas jų duomenų struktūros
aprašas.

.. _5 ★ Open Data: https://5stardata.info/


.. describe:: level

    .. describe:: 0

        **Nekaupiama**

        Duomenys nekaupiami. Duomenų rinkinys užregistruotas atvirų duomenų
        portale. Užpildyta :data:`dataset` eilutė.

    .. describe:: 1

        **Publikuojama**

        Duomenys publikuojami bet kokia forma. Užpildyta :data:`resource`
        eilutė.

    .. describe:: 2

        **Struktūruota**

        Duomenys kaupiami struktūruota, mašininiu būdu nuskaitoma forma, bet
        kokiu formatu. Užpildytas :data:`source` stulpelis.

    .. describe:: 3

        **Standartizuota**

        Duomenys saugomi atviru, standartiniu formatu. Užpildytas
        :data:`property.type` stulpelis ir duomenys atitinka nurodytą tipą.

    .. describe:: 4

        **Identifikuojama**

        Duomenų objektai turi aiškius, unikalius identifikatorius. Užpildytas
        :data:`ref` stulpelis.

    .. describe:: 4.5

        **Susieta**

        Duomenys susieti su vieningu valstybiniu žodynu. Užpildyta :data:`base`
        eilutė ir :data:`base` modelis yra iš globalios vardų erdvės.

    .. describe:: 5

        **Susieta su išoriniu žodynu**

        Duomenys susieti su išoriniais žodynais. Užpildytas :data:`uri`
        stulpelis.

Daugeliu atveju brandos lygis gali būti nustatomas automatiškai pagal tai ar yra
užpildyti tam tikri stulpeliai. Automatiškai brandos lygio negalima nustatyti
tarp `2` ir `3` brandos lygio, todėl automatinės priemonės visada turėtų
parinkti žemesnį `2` brandos lygį, jei nenurodyta kitaip.

Jei žemesnėje dimensijoje nėra nurodytas joks brandos lygis, jis yra paveldimas
iš aukštesnės dimensijos.
