.. _duomenų-tipai:

Duomenų tipai
#############

.. describe:: absent

    Žymi :term:`savybę <savybė>`, kuri buvo ištrinta ir nebenaudojama. Žiūrėti
    :ref:`struktūros-keitimas`.

.. describe:: boolean

    Loginė reikšmė.

.. describe:: integer

    Sveikas skaičius.

    Mažiausia galima reikšmė: `-2147483648`.

    Didžiausia galima reikšmė: `2147483647`.

    :data:`property.ref` stulpelyje, nurodomi :ref:`matavimo-vienetai`.

.. describe:: number

    Realusis skaičius, apvalinamas naudojant `slankiojo kablelio aritmetiką`__,
    kur sveikoji skaičiaus dalis gali būti šešių skaitmenų dydžio.

    __ https://en.wikipedia.org/wiki/IEEE_754

    :data:`property.ref` stulpelyje, nurodomi :ref:`matavimo-vienetai`.

    Sveikoji dalis atskiriama `.` simbolių.

.. describe:: string

    Simbolių eilutė. Neriboto dydžio, tačiau fiziškai simbolių eilutė turėtu
    būti ne didesnė, nei 1G.

.. describe:: text

    Žmonių kalba užrašytas tekstas, nurodant kalbą naudojant `ISO 639-1`_
    kodus. Tekstas gali būti pateiktas keliomis kalbomis. Tekste gali būti
    naudojamos TEI_ žymės.

    .. _ISO 639-1: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    .. _TEI: https://en.wikipedia.org/wiki/Text_Encoding_Initiative

.. describe:: binary

    Dvejetainiai duomenys. Bendras baitų skaičius turi būti ne didesnis nei 1G.


Data ir laikas
==============

.. describe:: datetime

    Data ir laikas atitinkantis `ISO 8601`_.

    Mažiausia galima reikšmė: `0001-01-01T00:00:00`.

    Didžiausia galima reikšmė: `9999-12-31T23:59:59.999999`.

    .. _ISO 8601: https://en.wikipedia.org/wiki/ISO_8601

    :data:`property.ref` stulpelyje, nurodomas `datos ir laiko tikslumas`__
    sekundėmis. Tikslumą galima nurodyti laiko vienetais, pavyzdžiui `Y`,
    `D`, `S`, arba `5Y`, `10D`, `30S`. Galimi vienetų variantai:

    =======  ================
    Reikšmė  Prasmė
    =======  ================
    Y        Metai
    M        Mėnesiai
    Q        Metų ketvirčiai
    W        Savaitės
    D        Dienos
    H        Valandos
    T        Minutės
    S        Sekundės
    L        Milisekundės
    U        Mikrosekundės
    N        Nanosekundžės
    =======  ================

    .. __: https://www.w3.org/TR/vocab-dcat-2/#Property:dataset_temporal_resolution

.. describe:: date

    Tas pats kas `datetime` tik dienos tikslumu.

.. describe:: temporal

    Apibrėžtis laike.

    Šis tipas atitinka `datetime`, tačiau nurodo, kad visas model yra
    apibrėžtas laike, būtent pagal šią savybę. Tik viena model savybė gali
    turėti `temporal` tipą. Pagal šios savybės reikšmes apskaičiuojamas ir
    įvertinamas `dct:temporal`_.

    .. _dct:temporal: https://www.w3.org/TR/vocab-dcat-2/#Property:dataset_temporal


Erdviniai duomenys
==================

