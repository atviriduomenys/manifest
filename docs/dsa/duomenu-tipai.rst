.. default-role:: literal

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

.. describe:: binary

    Dvejetainiai duomenys. Bendras baitų skaičius turi būti ne didesnis nei 1G.


.. _text-types:

Tekstiniai duomenys
===================

Tekstiniai duomenys skirstomi į du skirtingus tipus `string` ir `text`.


.. describe:: string

    Simbolių eilutė. Neriboto dydžio, tačiau fiziškai simbolių eilutė turėtu
    būti ne didesnė, nei 1G.

    Simboliu eilutė turėtu būti pateikta UTF-8 koduote.

    Šiuo tipu žymimi duomenų laukai, kuriuose tekstas pateiktas ne žmonių
    kalba. Tai gali būti įvairūs kategoriniai duomenys, identifikatoriai ar
    kito pobūdžio simbolių eilutės, kurios nėra užrašytos natūraliąja žmonių
    kalba.


.. describe:: text

    Natūraliaja žmonių kalba užrašytas tekstas.

    Galima nurodyti kokia kalba užrašytas tekstas naudojant `ISO 639-1`_ kodus.
    Kalbos kodas nurodomas :data:`property` stulpelyje, prie pavadinimo įrašant
    `@<kodas>`, kur `<kodas>` yra pakeičiamas į dviejų raidžių kalbos kodą.
    Pavyzdžiui `pavadinimas@lt`.

    .. _ISO 639-1: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

    Tekstas turėtu būti pateikta UTF-8 koduote. Jei šaltinyje tekstas nėra
    UTF-8 koduotės, tuomet galima :data:`prepare` stulepyje įrašoų formulių
    pagalba galima nurodyti transformavimo taisykles iš šatinio naudojamos į
    UTF-8 koduotę.


    :data:`property.ref` galima pateikti teksto formatą, nadojant vieną iš šių
    formatų:

    - `html` - tekstas pateiktas HTML_ formatu.
    - `md` - tekstas pateiktas Markdown_ formatu.
    - `rest` - tekstas pateitkas reStructuredText_ formatu.
    - `tei` - tekstas pateiktas TEI_ formatu.

    .. _HTML: https://en.wikipedia.org/wiki/HTML
    .. _Markdown: https://spec.commonmark.org/
    .. _reStructuredText: https://docutils.sourceforge.io/rst.html
    .. _TEI: https://en.wikipedia.org/wiki/Text_Encoding_Initiative


.. _temporal-types:

Data ir laikas
==============

.. describe:: datetime

    Data ir laikas atitinkantis `ISO 8601`_.

    Mažiausia galima reikšmė: `0001-01-01T00:00:00`.

    Didžiausia galima reikšmė: `9999-12-31T23:59:59.999999`.

    .. _ISO 8601: https://en.wikipedia.org/wiki/ISO_8601

    Pagal `ISO 8601`_ standartą, data gali būti pateikta tokia forma::

        YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]

    Simbolis `*` reiškia, kad galima pateikti bet kokį vieną simbolį,
    dažniausiai naudojamas tarpo simbolis, arba raidė `T`.

    :data:`property.ref` stulpelyje, nurodomas `datos ir laiko tikslumas`__
    sekundėmis. Tikslumą galima nurodyti laiko vienetais, pavyzdžiui `Y`,
    `D`, `S`, arba `5Y`, `10D`, `30S`. Visi duomenys turi atitikti vienodą
    tikslumą, tikslumas negali varijuoti. Galimi vienetų variantai:

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

    Tas pats kas `datetime` tik dienos tikslumu. Šio tipo reikšmės taip pat
    turi atitikti `ISO 8601`_:

        YYYY-MM-DD

    Jei norima nurodyti datą žemesnio nei dienos tikslumo, tada vietoj mėnesio
    ir dienos galima naudoti `01` ir :data:`property.ref` stulpelyje nurodyti
    tikslumą, taip, kaip aprašyta prie :data:`datetime`.

.. describe:: temporal

    Apibrėžtis laike.

    Šis tipas atitinka `datetime`, tačiau nurodo, kad visas model yra
    apibrėžtas laike, būtent pagal šią savybę. Tik viena model savybė gali
    turėti `temporal` tipą. Pagal šios savybės reikšmes apskaičiuojamas ir
    įvertinamas `dct:temporal`_.

    .. _dct:temporal: https://www.w3.org/TR/vocab-dcat-2/#Property:dataset_temporal


.. _spatial-types:

Erdviniai duomenys
==================

