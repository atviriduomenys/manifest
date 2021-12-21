.. default-role:: literal
.. _dimensijos:

Dimensijos
==========

:term:`Dimensijos <dimensija>` apibrėžia duomenų metaduomenų detalumo lygį.
Stulpeliai :data:`dataset`, :data:`resource`, :data:`base`, :data:`model` ir
:data:`property` yra naudojami kaip :term:`DSA` dimensijos. :data:`dataset` yra
aukščiausia dimensija, :data:`property` žemiausia. :data:`dataset` ir
:data:`resource` dimensijos atitinka DCAT_ žodyną ir užtikrina trečia duomenų
brandos lygį, o žemiau esantys :data:`base`, :data:`model` ir :data:`property`
atitinka RDFS_ žodyną ir užtikrina penktą duomenų brandos lygį. Vienoje lentelės
eilutėje gali būti užpildytas ne daugiau kaip vienas dimensijos stulpelis.
Užpildytasis dimensijos stulpelis nustato visų kitų stulpelių prasmę.

.. _DCAT: https://www.w3.org/TR/vocab-dcat-2/
.. _RDFS: https://www.w3.org/TR/rdf-schema/

+----+-----+-----+-----+-----+----------+------------------------------+
| id | d   | r   | b   | m   | property | title                        |
+====+=====+=====+=====+=====+==========+==============================+
|  1 | datasets/gov/ivpk/adk            | Atvirų duomenų katalogas     |
+----+-----+-----+-----+-----+----------+------------------------------+
|  2 |     | adk                        | Atvirų duomenų katalogo      |
|    |     |                            | duomenų bazė                 |
+----+-----+-----+-----+-----+----------+------------------------------+
|  3 |     |     | /dcat/dataset        | Duomenų rinkinys             |
+----+-----+-----+-----+-----+----------+------------------------------+
|  4 |     |     |     | dataset        | Duomenų rinkinys             |
+----+-----+-----+-----+-----+----------+------------------------------+
|  5 |     |     |     |     | title    | Duomenų rinkinio pavadinimas |
+----+-----+-----+-----+-----+----------+------------------------------+

Pavyzdyje aukščiau, taupant vietą, dalies dimensijų pavadinimai sutrumpinti iki
vienos raidės ir įtraukti ne visi stulpeliai, o tik :data:`id` ir :data:`title`
metaduomenų stulpeliai. Pavyzdyje matome, kad vienoje eilutėje užpildytas tik
vienas dimensijos stulpelis, o :data:`title` stulpelio prasmė keičiasi
priklausomai nuo dimensijos reikšmės. Toliau specifikacijoje konkrečios
dimensijos stulpeliai įvardijami pateikiant tiek dimensijos, tiek metaduomens
stulpelio pavadinimus, kad būtų aiškiau apie kurios dimensijos metaduomenį
kalbama, pavyzdžiui :data:`model.title` leidžia suprasti kad kalbama apie
„Duomenų rinkinys“ reikšmę 4-oje eilutėje.

Be minėtų dimensijų stulpelių :term:`DSA` lentelėje gali būti naudojami
papildomos metaduomenų dimensijos, kai nurodoma :data:`type` reikšmė ir
nepateikiama nei viena dimensijos stulpelio reikšmė. Pavyzdžiui:

+----+---+---+---+---+----------+--------+------+-----------------------------+
| id | d | r | b | m | property | type   | ref  | uri                         |
+====+===+===+===+===+==========+========+======+=============================+
|  1 |   |   |   |   |          | prefix | dcat | \http://www.w3.org/ns/dcat# |
+----+---+---+---+---+----------+--------+------+-----------------------------+

Šiuo atveju :data:`prefix` tampa dar viena dimensija, leidžianti pateikti
metaduomenis apie naudojamų URI prefiksus. Analogiškai, kaip ir su kitomis
dimensijomis, dimensijos ir metaduomens pavadinimus galima apjungti, pavyzdžiui
:data:`prefix.ref` apibūdina tik :data:`prefix` dimensijai priklausančius
:data:`ref` stulpelius.

Dimensijos leidžia suskirstyti metaduomenis į hierarchinę struktūrą. Todėl
:term:`DSA` lentelės eilučių eiliškumas yra svarbus, kadangi žemiau esančios
eilutės priklauso aukščiau esančiai dimensijai. Tas pats galioja ir pagalbinėms
:term:`dimensijoms <dimensija>`.

Nors lentelėje sudaro tik 15 stulpelių, tačiau pasitelkiant 5 pagrindinius
dimensijas ir keletą papildomų dimensijų, atsiranda galimybė išsamiai aprašyti
visą duomenų šaltinio struktūrą.


.. _dataset:

Duomenų rinkinys
----------------

:term:`DSA` lentelėje :term:`duomenų rinkinys` nurodomas tam, kad būtų
išlaikomas ryšys tarp :term:`DSA` ir :term:`ADK`. Atliekant duomenų
inventorizaciją, automatiškai generuota :term:`DSA` lentelė turi būti
suskirstoma į :term:`duomenų rinkinius <duomenų rinkinys>`. Tada priemonių
pagalba automatiškai sukuriami pirminiai :term:`ADK` metaduomenys apie
:term:`duomenų rinkinius <duomenų rinkinys>`, kuriuos vėliau reikia papildyti
rankiniu būdu prisijungus prie ADK. Automatizuota priemonė sukūrus duomenų
rinkinių įrašus :term:`ADK`, papildys :term:`DSA` lentelę, į :data:`dataset.ref`
įrašant :term:`ADK` sukurto duomenų rinkinio identifikatorių. Tokiu būdu,
sekantį kartą vykdant sinchronizaciją, jei :data:`dataset.ref` yra užpildytas,
bus atnaujinami jau sukurti :term:`ADK` :term:`duomenų rinkinių <duomenų
rinkinys>` įrašai.