.. describe:: geometry

    Erdviniai duomenys. Duomenys pateikiami WKT_, WKB_ arba suderinamu
    formatu, kartu nurodant ir SRID_.

    .. _WKT: https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
    .. _WKB: https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary
    .. _SRID: https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier

    :data:`property.ref` stulpelyje nurodomas `erdvinis tikslumas`__
    metrais. Tikslumą galima pateikti naudojanti SI vienetus, pavyzdžiui
    `m`, `km` arba `10m`, 100km`.

    .. __: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases

.. describe:: spatial

    Apibrėžtis erdvėje.

    Šis tipas atitinka `geometry`, tačiau nurodo, kad visas model yra
    apibrėžtas erdvėje, būtent pagal šią savybę.  Tik viena model savybė
    gali turėti `spatial` tipą. Pagal šios savybės reikšmes apskaičiuojamas ir
    įvertinamas `dct:spatial`_.

    .. _dct:spatial: https://www.w3.org/TR/vocab-dcat-2/#Property:dataset_spatial


Valiuta
=======

.. describe:: currency

    Valiuta. Saugomas valiutos kiekis, nurodant tiek sumą, tiek valiutos
    kodą naudojant `ISO 4217`_ kodus.

    .. _ISO 4217: https://en.wikipedia.org/wiki/ISO_4217


Failai
======

.. describe:: file

    Failas. Galimi failo metaduomenis:

    id
        Laukas, kuris unikaliai identifikuoja failą, šis laukas duomenų
        saugojimo metu pavirs failo identifikatoriumi, jam suteikiant unikalų
        UUID.

    name
        Failo pavadinimas.

    type
        Failo `media tipas`__.

        __ https://en.wikipedia.org/wiki/Media_type

    size
        Failo turinio dydis baitais.

    content
        Failo turinys.

    Šiuos metaduomenis galima perduoti `file()` funkcijai, kai vardinius
    argumentus. Pavyzdžiui:

    +---+---+---+---+----------------+--------+----------------+-----------------------------------------------------+--------------+
    | d | r | b | m | property       | type   | source         | prepare                                             | access       |
    +===+===+===+===+================+========+================+=====================================================+==============+
    | datasets/example               |        |                |                                                     |              |
    +---+---+---+---+----------------+--------+----------------+-----------------------------------------------------+--------------+
    |   |   |   | Country            |        |                |                                                     |              |
    +---+---+---+---+----------------+--------+----------------+-----------------------------------------------------+--------------+
    |   |   |   |   | name           | string | NAME           |                                                     | open         |
    +---+---+---+---+----------------+--------+----------------+-----------------------------------------------------+--------------+
    |   |   |   |   | flag_file_name | string | FLAG_FILE_NAME |                                                     | private      |
    +---+---+---+---+----------------+--------+----------------+-----------------------------------------------------+--------------+
    |   |   |   |   | flag_file_data | binary | FLAG_FILE_DATA |                                                     | private      |
    +---+---+---+---+----------------+--------+----------------+-----------------------------------------------------+--------------+
    |   |   |   |   | flag           | file   |                | file(name: flag_file_name, content: flag_file_data) | open         |
    +---+---+---+---+----------------+--------+----------------+-----------------------------------------------------+--------------+

    Šiame pavyzdyje, iš `flag_file_name` ir `flag_file_data` laukų padaromas
    vienas `flag` laukas, kuriame panaudojami duomenys iš dviejų laukų.
    Šiuo atveju, `flag_file_name` ir `flag_file_data` laukai tampa
    pertekliniais, todėl :data:`access` stulpelyje jie pažymėti `private`.

.. describe:: image

    Paveiksliukas. `image` tipas turi tokias pačias savybes kaip `file`
    tipas.


Išoriniai raktai
================

Taip pat žiūrėkite: :ref:`ryšiai`.

.. describe:: ref

    Ryšys su modeliu. Šis tipas naudojamas norint pažymėti, kad lauko
    reikšmė yra :data:`property.ref` stulpelyje nurodyto :data:`model.ref`
    modelio id.

.. describe:: backref

    Atgalinis ryšys su modeliu.

    Šis tipas naudojamas norint pažymėti, kad tam tikras kitas modelis turi
    `ref` tipo lauką, kuris rodo į šį modelį. Šis laukas pats duomenų
    neturi, tai tik papildomas metaduomuo, padedantis geriau suprasti ryšius
    tarp modelių.

.. describe:: generic

    Dinaminis ryšys su modeliu.

    Šis tipas naudojamas tada, kai yra poreikis perteikti dinaminį ryšį, t.
    y. duomenys siejami ne tik pagal id, bet ir pagal modelio pavadinimą.
    Tokiu būdu, vieno modelio laukas gali būti siejamas su keliais
    modeliais.

    Taip pat žiūrėkite :ref:`bendrieji-ryšiai`.


.. _sudėtiniai-tipai:

Sudėtiniai tipai
================

.. describe:: object

    Kompozicinis tipas.

    Šis tipas naudojamas apibrėžti sudėtiniams duomenims, kurie aprašyti
    naudojant kelis skirtingus tipas. Kompozicinio tipo atveju property
    stulpelyje komponuojami pavadinimai atskiriami taško simboliu.

    Sudarant duomenų modelį, rekomenduojama laikytis plokščios struktūros ir
    komponavimą įgyvendinti siejant modelius per `ref` ar `generic` tipus.

.. describe:: array

    Masyvas.

    Šis tipas naudojamas apibrėžti duomenų masyvams. Jei masyvo elementai
    turi vienodus tipus, tada elemento tipas pateikiamas property pavadinimo
    gale prirašant [] sufiksą, kuris nurodo, kad aprašomas ne pats masyvas,
    o masyvo elementas.

    Rekomenduojama vengti naudoti šį tipą, siekiant išlaikyti plokščią
    duomenų modelį. Vietoje `array` tipo rekomenduojama naudoti `backref`.