.. describe:: geometry

    Erdviniai duomenys. Duomenys pateikiami WKT_ formatu.

    .. _WKT: https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
    .. _WKB: https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary

    :data:`property.ref` stulpelyje nurodomas tikslumas metrais. Tikslumą
    galima pateikti naudojanti SI vienetus, pavyzdžiui `m`, `km` arba `10m`,
    100km`.

    `geometry` tipas gali turėti du argumentus: geometrijos tipą ir projekciją.

    Jei geometrijos tipas nenurodytas, tada duomenys gali būti bet kokio
    geometrinio tipo. Jei tipas nurodytas, tada visi duomenys turi būti tik
    tokio tipo, koks nurodytas.

    Galimi tokie geometrijos tipai:

    - `point` - taškas.
    - `linestring` - linija.
    - `polygon` - daugiakampis.
    - `multipoint` - keli taškai.
    - `multilinestring` - kelios linijos.
    - `multipolygon` - keli daugiakampiai.

    Kiekvienas iš šių tipų gali turėti tokius dimensijų sufiksus:

    - `z` - aukštis.
    - `m` - pasirinktas matmuo (pavyzdžiui laikas, atstumas, storis ir pan.)
    - `zm` - aukštis ir pasirinktas matmuo.

    Antrasis projekcijos argumentas nurodomas pateikiant SRID_ numerį. Visi
    duomenys turi atitikti nurodytą projekciją. Jei projekcija nenurodyta,
    tuomet pagal nutylėjimą bus naudojamas `4326 (WGS84)`_ projekcija.

    Jei duomenų projekcija yra nežinoma, tuomet duomenų brandos lygis turi
    būti 2. Jei duomenų projekcija skirtingiems objektams yra skirtinga, tada
    brandos lygis turi būti 1.

    Pilną SRID_ kodų sąrašą galite rasti `epsg.io`_ svetainėje. Keletas
    dažniau naudojamų SRID_ kodų:

    - `4326 (WGS84)`_ - Pasaulinė geodezinė sistema, priimta 1984 m., naudojama
      GPS imtuvuose.

    - `3346 (LKS94)`_ - Lietuvos koordinačių sistema, priimta 1994 m.

    Geometrinio tipo naudojimo pavyzdžiai:

    - `geometry` - WGS84 projekcijos, bet kokio  tipo geometriniai objektai.
    - `geometry(3346)` - LKS94 projekcijos, bet kokio tipo geometriniai
      objektai.
    - `geometry(point)` - GWS84 projekcijos, bet `point` tipo geometriniai
      objektai.
    - `geometry(linestringm, 3345)` - LKS94 projekcijos, `linestringm` tipo
      geometriniai objektai su pasirinktu matmeniu, kaip trečia dimensija.

    .. _SRID: https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier
    .. _epsg.io: https://epsg.io/
    .. _4326 (WGS84): https://epsg.io/4326
    .. _3346 (LKS94): https://epsg.io/3346

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

    Šis duomenų tipas yra sudėtinis, susidedantis iš tokių duomenų:

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

    ==  ==  ==  ==  ==============  ======  ==============  =======  =======
    d   r   b   m   property        type    source          prepare  access
    ==  ==  ==  ==  ==============  ======  ==============  =======  =======
    datasets/example
    ------------------------------  ------  --------------  -------  -------
    \           Country
    --  --  --  ------------------  ------  --------------  -------  -------
    \               name            string  NAME                     open
    \               flag_file_name  string  FLAG_FILE_NAME           private
    \               flag_file_data  binary  FLAG_FILE_DATA           private
    \               flag            file                    |file|   open
    ==  ==  ==  ==  ==============  ======  ==============  =======  =======

    .. |file| replace:: file(name: flag_file_name, content: flag_file_data)

    Šiame pavyzdyje, iš `flag_file_name` ir `flag_file_data` laukų padaromas
    vienas `flag` laukas, kuriame panaudojami duomenys iš dviejų laukų.
    Šiuo atveju, `flag_file_name` ir `flag_file_data` laukai tampa
    pertekliniais, todėl :data:`access` stulpelyje jie pažymėti `private`.

.. describe:: image

    Paveiksliukas. `image` tipas turi tokias pačias savybes kaip `file`
    tipas.


.. _ref-types:

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

    Taip pat žiūrėkite :ref:`atgalinis-ryšys`.

.. describe:: generic

    Dinaminis ryšys su modeliu.

    Šis tipas naudojamas tada, kai yra poreikis perteikti dinaminį ryšį, t.
    y. duomenys siejami ne tik pagal id, bet ir pagal modelio pavadinimą.
    Tokiu būdu, vieno modelio laukas gali būti siejamas su keliais
    modeliais.

    Taip pat žiūrėkite :ref:`polimorfinis-ryšys`.

    Šis duomenų tipas yra sudėtinis, susidedantis iš tokių duomenų:

    object_model
        Pilnas modelio pavadinimas, su kuriuo yra siejamas objektas.

    object_id
        `object_model` modelio objekto id.


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