Į :term:`ADK` turi būti publikuojami tik tie duomenų rinkiniai iš DSA, kurių
:data:`dataset.access` reikšmė yra `public` arba `open`.

.. data:: dataset.source

    Jei nenurodyta, naudoti \https://data.gov.lt/ adresą.

.. data:: dataset.prepare

    Nenaudojama.

.. data:: dataset.type

    Jei nenurodyta, naudoti `ivpk` reikšmę. type nurodo :term:`API`
    formatą, kuriuo automatiškai pildomi duomenų rinkinių metaduomenys atvirų
    duomenų portale.

    Galimos reikšmės:

    .. describe:: ckan

        CKAN_ duomenų katalogas.

    .. describe:: ivpk

        `data.gov.lt`_ duomenų katalogas.

.. _CKAN: https://ckan.org/
.. _data.gov.lt: https://data.gov.lt/

.. data:: dataset.ref

    :term:`Duomenų rinkinio <duomenų rinkinys>` duomenų kataloge
    identifikatorius.

.. data:: dataset.level

    Viso duomenų rinkinio :ref:`level`. Paveldimas.

.. data:: dataset.access

    Viso duomenų rinkinio :ref:`access`. Paveldimas.

.. data:: dataset.title

    Duomenų rinkinio pavadinimas.

.. data:: dataset.description

    Duomenų rinkinio aprašymas.

Skaidymas į :term:`duomenų rinkinius <duomenų rinkinys>` turi būti atliekamas
tokiu principu, kad visi tarpusavyje susiję :term:`modeliai <modelis>` patektų į
vieną :term:`duomenų rinkinį <duomenų rinkinys>`. Teoriškai, absoliučiai visi
:term:`modeliai <modelis>` gali būti susiję tarpusavyje, skaidymą reikėtų daryti
pagal tematinį :term:`modelių <modelis>` tarpusavio ryšį, o ne pagal reliacinius
ryšius.

Jei duomenys yra išskaidyti pagal laiką, vietove ar kitus kriterijus į
skirtingus duomenų šaltinius, tokie duomenys turėtų būti apjungti į vieną modelį
:ref:`base` pagalba ir turėtų priklausyti vienam :term:`duomenų rinkiniui
<duomenų rinkinys>`. Tą pačią semantinę prasmę turintys duomenys neturėtų būti
išskaidyti keliuose :term:`duomenų rinkiniuose <duomenų rinkinys>`.


.. _duomenų-šaltinis:

Duomenų šaltinis
----------------

:term:`ŠDSA` atveju :term:`duomenų šaltinis` bus vidinis duomenų bazių serveris,
kažkoks vidinis katalogas kuriame yra lentelių failai ar koks nors vidinis API.

:term:`ADSA` atveju, :term:`duomenų šaltinis` gali būti nenurodytas, tai
reiškia, kad duomenų rinkinio duomenys dar nėra publikuoti. Jei duomenys jau yra
publikuoti, tada :term:`ADSA` :term:`duomenų šaltinis` turi rodyti į publikuotus
atvertus duomenis, tai gali būti nuorodos į CSV failus, į viešą JSON API ir pan.

:term:`Duomenų šaltinio <duomenų šaltinis>` įrašas taip pat naudojamas tam, kad
automatiškai atnaujinti :term:`ADK` esančius :term:`duomenų rinkinius <duomenų
rinkinys>`, patelkiant konkrečias nuorodas į konkrečius duomenų failus.
Analogiškai kaip ir :ref:`dataset` atveju, :data:`resource.ref` stulpelyje
nurodomas duomenų šaltinio identifikatorius iš :term:`ADK`.

.. data:: resource.type

    Duomenų šaltinio tipas. Galimos reikšmės:

    .. describe:: sql

        Reliacinės duomenų bazės

    .. describe:: csv

        CSV lentelės

    .. describe:: tsv

        TSV lentelės

    .. describe:: json

        JSON resursai

    .. describe:: jsonl

        JSON lines resursai

    .. describe:: geojson

        GeoJSON failai

    .. describe:: xml

        XML resursai

    .. describe:: html

        HTML puslapiai

    .. describe:: xlsx

        Excel lentelės (naujasis OOXML_ formatas)

        .. _OOXML: https://en.wikipedia.org/wiki/Office_Open_XML

    .. describe:: xls

        Excel lentelės (senasis formatas)

    .. describe:: ods

        ODT_ skaičiuoklės formatas

        .. _ODT: https://en.wikipedia.org/wiki/OpenDocument

    .. describe:: zip

        ZIP_ failų archyvas.

        .. _ZIP: https://en.wikipedia.org/wiki/ZIP_(file_format)

.. data:: resource.source

    Priklauso nuo :data:`resource.source`. Žiūrėti :ref:`resource`.

.. data:: resource.ref

    Resurso kodinis pavadinimas, kuris yra apibrėžtas atskirai duomenų
    struktūros apraše, ar konfigūracijos failuose.

    Kai vienas resursas nurodo kitą, tuomet aprašomas resursas išplečia kitą
    resursą į kurį rodo arba naudoja kitą resursą, kaip konteinerį, kuriame
    saugomi duomenys.

    Išplėtimo atveju, galima pateikti tam tikro resurso konfidencialius
    duomenis, tokius, kaip slaptažodis, atskirai nuo duomenų struktūros aprašo,
    konfigūracijos failuose, o duomenų struktūros apraše išplėsti resursą,
    pateikiant ne konfidencialius duomenis.

    Tokiais atvejais, kaip duomenų failai saugomi ZIP archyvuose arba FTP
    serveryje, galima atskirai aprašyti ZIP ar FTP resursą, o po to, aprašant
    konkretų duomenų failo resursą, pateikti nuorodą, kuriame kitame resurse
    aprašomas failas yra.

.. data:: resource.level

    Viso duomenų šaltinio brandos lygis. Paveldimas.

.. data:: resource.access

    Viso duomenų šaltinio prieigos lygis. Paveldimas.

.. data:: resource.title

    Duomenų šaltinio pavadinimas.

.. data:: resource.description

    Duomenų šaltinio aprašymas.

Duomenų šaltinio :data:`resource.type` reikšmė apibrėžia kokią :term:`ETL`
priemonę naudoti skaitant duomenis iš duomenų šaltinio. Automatizuota duomenų
priemonė skirta įstaigos duomenų atvėrimui turėtų palaikyti tik tokius duomenų
šaltinius, kurie naudojami įstaigos vidinėje infrastruktūroje.

Esant poreikiui gali būti įgyvendintas palaikymas naujiems duomenų šaltiniams.


.. _base:

Modelio bazė
------------

.. note:: Kol kas modelių apjungimas naudojant vieną bazę nėra įgyvendintas.

Modelio bazė naudojama kelių modelių (lentelių) susiejimui arba apjungimui.
Kadangi įvairiuose duomenų šaltiniuose dažnai pasitaiko duomenų, kuriuose
saugomos tą pačią semantinę prasmę turinčios lentelės, :data:`base` stulpelyje
galima nurodyti kaip skirtingos lentelės siejasi tarpusavyje.

:data:`base.type` stulpelyje nurodoma kokiu būdu lentelės yra susiję.
:term:`ETL` priemonė vadovaujantis :data:`base` informacija duomenis
automatiškai transformuoja ir sujungia kelias lenteles į vieną.

Modeliai ne tik susiejami semantiškai tarpusavyje, bet taip pat suliejami ir
dviejų modelių duomenys naudojant laukų sąrašą nurodytą :data:`base.ref`
stulpelyje. :data:`base.ref` stulpelyje nurodyti laukai naudojami norint
unikaliai identifikuoti :data:`model` lentelėje esančią eilutę, kuri atitinka
:data:`base` lentelėje esančią eilutę.

Siejant :data:`model` ir :data:`base` duomenis tarpusavyje, :data:`model`
lentelė įgauna lygiai tokius pačius unikalius identifikatorius, kurie yra base
lentelėje. Tai reiškia, kad :data:`model` lentelėje negali būti duomenų, kurių
nėra :data:`base` lentelėje.

:data:`model.property` laukai turi sutapti su :data:`base` modelio laukais,
tačiau :data:`model` gali turėti ir papildomų laukų, kurių nėra :data:`base`
modelyje Visi :data:`base.ref` laukai turi būti aprašyti tiek :data:`base`, tiek
:data:`model` modeliuose.

.. data:: base.source

Nenaudojamas.

.. data:: base.prepare

    Išimtiniais atvejais, kai nėra galimybės lentelių susieti ar apjungti
    įprastiniais metodais, galima pasitelkti formules, kurių pagalba galima
    įgyvendinti nestandartinius lentelių apjungimo atvejus.

.. data:: base.type

    Lentelių susiejimo tipas. Jei nenurodyta naudoti `sameas`.

    Galimos reikšmės:

    .. describe:: base

        Išplečia :data:`base` ir saugo tik tų :data:`property` duomenis, kurių
        neturi :data:`base`. :data:`base` ir :data:`model` identifikatoriai
        sutampa.

    .. describe:: sameas

        Naudojama, kai tą pačią semantinę prasmę turintys duomenys saugomi
        skirtingose vietose.

    .. describe:: proxy

        Naudojama tada, kai kelių modelių duomenys yra identiški vienam
        :data:`base` ir reikia duomenis saugoti tik į :data:`base`.

    .. describe:: prototype

        Naudojamas tada, kai :data:`model` tik paveldi :data:`base` savybes,
        tačiau duomenis saugo atskirai ir identifikatorių nepernaudoja iš
        :data:`base`.

    Savybių matrica:

    ==========  ==========  ===========  =======================  =======  =========
    \           Sutampantys laukai                                Saugo duomenis į
    ----------  ------------------------------------------------  ------------------
    base.type   Išplečiami  Dubliuojami  Vienas identifikatorius  base     model
    ==========  ==========  ===========  =======================  =======  =========
    base        taip        ne           taip                     taip     taip [*]_
    sameas      taip        taip         taip                     taip     taip
    proxy       ne          ne           taip                     taip     ne
    prototype   taip        taip         ne                       ne       taip
    ==========  ==========  ===========  =======================  =======  =========

    .. [*] Saugo tik tuos duomenis, kurie nėra saugomi base modelyje.

    Išplečiami
        :data:`model` gali turėti property eilučių, kurių neturi :data:`base`.

    Dubliuojami
        :data:`model` saugo :data:`property` reikšmes, kurios sutampa su
        :data:`base`.

    Vienas identifikatorius
        :data:`model` gauna identifikatorių iš :data:`base` ir abiejose vietose
        naudojamas vienodas identifikatorius.

.. data:: base.ref

    :data:`model.property` reikšmė, kurios pagalba :data:`model` objektai
    siejami su :data:`base` objektais. Jei susiejimas pagal vieną model property
    yra neįmanomas, galima nurodyti kelis :data:`model.property` pavadinimus
    atskirtus kableliu.

.. data:: base.level

    Baziniam modeliui priskirtų modelių :ref:`brandos lygis <level>`.
    Paveldimas.

.. data:: base.access

    Baziniam modeliui priskirtų modelių :ref:`prieigos lygis <access>`.
    Paveldimas.

Paaiškinimas, ką reiškia kiekviena savybė.


.. _duomenų-modelis:

Duomenų modelis
---------------

Duomenų modelis apibrėžia duomenų grupę turinčią tas pačias savybes.
Skirtinguose duomenų šaltiniuose ir formatuose, duomenų modelis gali būti
išreikštas skirtingomis formomis, pavyzdžiui `sql` duomenų šaltinio atveju,
modelis aprašo vieną duomenų bazės lentelę.

Kiekvienas modelis turi turėti pirminį raktą, unikalų modelio duomenų
identifikatorių. Pirminis raktas aprašomas pateikiant vieną ar kelias
:data:`model.property` reikšmes :data:`model.ref` stulpelyje, kurios kartu
unikaliai identifikuoja kiekvieną duomenų eilutę.

Išimtiniais atvejais, kai modelio duomenų laukų reikšmės turi būti generuojamos
dinamiškai ar kitais nestandartiniais atvejais yra galimybė nurodyti model.type
reikšmę. Jei :data:`model.type` yra pateiktas, tada už modelio duomenų
generavimą, įeinančių duomenų tikrinimą ir visos kitos su modeliu susijusios
dalys gali būti pritaikytos konkretaus modelio atvejui. Tačiau, jei reikia
keisti tik duomenų pateikimą, užtenka naudoti :data:`model.prepare` formules.

.. data:: model.source

    Modelio pavadinimas šaltinyje. Prasmė priklauso nuo :data:`resource.type`.

.. data:: model.prepare

    Formulė skirta duomenų filtravimui ir paruošimui, iš dalies priklauso nuo
    :data:`resource.type`.

    Taip pat skaitykite: :ref:`duomenų-atranka`.

.. data:: model.type

    Jei nurodytą, naudoti išplėstą modelio variantą, jei nenurodyta palikti
    tuščią. Jei tuščia, naudoti standartinį modelio variantą.

    Gali būti įrašoma reikšmė `absent`, kuri nurodo, kad modelis buvo ištrintas.

.. data:: model.ref

    Kableliu atskirtas sąrašas :data:`model.property` reikšmių, kurios kartu
    unikaliai identifikuoja vieną duomenų eilutę (pirminis lentelės raktas).

.. data:: model.level

    Modeliui priklausančių laukų :ref:`brandos lygis <level>`. Paveldimas.

.. data:: model.access

    Modeliui priklausančių laukų :ref:`prieigos lygis <access>`. Paveldimas.

.. data:: model.uri

    Sąsaja su :ref:`išoriniu žodynu <vocab>`.

.. data:: model.title

    Modelio pavadinimas.

.. data:: model.description

    Modelio aprašymas.

.. data:: model.property

    Modeliui priklausantis duomenų laukas.


.. _savybė:

Savybė
------

.. data:: property.source

    Duomenų lauko pavadinimas šaltinyje. Prasmė priklauso nuo
    :data:`resource.type`.

.. data:: property.prepare

    Formulė skirta duomenų tikrinimui ir transformavimui arba statinės reikšmės
    pateikimui.

.. data:: property.type

    Žiūrėti :ref:`duomenų-tipai`.

.. data:: property.ref

    Priklauso nuo `property.type`, nurodo matavimo vienetus, laiko ar vietos
    tikslumą, :ref:`klasifikatorių <enum>` arba :ref:`ryšį su kitais modeliais
    <ryšiai>`. Ką tiksliai reiškia šis laukas, patikslinta skyrelyje
    :ref:`duomenų-tipai`.

.. data:: property.level

    Nurodo duomenų lauko brandos lygį. Žiūrėti :ref:`level`.

.. data:: property.access

    Nurodo prieigos prie duomenų lygį. Žiūrėti skyrių :ref:`access`.

.. data:: property.uri

    Sąsaja su išoriniu žodynu. Žiūrėti :ref:`vocab`.

.. data:: property.title

    Duomenų lauko pavadinimas. Šis pavadinimas yra skirtas skaityti žmonėms
    ir bus rodomas duomenų laukų sąrašuose ir antraštėse. Jei nenurodyta, bus
    naudojamas :data:`property` kodinis pavadinimas.

.. data:: property.description

    Duomenų lauko aprašymas.

.. data:: property.enum

    Žiūrėti :ref:`enum`.


.. _papildomos-dimensijos:

Papildomos dimensijos
=====================

.. _išorinių-žodynų-prefiksai:

Išorinių žodynų prefiksai
-------------------------

Sąsają su išoriniais žodynais galima pateikti :data:`model.uri` ir
:data:`property.uri` stulpeliuose. Tačiau prieš naudojant žodynus, pirmiausia
reikia apsirašyti žodynų prefiksus. Žodynų prefiksai aprašomi taip:

.. data:: prefix

    .. data:: prefix.ref

        Prefikso pavadinimas.

    .. data:: prefix.uri

        Išorinio žodyno URI.

    .. data:: prefix.title

        Prefikso antraštė.

    .. data:: prefix.description

        Prefikso aprašymas.

Rekomenduojama naudoti LOV_ prefiksus.

.. _LOV: https://lov.linkeddata.es/dataset/lov/

Aprašyti prefiksai gali būti naudojami :data:`model.uri` ir :data:`property.uri`
stulpeliuose tokiu būdu: `prefix:name`.


.. _enum:

Klasifikatoriai
---------------

.. _Categorical data: https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html

Tam tikri duomenų laukai turi fiksuotą reikšmių variantų aibę. Dažnai duomenų
bazėse fiksuotos reikšmės saugomos skaitine forma ar kitais kodiniais
pavadinimais. Tokias fiksuotas reikšmes duomenų struktūros apraše galima
pateikti neužpildant hierarchinių stulpelių ir nurodant `type` reikšmę
`enum`, pavyzdžiui:

+----+---+---+---+---+----------+---------+-----+-----------+-----------+-------+--------+-----+---------+-------------+
| id | d | r | b | m | property | type    | ref | source    | prepare   | level | access | uri | title   | description |
+====+===+===+===+===+==========+=========+=====+===========+===========+=======+========+=====+=========+=============+
|  1 | datasets/example/places  |         |     |           |           |       |        |     |         |             |
+----+---+---+---+---+----------+---------+-----+-----------+-----------+-------+--------+-----+---------+-------------+
|  2 |   | places               | sql     |     | sqlite:// |           |       |        |     |         |             |
+----+---+---+---+---+----------+---------+-----+-----------+-----------+-------+--------+-----+---------+-------------+
|  3 |   |   |   | Place        |         | id  | PLACES    |           |       |        |     |         |             |
+----+---+---+---+---+----------+---------+-----+-----------+-----------+-------+--------+-----+---------+-------------+
|  4 |   |   |   |   | id       | integer |     | ID        |           | 3     | open   |     |         |             |
+----+---+---+---+---+----------+---------+-----+-----------+-----------+-------+--------+-----+---------+-------------+
|  5 |   |   |   |   | type     | string  |     | CODE      |           | 3     | open   |     |         |             |
+----+---+---+---+---+----------+---------+-----+-----------+-----------+-------+--------+-----+---------+-------------+
|  6 |   |   |   |   |          | enum    |     | 1         | "city"    |       |        |     | City    |             |
+----+---+---+---+---+----------+---------+-----+-----------+-----------+-------+--------+-----+---------+-------------+
|  7 |   |   |   |   |          |         |     | 2         | "town"    |       |        |     | Town    |             |
+----+---+---+---+---+----------+---------+-----+-----------+-----------+-------+--------+-----+---------+-------------+
|  8 |   |   |   |   |          |         |     | 3         | "village" |       |        |     | Village |             |
+----+---+---+---+---+----------+---------+-----+-----------+-----------+-------+--------+-----+---------+-------------+
|  9 |   |   |   |   | name     | string  |     | NAME      |           | 3     | open   |     |         |             |
+----+---+---+---+---+----------+---------+-----+-----------+-----------+-------+--------+-----+---------+-------------+

Šiame pavyzdyje `Place.type` laukas yra klasifikatorius, kurio reikšmės yra
kodai 1, 2 ir 3, kurios duomenų struktūros apraše keičiamos į `city`, `town`
ir `village`, papildomai `title` stulpelyje nurodant reikšmės pavadinimą.

Jei tas pats klasifikatorius gali būti naudojamas kelios skirtingose vietos,
tada galima iškelti klasifikatorių ir suteikti jam pavadinimą, pavyzdžiui:

+----+---+---+---+---+----------+---------+---------+-----------+---------------+-------+--------+-----+---------+-------------+
| id | d | r | b | m | property | type    | ref     | source    | prepare       | level | access | uri | title   | description |
+====+===+===+===+===+==========+=========+=========+===========+===============+=======+========+=====+=========+=============+
|  6 |   |   |   |   |          | enum    | place   | 1         | "city"        |       |        |     | City    |             |
+----+---+---+---+---+----------+---------+---------+-----------+---------------+-------+--------+-----+---------+-------------+
|  7 |   |   |   |   |          |         |         | 2         | "town"        |       |        |     | Town    |             |
+----+---+---+---+---+----------+---------+---------+-----------+---------------+-------+--------+-----+---------+-------------+
|  8 |   |   |   |   |          |         |         | 3         | "village"     |       |        |     | Village |             |
+----+---+---+---+---+----------+---------+---------+-----------+---------------+-------+--------+-----+---------+-------------+
|  1 | datasets/example/places  |         |         |           |               |       |        |     |         |             |
+----+---+---+---+---+----------+---------+---------+-----------+---------------+-------+--------+-----+---------+-------------+
|  2 |   | places               | sql     |         | sqlite:// |               |       |        |     |         |             |
+----+---+---+---+---+----------+---------+---------+-----------+---------------+-------+--------+-----+---------+-------------+
|  3 |   |   |   | Place        |         | id      | PLACES    |               |       |        |     |         |             |
+----+---+---+---+---+----------+---------+---------+-----------+---------------+-------+--------+-----+---------+-------------+
|  4 |   |   |   |   | id       | integer |         | ID        |               | 3     | open   |     |         |             |
+----+---+---+---+---+----------+---------+---------+-----------+---------------+-------+--------+-----+---------+-------------+
|  5 |   |   |   |   | type     | string  | place   | CODE      |               | 3     | open   |     |         |             |
+----+---+---+---+---+----------+---------+---------+-----------+---------------+-------+--------+-----+---------+-------------+
|  9 |   |   |   |   | name     | string  |         | NAME      |               | 3     | open   |     |         |             |
+----+---+---+---+---+----------+---------+---------+-----------+---------------+-------+--------+-----+---------+-------------+

Šiuo atveju, klasifikatoriui buvo suteiktas pavadinimas `place` įrašytas
`enum.ref` stulpelyje, 6 eilutėje. O `Place.type` laukui, `prepare`
stulpelyje nurodyta, kad šis laukas naudoja vardinį `place` klasifikatorių.


.. data:: enum

    .. data:: enum.ref

        Pasirinkimų sąrašo pavadinimas.

    .. data:: enum.source

        Pateikiama originali reikšmė, taip kaip ji saugoma duomenų šaltinyje.
        Pateiktos reikšmės turi būti unikalios ir negali kartotis.

        Jei pageidaujama aprašyti tuščią šaltinio reikšmę, tada
        :data:`property.prepare` celėje reikia nurodyti formulę, kuri tuščią
        reikšmę pakeičia, į kokią nors kitą. Formulės pavyzdys:

        .. code-block:: python

            swap('', '-')

    .. data:: enum.prepare

        Pateikiama reikšmė, tokia kuri bus naudojama atveriant duomenis.
        :data:`model.prepare` filtruose taip pat bus naudojama būtent ši
        reikšmė.

        `enum.prepare` reikšmės gali kartotis, tokiu būdu, kelios skirtingos
        `enum.source` reikšmės bus susietos su viena `enum.prepare` reikšme.

    .. data:: enum.access

        Klasifikatoriams galima nurodyti skirtingas prieigos teises, tokiu
        atveju, naudotojas turintis `open` prieigą matys tik tuos duomenis,
        kurių klasifikatorių reikšmės turi `open` prieigos teises, visi kiti bus
        išfiltruoti.

    .. data:: enum.title

        Fiksuotos reikšmės pavadinimas.

    .. data:: enum.description

        Fiksuotos reikšmės aprašymas.

Pagal nutylėjimą, jei :data:`property.prepare` yra tuščias ir :data:`property`
turi :ref:`enum` sąrašą, tada jei šaltinis turi neaprašytą reikšmę, turėtų
būti fiksuojama klaida.

Jei yra poreikis fiksuoti tik tam tikras reikšmes, o visas kitas palikti tokias,
kokios yra šaltinyje, tada :data:`property.prepare` stulpelyje reikia įrašyti
`self.choose(self)`.


.. _param:

Parametrai
----------

Parametrai leidžia iškelti tam tikras duomenų paruošimo operacijas į parametrus
kurie gali būti naudojami :ref:`dimensijos`, kurioje apibrėžtas parametras
kontekste. Parametrai gali gražinti :term:`iteratorius`, kurių pagalba galima
dinamiškai kartoti :data:`resource` duomenų skaitymą, panaudojant aprašytus
parametrus. Taip pat parametrų pagalba galima sudaryti reikšmių sąrašus, kurių
pagalba galima kartoti :data:`resource` su kiekviena reikšme.

Parametrai dažniausiai naudojami žemesnio brandos lygio duomenų šaltiniams
aprašyti, o taip pat API atvejais, kai duomenys atiduodame dinamiškai.

Parametrai aprašomi pasitelkiant papildomą :ref:`param` dimensiją.

+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
| id | d | r | b | m | property   | type    | ref                   | source                      | prepare               |
+====+===+===+===+===+============+=========+=======================+=============================+=======================+
|  1 | datasets/example/cities    |         |                       |                             |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  2 |   | places                 | csv     |                       | \https://example.com/{}.csv |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  3 |   |   |   | Country        |         | id                    | countries                   |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  4 |   |   |   |   | code       | string  |                       | CODE                        |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  5 |   |   |   |   | title      | string  |                       | TITLE                       |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  6 |   |   |   | City           |         | country, |nbsp| title | cities/{country.code}       |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  7 |   |   |   |   |            | param   | country               | Country                     | select(code)          |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  8 |   |   |   |   | country    | ref     | Country               |                             | param("country").code |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  9 |   |   |   |   | title      | string  |                       | TITLE                       |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+

.. data:: param

    .. data:: param.ref

        Parametro :term:`kodinis pavadinimas`.

    .. data:: param.prepare

        Formulė, kuri grąžina sąrašą reikšmių aprašomam parametrui.

    .. data:: param.source

        Jei reikšmė pateikta, tada ši reikšmė perduodama formulei kaip `self`.
        Pavyzdžiui, jei :data:`param.prepare` pateikta formulė `select(code)`, o
        :data:`param.source` nurodyta `Country`, tai formulė bus iškviesta taip
        `select("Country", code)`.

Jei parametro reikšmė yra :term:`iteratorius`, tada :term:`dimensija`, kurios
kontekste yra aprašytas :ref:`parametras <param>` yra kartojama tiek kartų,
kiek reikšmių grąžina :term:`iteratorius`.

Jei yra keli :ref:`param` grąžinantys :term:`iteratorius`, tada iš
visų :term:`iteratorių <iteratorius>` sudaroma `Dekarto sandauga`_ ir
:data:`resource` dimensija vykdoma su kiekviena sandaugos rezultato reikšme.

.. _Dekarto sandauga: https://lt.wikipedia.org/wiki/Dekarto_sandauga

Jei sekančioje :term:`DSA` eilutėje, einančioje po eilutės, kurioje aprašytas
:ref:`param`, nenurodytas :data:`type` ir neužpildytas joks kitas
:term:`dimensijos <dimensija>` stulpelis, tada parametras tampa
:term:`iteratoriumi <iteratorius>`, kurio reikšmių sąrašą sudaro sekančiose
eilutėse patektos :data:`source` ir :data:`prepare` reikšmės. Pavyzdžiui
anksčiau pateiktą pavyzdį galima būtų perdaryti taip:

+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
| id | d | r | b | m | property   | type    | ref                   | source                      | prepare               |
+====+===+===+===+===+============+=========+=======================+=============================+=======================+
|  1 | datasets/example/cities    |         |                       |                             |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  2 |   | places                 | csv     |                       | \https://example.com/{}.csv |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  3 |   |   |   | Country        |         | id                    | countries                   |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  4 |   |   |   |   | code       | string  |                       | CODE                        |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  5 |   |   |   |   | title      | string  |                       | TITLE                       |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  6 |   |   |   | City           |         | country, |nbsp| title | cities/{country}            |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  7 |   |   |   |   |            | param   | country               |                             | "lt"                  |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  7 |   |   |   |   |            |         |                       |                             | "lv"                  |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  7 |   |   |   |   |            |         |                       |                             | "ee"                  |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  8 |   |   |   |   | country    | ref     | Country               |                             | param("country")      |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+
|  9 |   |   |   |   | title      | string  |                       | TITLE                       |                       |
+----+---+---+---+---+------------+---------+-----------------------+-----------------------------+-----------------------+

Šiame pavyzdyje, parametras `country` grąžins tris šalies kodus: lt, lv ir
ee, kurie bus panaudojami `cities/{country}` pavadinime, pakeičiant
`{country}` dalį.

:ref:`param` reikšmės pasiekiamos naudojanti pavadinimą įrašytą
:data:`param.ref` stulpelyje. Pavyzdžiui, jei :data:`param.ref` stulpelyje
įrašyta `x`, tada `x` parametro reikšmę galima gauti taip:

.. describe:: source

    `{x}`.

.. describe:: prepare

    `x` arba `param(x)`.

Parametrų generavimui galima naudoti tokias formules:

.. describe:: param.prepare

    .. function:: range(stop)

        Sveikų skaičių generavimas nuo 0 iki `stop`, `stop` neįeina.

    .. function:: range(start, stop)

        Sveikų skaičių generavimas nuo `start` iki `stop`, `stop` neįeina.

    .. function:: scalar(name)

        Jei nurodytas :data:`param.source`, tada imama tik `name` lauko reikšmė,
        o ne visi modelio laukai.

Jei užpildytas :data:`param.source` stulpelis, tada :data:`param.prepare`
stulpelyje galima naudoti filtrą nurodyto :data:`param.source` modelio duomenims
filtruoti, o naudojant parametrus galima nurodyti ir modelio laukų pavadinimus,
pavyzdžiui:

.. describe:: source

    `{x.field}`.

.. describe:: prepare

    `x.field` arba `param(x).field`.




Reikšmių sukeitimas
-------------------

Tam tikrais atvejais duomenis tenka normalizuoti parenkant tam tikrą reikšmę jei
tenkinama nurodyta sąlyga. Tokias situacijas galima aprašyti pasitelkiant
:data:`switch` dimensiją.

.. data:: switch

    .. data:: switch.source

        Reikšmė, kuri bus atveriama.

    .. data:: switch.prepare

        Sąlyga, naudojant einamojo modelio laukus. Jei sąlyga tenkinama, tada
        laukui priskiriama :data:`switch.source` reikšmė. Jei sąlyga
        netenkinama, tada bandoma tikrinti sekančią sąlygą. Parenkama ta
        reikšmė, kurios pirmoji sąlyga tenkinama.

        Jei :data:`switch.prepare` yra tuščias, tada sąlyga visada teigiama ir
        visada grąžinama :data:`switch.source` reikšmė.


Komentavimas
------------

Dirbant su :term:`DSA` yra galimybė komentuoti eilutes, naudojant papildomą
:data:`comment` dimensiją, kurią galima naudoti bet kurios kitos dimensijos
kontekste.

.. data:: comment

    .. data:: comment.id

        Komentaro numeris.

    .. data:: comment.title

        Komentaro data, `ISO 8601`_ formatu.

        .. _ISO 8601: https://en.wikipedia.org/wiki/ISO_8601

    .. data:: comment.description

        Komentaro tekstas.

    .. data:: comment.source

        Komentaro autorius.

    .. data:: comment.ref

        Cituojamo komentaro numeris. Jei šis stulpelis užpildytas, tai reiškia,
        kad komentaras yra atsakymas į kitą, nurodyto numerio komentarą.

    .. data:: comment.access

        Nurodoma, ar komentaras gali būti publikuojamas viešai.

        private
            Komentaras negali būti publikuojamas viešai. Šis prieigos lygis
            naudojamas pagal nutylėjimą.

        open
            Komentaras gali būti publikuojamas viešai.


Daugiakalbiškumas
-----------------

:data:`title` ir :data:`description` stulpeliuose tekstas rašomas lietuvių
kalba, tačiau galima pateikti tekstą ir kita kalba, panaudojus papildomą
:data:`lang` dimensiją, kurią reikia naudoti prieš eilutę, kuriai pateikiamas
tekstas kita kalba.

.. data:: lang

    .. data:: lang.ref

        `ISO 639-1`_ dviejų simbolių kalbos kodas.

        .. _ISO 639-1: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

    .. data:: lang.title

        Pavadinimas :data:`lang.ref` stulpelyje nurodyta kalba.

    .. data:: lang.description

        Aprašymas :data:`lang.ref` stulpelyje nurodyta kalba.


.. _struktūros-keitimas:

Struktūros keitimas
-------------------

Laikui einant, pirminių duomenų šaltinių arba jau atvertų duomenų struktūra
keičiasi, papildoma naujais :term:`modeliais <modelis>` ar :term:`savybėmis
<savybė>`, keliant duomenų brandos lygį seni duomenys keičiami naujais,
aukštesnio brandos lygio duomenimis.

Visi šie struktūros ar pačių duomenų pasikeitimai fiksuojami papildomos
:data:`migrate` dimensijos pagalba, kuri gali būti naudojama, bet kurios kitos
dimensijos kontekste.

.. data:: migrate

    .. data:: migrate.ref

        Migracijos numeris (UUID). Kiekvienos migracijos metu gali būti
        atliekama eilė operacijų, visos operacijos fiksuojamos naudojant
        migracijos numerį.

        Visų migracijų sąrašas pateikiamas, kai :data:`migrate` nepriklauso
        jokiam dimensijos kontekstui. Migracijų eiliškumas yra svarbus.

    .. data:: migrate.source

        Ankstesnės migracijos numeris, pateiktas :data:`migrate.ref` stulpelyje,
        arba tuščia, jei prieš tai jokių kitų migracijų nebuvo.

        Naudojamas jei :data:`migrate` nepatenka į jokios dimensijos kontekstą.

        Jei :data:`migrate` aprašomas dimensijos kontekste, tada šis stulpelis
        nenaudojamas.

    .. data:: migrate.prepare

        Migracijos operacija. Galimos tokios operacijos:

        .. function:: create(**kwargs)

            Priklausomai nuo dimensijos konteksto, prideda naują modelį, arba
            savybę.

            Funkcijai galima perduoti `name` ir kitus vardinius argumentus,
            kurie atitinka :term:`DSA` lentelės metaduomenų stulpelių
            pavadinimus.

        .. function:: update(**kwargs)

            Priklausomai nuo dimensijos konteksto, keičia modelį ar savybę.

            Funkcijai galima perduoti `name` ir kitus vardinius argumentus,
            kurie atitinka :term:`DSA` lentelės metaduomenų stulpelių
            pavadinimus.

            Perduodami tik tie vardiniai argumentai, kuriuos atitinkantys
            metaduomenys keičiasi.

        .. function:: delete()

            Priklausomai nuo dimensijos konteksto, šalina modelį ar savybę.

            Pašalinto modelio ar savybės :data:`type` keičiamas į `absent`
            reikšmę.

        .. function:: filter(where)

            Naudojamas :data:`property` kontekste, kai vykdoma duomenų
            migracija. Nurodo, kad migracija taikoma tik `where` sąlygą
            tenkinantiems duomenims.

        Be šių pagrindinių migracijos operacijų, galima naudoti kitas duomenų
        transformavimo operacijas, kurios vykdomos su kiekviena duomenų eilute
        ir atlikus pateiktas transformacijos funkcijas, pakeista reikšmė
        išsaugoma.

    .. data:: migrate.title

        Migracijos data ir laikas.

        Naudojamas tik tada, kai :data:`migrate` nepatenka į jokios dimensijos
        kontekstą.

    .. data:: migrate.description

        Migracijos atliekamo pakeitimo trumpas aprašymas.


.. _vardų-erdvės-dimensija:

Vardų erdvės
------------

Vardų erdvės gali būti aprašomos  pasitelkiant :data:`ns` papildomą dimensiją.

.. data:: ns

    .. data:: ns.ref

        Vardų erdvės kodinis pavadinimas.

    .. data:: ns.title

        Vardų erdvės pavadinimas.

    .. data:: ns.description

        Vardų erdvės aprašymas.



.. |nbsp| unicode:: 0xA0
   :trim: