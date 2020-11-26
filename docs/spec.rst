.. default-role:: literal

.. _spec:


Specifikacija
#############

Čia rasite pilna duomenų struktūros aprašo (:term:`DSA`) lentelės specifikaciją.

:term:`Duomenų struktūros aprašas <DSA>` yra lentelė, kurią galima redaguoti
skaičiuoklės pagalba. Lentelėje pateikiama informacija apie vieno ar kelių
duomenų šaltinių struktūrą.

:term:`Duomenų struktūros aprašas <DSA>` skirtas tam, kad būtų galima
automatizuoti duomenų atvėrimo veiklas. Įstaigoms, atveriančioms duomenis,
daugeliu atveju turėtu užtekti paruošti tik :term:`DSA` lentelę. Turint parengtą
:term:`DSA` lentelę, visos kitos veiklos yra pilnai automatizuojamos.

Vieninga aprašų struktūros parengimo metodika sudaro galimybę automatizuoti
duomenų atvėrimo ir publikavimo procesus bei užtikrinti atveriamų duomenų
kokybę, vientisumą ir viso proceso stebėseną.

:term:`Duomenų struktūros aprašas <DSA>` gali būti rengiamas jau atvertiems
duomenims (:term:`ADSA`) ir dar neatvertiems duomenims (:term:`ŠDSA`).


Šaltinio duomenų struktūros aprašas (ŠDSA)
==========================================

:term:`ŠDSA` yra :term:`DSA` lentelė, kurioje aprašoma :term:`pirminio duomenų
šaltinio <pirminis duomenų šaltinis>` struktūra.

Jei įmanoma pirminis :term:`ŠDSA` lentelės variantas generuojamas automatiškai,
skaitant šaltinio duomenų struktūrą. Vėliau pirminis :term:`ŠDSA` papildomas ir
taisomas rankiniu būdu, suskirstant duomenis į :term:`duomenų rinkinius <duomenų
rinkinys>`, nurodant kurie duomenų laukai gali būti atverti, pateikiant duomenų
laukų aprašymus, atliekant nuasmeninimo transformacijas ir pan.

Jei automatiškai generuoti :term:`ŠDSA` galimybės nėra, tada :term:`ŠDSA`
rengiamas rankiniu būdu.

Galiausiai publikavimui paruoštas :term:`ŠDSA` transformuojamas į :term:`ADSA`,
pašalinant vidinės struktūros informaciją ir paliekant tik viešinimui skirtą
informaciją. :term:`ADSA` skaidomas į vieno duomenų rinkinio lenteles ir
automatiškai įkeliamas į :term:`ADK`. :term:`ADSA` turėtų būti publikuojamas
:term:`ADK` dar prieš publikuojant pačius duomenis.

Duomenys publikuojami naudojant :term:`ŠDSA` lentelėje pateiktus metaduomenis.
Duomenų publikavimas gali būti atliekamas kopijuojant duomenis į centrinę
duomenų saugyklą (:term:`ADS`), kopijuojami į įstaigos :term:`atvirų duomenų
saugyklą <ADS>` arba teikiami tiesiai iš įstaigos duomenų bazių ar
paprasčiausiai eksportuojami vienu iš atvirų duomenų formatų.

Po to, kai duomenys publikuojami, turi būti atnaujinamas ir :term:`ADSA`,
pateikiant informaciją apie tai kur ir kaip pasiekti publikuotus duomenis.

Jei :term:`ŠDSA` apimtis yra didelė, tada :term:`ŠDSA` paruošimo publikavimui
darbus reikėtų atlikti palaipsniui. Pirmiausiai publikavimui reikėtų parengti
tuos duomenis, kuriems yra išreikštas didžiausias poreikis.

:term:`ŠDSA` parengimas publikavimui yra pagrindinė veikla atveriant duomenis,
kadangi didelė dalis duomenų atvėrimo proceso gali būti automatizuojama
naudojant :term:`ŠDSA` pateiktus metaduomenis.

Jei įstaiga jau yra atvėrusi ir publikavusi duomenis, tada :term:`ŠDSA` rengti
nereikia, tačiau reikia parengti :term:`ADSA`.


Atvertų duomenų struktūros aprašas (ADSA)
=========================================

Įprastai :term:`ADSA` turėtu būti generuojamas automatiškai :term:`ŠDSA`
pagrindu. Tačiau jei įstaiga jau yra atvėrusi duomenis ir neturi :term:`ŠDSA`,
tada :term:`ADSA` jei įmanoma, automatiškai generuojamas atvertų duomenų
pagrindu.

:term:`ADSA` lentelėje gali būti aprašyta daug duomenų rinkinių, tačiau
publikuojant duomenų rinkinių metaduomenis į :term:`ADK`, :term:`ADSA` lentelė
turi būti suskaidoma į dalis pagal domenų rinkinius. Vienoje dalyje turi būti
tik vieno duomenų rinkinio aprašas.

Nepriklausomai kur ir kaip publikuojami atverti duomenys :term:`ADSA` dėka visi
duomenys galiausiai kopijuojami į centrinę valstybinę duomenų saugyklą iš kurios
duomenys teikiami įvairiais formatais, sudarant galimybę duomenis pasiekti per
centrinį valstybinį API.


Lentelės formatas
=================

:term:`DSA` yra sudarytas taip, kad būtų patogu dirbti tiek žmonėms, tiek
programoms. Žmonės su :term:`DSA` lentele gali dirbti naudojantis, bet kuria
skaičiuoklės programa ar kitas pasirinktas priemones. Kadangi :term:`DSA` turi
aiškią ir griežtą struktūrą, lentelėje pateiktus duomenis taip pat gali lengvai
nuskaityti ir interpretuoti kompiuterinės programos.

Tais atvejais, kai su :term:`DSA` lentele dirba žmonės, lentelė gali būti
saugoma įstaigos pasirinktos skaičiuoklės programos ar kitų priemonių formatu.

Automatizuotoms priemonėms :term:`DSA` turi būti teikiamas CSV formatu laikantis
:rfc:`4180` taisyklių, failo koduotė turi būti UTF-8.


Orientacinis įgyvendinimas
==========================

:term:`DSA` sudarytas remiantis praktine patirtimi, įgyvendinant priemones
skirtas automatizuotam duomenų atvėrimui. Minėtos priemonės gali būti
naudojamos, kaip orientacinis pavyzdys kuriant automatizuotas priemones.
Projekto kodą galima rasti šiuo adresu:

https://gitlab.com/atviriduomenys/spinta/

Šios priemonės bus naudojamas tikrinimui ar :term:`DSA` atitinka specifikaciją
ir ar patys atverti duomenys atitinka DSA.

Priemonės įgyvendintos naudojant Python_ programavimo kalbą ir priemonių kodas
teikiamas pagal atviro kodo MIT licencijos sąlygas. Projekto dokumentaciją
galima rasti šiuo adresu:

.. _Python: https://www.python.org/

https://spinta.readthedocs.io/


Lentelės struktūra
==================

Rengiant duomenų struktūros aprašus darbas vyksta su viena lentele. Lentelė
sudaryta iš 15 stulpelių. Ką reiškia kiekvienas stulpelis paaiškinta žemiau.


.. data:: id

    **Eilutės identifikatorius**

    Unikalus elemento numeris, gali būti sveikas, monotoniškai didėjantis
    skaičius arba UUID. Svarbu užtikrinti, kad visi elementai turėtu unikalų id.

.. data:: dataset

    **Duomenų rinkinys**

    Kodinis duomenų rinkinio pavadinimas. Atitinka dcat:Dataset prasmę.
    Žiūrėti Duomenų rinkinys.

.. data:: resource

    **Duomenų šaltinis**

    Kodinis duomenų šaltinio pavadinimas. Atitinka dcat:Distribution prasmę.
    Žiūrėti Duomenų šaltinis.

.. data:: base

    **Modelio bazė**

    Kodinis bazinio modelio pavadinimas. Atitinka rdfs:subClassOf prasmę
    (model rdfs:subClassOf base). Žiūrėti Modelio bazė.

.. data:: model

    **Modelis (lentelė)**

    Kodinis modelio pavadinimas. Atitinka rdfs:Class prasmę. Žiūrėti Duomenų
    modelis.

.. data:: property

    **Savybė (stulpelis)**

    Kodinis savybės pavadinimas. Atitinka rdfs:Property prasmę. Žiūrėti
    Duomenų laukas.

.. data:: type

    **Tipas**

    Prasmė priklauso nuo dimensijos. Žiūrėti Duomenų laukų tipai.

.. data:: ref

    **Ryšys**

    Prasmė priklauso nuo dimensijos. Žiūrėti Ryšiai tarp modelių.

.. data:: source

    **Šaltinis**

    Duomenų šaltinio struktūros elementai. Žiūrėti Duomenų šaltiniai.

.. data:: prepare

    **Formulė**

    Formulė skirta duomenų atrankai, nuasmeninimui, transformavimui,
    tikrinimui ir pan. Žiūrėti Formulės.

.. data:: level

    **Brandos lygis**

    Duomenų brandos lygis, atitinka 5 Star Data. Žiūrėti Brandos lygiai.

.. data:: access

    **Prieiga**

    Duomenų prieigos lygis. Žiūrėti Prieigos lygiai.

.. data:: uri

    **Žodyno atitikmuo**

    Sąsaja su išoriniu žodynu. Žiūrėti Sąsaja su išoriniais žodynais.

.. data:: title

    **Pavadinimas**

    Elemento pavadinimas.

.. data:: description

    **Aprašymas**

    Elemento aprašymas. Galima naudoti Markdown sintaksę.

:term:`Duomenų struktūros aprašo <DSA>` lentelėje laukas :data:`id` turi būti
visada užpildytas. :data:`id` reikšmė turi sutapti tiek :term:`ŠDSA` tiek
:term:`ADSA`.

Visi stulpeliai lentelėje yra neprivalomi. Stulpelių tvarka taip pat nėra svari.
Pavyzdžiui jei reikia apsirašyti tik globalių modelių struktūrą, nebūtina
įtraukti :data:`dataset`, :data:`resource` ir :data:`base` stulpelių. Jei norima
apsirašyti tik prefiksus naudojamus :data:`uri` lauke, užtenka turėti tik
prefiksų aprašymui reikalingus stulpelius.

Įrankiai skaitantys :term:`DSA`, stulpelius, kurių nėra lentelėje turi
interpretuoti kaip tuščius. Taip pat įrankiai neturėtų tikėtis, kad stulpeliai
bus išdėstyti būtent tokia tvarka. Nors įrankių atžvilgiu stulpelių tvarka nėra
svarbi, tačiau rekomenduotina išlaikyti vienodą stulpelių tvarką, tam kad
lenteles būtų lengviau skaityti.

Kodiniai pavadinimai
====================

Kadangi :term:`DSA` lentelė skirta naudoti tiek žmonėms tiek automatizuotoms
priemonėms, tam tikros lentelės dalys privalo naudoti sutartinius kodinius
pavadinimus. Kodiniams pavadinimams keliami griežtesni reikalavimai, kadangi
šiuos pavadinimus interpretuos automatizuotos priemonės.

Visi :term:`DSA` lentelės stulpelių pavadinimai turi būti užrašyti tiksliai
taip, kaip nurodyta, kad kompiuterio programos galėtų juos atpažinti.

Visuose dimensijų stulpeliuose ir kitose vietose kuriose nurodyta naudoti
kodinius pavadinimus keliamas reikalavimas, kad pavadinimai atitiktų šią
reguliariąją išraišką:

.. code-block:: regex

    [a-zA-Z][a-zA-Z0-1_-]+

Tai reiškia, kad pavadinimo pirmas simbolis turi būti lotyniška raidė, o
sekančios raidės gali būti lotyniškos raidės, skaičiai ir pabraukimo simbolis ar
brūkšnelis skirti žodžiams atskirti, jei pavadinimą sudaro daugiau nei vienas
žodis. Kodiniuose pavadinimuose gali būti tik lotyniškos raidės, lietuviškų
raidžių kodiniuose pavadinimuose neturi būti.

Pabraukimo simbolis ir brūkšnelis negali kartotis daugiau nei vieną kartą.

Interpretuojant kodinį pavadinimą, turi būti ignoruojamos didžiosios/mažosios
raidės, pabraukimo simbolis ir brūkšnelis. Tai reškia, kad visi šie
pavadinimai interpretuojami kaip sinonimai::

    kodinis-pavadinimas
    kodinis_pavadinimas
    KodinisPavadinimas
    kodinisPavadinimas

Ypatingas dėmesys turi būti kreipiamas suteikiant pavadinimus :data:`dataset`,
:data:`model` ir :data:`property` stulpeliuose. Šiuose stulpeliuose pateikti
pavadinimai naudojami identifikuojant konkrečias duomenų struktūros vietas, taip
pat šie pavadinimai bus naudojami publikuojant duomenis, tai reiškia, kad šiuos
pavadinimus naudos ir duomenų naudotojai. Po to, kai duomenys publikuojami
minėtų :data:`dataset`, :data:`model` ir :data:`property` pavadinimu reikėtų
vengti keisti, kad duomenų naudotojams nereikėtų taisyti jau padarytų
integracijų su atvertais duomenimis.


.. _vardų-erdvės:

Vardų erdvės
============

:data:`dataset` ir :data:`model` esantys pavadinimai turi būti globaliai
(Lietuvos mastu) unikalūs. Kad užtikrinti pavadinimų unikalumą :data:`dataset`
ir :data:`model` pavadinimai formuojami pasitelkiant vardų erdves.

.. describe:: /<standard>/

    **Standartų vardų erdvė**

    Standartų vardų erdvė formuojama egzistuojančių standartų ir išorinių žodynų
    pagrindu suteikiant vardų erdvei `<standard>` standarto sutrumpintą
    pavadinimą. Pavyzdžiui atvirų duomenų katalogo metaduomenys turėtų keliauti
    į `/dcat/` vardų erdvę. Standartų sutrumpintus pavadinimus rekomenduojame
    imti iš `Linked Open Vocabularies`_ katalogo.

    .. _Linked Open Vocabularies: https://lov.linkeddata.es/dataset/lov/

.. describe:: /transformations/<standard>/

    **Transformacijų vardų erdvė**

    Ši vardų erdvė skirta įstaigų duomenų rinkinių transformavimui į
    `/<standard>/` vardų erdvę, apjungiant visų įstaigų duomenis į vieningus
    modelius standartų vardų erdvėje.

    Ši vardų erdvė yra tranzitinė ir joje duomenys nesaugomi, o perduodami
    tiesiai į standartų vardų erdvėje esančius modelius, `proxy`
    :data:`base.type` pagalba.

.. describe:: /datasets/<type>/<org>/

    **Įstaigų vardų erdvė**

    Konkrečios organizacijos vietinė rinkinio vardų erdvė. Rekomenduojama
    `<org>` reikšmei naudoti organizacijos trumpinį, kad bendras modelio
    pavadinimas nebūtų per daug ilgas.

    Galimos `<type>` reikšmės:

    .. describe:: gov

        Valstybinės įstaigos.

    .. describe:: com

        Verslo įmonės.

.. describe:: /datasets/<type>/<org>/<dataset>/

    **Įstaigų duomenų rinkinių vardų erdvė**

    Įstaigos duomenų rinkinio vardų erdvė į kurią patenka visi įstaigos duomenų
    modeliai.

Naujai atveriami :term:`duomenų struktūros aprašai <DSA>` sudaromi :term:`ŠDSA`
pagrindu. Įprastai duomenų bazių struktūra nėra kuriami vadovaujantis
standartais. Vidinės struktūros dažniausiai kuriamos vadovaujantis sistemai
keliamais reikalavimais. Todėl naujai atveriamų duomenų rinkiniai turi keliauti
į duomenų rinkinio vardų erdvę `/datasets/<type>/<org>/<dataset>/`, išlaikant
pirminę duomenų struktūrą ir neprarandant duomenų.

Tačiau su laiku, dalis įstaigos duomenų iš duomenų rinkinio vardų erdvės turėtu
būti perkeliami į globalią duomenų erdvę. Į globalią duomenų erdvę pirmiausiai
turėtų būti perkeliami tie duomenys, kurie yra plačiai naudojami. Perkėlimas į
globalią duomenų erdvę nepanaikina duomenų rinkinio iš ankstesnės vardų erdvės,
tiesiog duomenų rinkinio duomenų pagrindu kuriama kopija į globalią duomenų
erdvę.

Vardų erdvės pavadinimai gali būti globalūs arba vietiniai. Globalūs vardų
erdvės pavadinimai turi prasidėti `/` simboliu, vietiniai vardų erdvės
pavadinimai neturi prasidėti `/` simboliu.

Modeliai gali būti aprašomi duomenų rinkinio kontekste arba nepriklausomai nuo
duomenų rinkinio. Jei modelis aprašomas duomenų rinkinio kontekste ir modelio
pavadinimas neprasideda `/` simboliu, tada pilnas modelio pavadinimas
formuojamas jungiant vietinį modelio pavadinimą prie duomenų rinkinio vardų
erdvės. Tačiau jei modelio pavadinimas prasideda `/` simboliu, tada pilnas
modelio pavadinimas nėra jungiamas prie duomenų rinkinio vardų erdvės.

Kaip tai atrodo :term:`DSA` lentelėje iliustruota žemiau:



+--------+-----+-----+-----+-----+--------------+
| |id|   | |d| | |r| | |b| | |m| | |property|   |
+========+=====+=====+=====+=====+==============+
|  **1** |     |     |     | ****dcat/dataset** |
+--------+-----+-----+-----+-----+--------------+
|      2 |     |     |     |     | title        |
+--------+-----+-----+-----+-----+--------------+
|  **3** | **datasets/gov/ivpk/adk**            |
+--------+-----+-----+-----+-----+--------------+
|      4 |     | adk                            |
+--------+-----+-----+-----+-----+--------------+
|      5 |     |     | **/dcat/dataset**        |
+--------+-----+-----+-----+-----+--------------+
|  **6** |     |     |     | **dataset**        |
+--------+-----+-----+-----+-----+--------------+
|      7 |     |     |     |     | title        |
+--------+-----+-----+-----+-----+--------------+

Šiame pavyzdyje matome, kad pirmoje eilutėje yra apibrėžtas `dcat/dataset`
modelis, kuris nėra susietas duomenų rinkiniu, tai reiškia, kad modelis yra
globalus. `dcat/dataset` modelio pavadinimas neturi `/` simbolio priekyje, todėl
pilnas modelio pavadinimas bus `/dcat/dataset`, nes šis modelis neturi duomenų
rinkinio konteksto. Modelio pavadinime `dcat` reiškia standarto arba domeno
(srities) pavadinimą.

Toliau lentelėje yra aprašytas duomenų rinkinys `datasets/gov/ivpk/adk`, kur
`gov` yra valstybinio sektoriaus duomenų erdvė, `ivpk` yra konkrečios įstaigos
sutrumpintas pavadinimas, o `adk` yra atvirų duomenų katalogo duomenų rinkinio
sutrumpintas pavadinimas.

Toliau 5 eilutėje nurodyta modelio bazė `/dcat/dataset`. Kadangi modelio bazės
pavadinimas prasideda `/` simboliu, tai modelio pavadinimas nesiejamas su
duomenų rinkinio vardų erdve ir rodo į pirmoje eilutėje apibrėžtą modelį.

6 eilutėje pateiktas modelio pavadinimas `dataset` neturi priekyje `/`, todėl
yra siejamas su duomenų rinkinio vardų erdve. Pilnas 6 eilutėje aprašyto modelio
pavadinimas bus `/datasets/gov/ivpk/adk/dataset`.

Visose vietose, kur naudojamas modelio pavadinimas, jei eilutė yra `dataset`
dimensijos sudėtyje, tada modelio pavadinimas bus jungiamas prie duomenų
rinkinio vardų erdvės, nebent modelio pavadinimas prasideda `/` simboliu.


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
papildomos metaduomenų dimensijos, kai nurodoma :term:`type` reikšmė ir
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


.. _duomenų-rinkinys:

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

    Viso duomenų rinkinio :term:`brandos lygis`. Paveldimas.

.. data:: dataset.access

    Viso duomenų rinkinio :term:`prieigos lygis`. Paveldimas.

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
:data:`base` pagalba ir turėtų priklausyti vienam :term:`duomenų rinkiniui
<duomenų rinkinys>`. Tą pačią semantinę prasmę turintys duomenys neturėtų būti
išskaidyti keliuose :term:`duomenų rinkiniuose <duomenų rinkinys>`.


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
Analogiškai kaip ir :data:`dataset:` atveju, :data:`resource.ref` stulpelyje
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

    .. describe:: wsdl

        WSDL servisas.

.. data:: resource.ref

    Duomenų šaltinio duomenų kataloge identifikatorius. Priklauso nuo
    dataset.type reikšmės.

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


Modelio bazė
------------

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

    Lentelių susiejimo tipas. Jei nenurodyta naudoti `alias`.

    Galimos reikšmės:

    .. describe:: extends

        Išplečia :data:`base` ir saugo tik tų :data:`property` duomenis, kurių
        neturi :data:`base`.

    .. describe:: partition

        Naudojama, kai reikia vieno modelio duomenis išskaidytus pagal datą ar
        vietą, sujungti į vieną bazę.

    .. describe:: alias

        Naudojama, kai tą pačią semantinę prasmę duomenys saugomi skirtingose
        vietose.

    .. describe:: proxy

        Naudojama tada, kai kelių modelių duomenys yra identiški vienam
        :data:`base`.

    Savybių matrica:

    =================  ========  =======  ========  =========
    \                  Savybės
    -----------------  --------------------------------------
    :data:`base.type`  Išplečia  Papildo  Perduoda  Dubliuoja
    =================  ========  =======  ========  =========
    `extends`          taip      ne       ne        ne
    `partition`        taip      taip     ne        taip
    `alias`            taip      ne       ne        taip
    `proxy`            ne        taip     taip      ne
    =================  ========  =======  ========  =========

    Išplečia
        :data:`model` gali turėti property eilučių, kurių neturi :data:`base.`

    Papildo
        :data:`model` gali papildyti :data:`base` naujais objektais, jei joks
        objektas neatitinka :data:`base.ref`.

    Perduoda
        :data:`model` duomenys perduodami į :data:`base`, pats :data:`model`
        duomenų nesaugo.

    Dubliuoja
        :data:`model` saugo kopiją :data:`property` reikšmių, kurios saugomos
        :data:`base`.

.. data:: base.ref

    :data:`model.property:data:` reikšmė, kurios pagalba :data:`model` objektai
    siejami su :data:`base` objektais. Jei susiejimas pagal vieną model property
    yra neįmanomas, galima nurodyti kelis :data:`model.property` pavadinimus
    atskirtus kableliu.

.. data:: base.level

    Baziniam modeliui priskirtų modelių :term:`brandos lygis`. Paveldimas.

.. data:: base.access

    Baziniam modeliui priskirtų modelių :term:`prieigos lygis`. Paveldimas.

Paaiškinimas, ką reiškia kiekviena savybė.


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

    Modeliui priklausančių laukų :term:`brandos lygis`. Paveldimas.

.. data:: model.access

    Modeliui priklausančių laukų :term:`prieigos lygis`. Paveldimas.

.. data:: model.uri

    Sąsaja su :term:`išoriniu žodynu`.

.. data:: model.title

    Modelio pavadinimas.

.. data:: model.description

    Modelio aprašymas.


Duomenų laukas
--------------

.. data:: property.source

    Duomenų lauko pavadinimas šaltinyje. Prasmė priklauso nuo
    :data:`resource.type`.

.. data:: property.prepare

    Formulė skirta duomenų tikrinimui ir transformavimui arba statinės reikšmės
    pateikimui.

.. data:: property.type

    Duomenų tipas. Galimos reikšmės:

    .. describe:: absent

        žymi savybė, kuri buvo ištrinta ir nebenaudojama.

    .. describe:: boolean

        Loginė reikšmė.

    .. describe:: integer

        Sveikas skaičius.

    .. describe:: number

        Realusis skaičius.

    .. describe:: string

        Simbolių eilutė.

    .. describe:: text

        Žmonių kalba užrašytas tekstas, nurodant kalbą naudojant `ISO 639-1`_
        kodus. Tekstas gali būti pateiktas keliomis kalbomis. Tekste gali būti
        naudojamos TEI_ žymės.

        .. _ISO 639-1: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
        .. _TEI: https://en.wikipedia.org/wiki/Text_Encoding_Initiative

    .. describe:: binary

        Dvejetainiai duomenys.

    .. describe:: date

        Data atitinkanti `ISO 8601`_.

        .. _ISO 8601: https://en.wikipedia.org/wiki/ISO_8601

    .. describe:: datetime

        Data ir laikas atitinkantis `ISO 8601`_.

    .. describe:: geometry

        Erdviniai duomenys. Duomenys pateikiami WKT_, WKB_ arba suderinamu
        formatu, kartu nurodant ir SRID_.

        .. _WKT: https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
        .. _WKB: https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary
        .. _SRID: https://en.wikipedia.org/wiki/Spatial_reference_system#Identifier

    .. describe:: currency

        Valiuta. Saugomas valiutos kiekis, nurodant tiek sumą, tiek valiutos
        kodą naudojant `ISO 4217`_ kodus.

        .. _ISO 4217: https://en.wikipedia.org/wiki/ISO_4217

    .. describe:: file

        Failas. Galimi failo metaduomenis:

        id
            Failo UUID.

        file_name
            Failo pavadinimas.

        content_type
            Failo media tipas.

        size
            Failo turinio dydis baitais.

        content
            Failo turinys.

    .. describe:: image

        Paveiksliukas. `image` tipas turi tokias pačias savybes kaip `file`
        tipas.

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

    .. describe:: temporal

        Apibrėžtis laike.

        Šis tipas atitinka `datetime`, tačiau nurodo, kad visas model yra
        apibrėžtas laike, būtent pagal šią savybę. Tik viena model savybė gali
        turėti `temporal` tipą. Pagal šios savybės reikšmes apskaičiuojamas ir
        įvertinamas `dct:temporal`_.

        .. _dct:temporal: https://www.w3.org/TR/vocab-dcat-2/#Property:dataset_temporal

    .. describe:: spatial

        Apibrėžtis erdvėje.

        Šis tipas atitinka `geometry`, tačiau nurodo, kad visas model yra
        apibrėžtas erdvėje, būtent pagal šią savybę.  Tik viena model savybė
        gali turėti `spatial` tipą. Pagal šios savybės reikšmes apskaičiuojamas ir
        įvertinamas `dct:spatial`_.

        .. _dct:spatial: https://www.w3.org/TR/vocab-dcat-2/#Property:dataset_spatial

    Papildomi tipai asmenį identifikuojantiems duomenų laukams.

    .. describe:: pii:name

        Asmens vardas ir/arba pavardė.

    .. describe:: pii:dob

        Asmens gimimo data.

    .. describe:: pii:phone

        Asmens telefonas.

    .. describe:: pii:email

        Asmens el. pašto adresas.

    .. describe:: pii:id

        Asmens kodas.

    .. describe:: pii:address

        Asmens gyvenamosios vietos telefonas.

    .. describe:: pii:age

        Asmens amžius.

.. data:: property.ref

    Šį lauką reikia pildyti `ref`, `backref` ir `generic` :data:`property.type`
    atvejais. Šiame stulpelyje reikia nurodyti :data:`model` pavadinimą, kas
    nurodo, kad lauko reikšmė rodo į kitą modelį. Žiūrėti Ryšiai tarp modelių.

.. data:: property.level

    Nurodo duomenų lauko brandos lygį. Žiūrėti Brandos lygiai.

.. data:: property.access

    Nurodo prieigos prie duomenų lygį. Žiūrėti skyrių Prieigos lygiai.

.. data:: property.uri

    Sąsaja su išoriniu žodynu.

.. data:: property.title

    Duomenų lauko pavadinimas.

.. data:: property.description

    Duomenų lauko aprašymas.


Ryšiai tarp modelių
===================

Ryšiai tarp modelių nurodomi `ref`, `backref` ir `generic` :data:`property.type`
pagalba. Pats ryšys pateikiamas :data:`property.ref` stulpelyje.
:data:`property.ref` stulpelyje ryšį su modeliu galima nurodyti tokiais būdais:

.. describe:: property.ref

    .. describe:: model

        `model` nurodo kito :data:`model` pavadinimą kurio :data:`model.ref`
        siejamas su :data:`property`.

        Jei :data:`model.ref` pirminiam raktui naudoja daugiau nei vieną lauką,
        tada :data:`property.source` laukas turi būti tuščias, o
        :data:`property.prepare` turi būti pateikiamos kableliu atskirtos
        property reikšmės, kurios bus naudojamos susiejimui.

    .. describe:: model[property]

        Tais atvejais, kai :data:`property` duomenys nesutampa su siejamo
        :data:`model.ref,` galima nurodyti :data:`property` iš :data:`model.`

    .. describe:: model[*property]

        Jei susiejimui reikia daugiau nei vieno duomenų lauko ir jie nesutampa
        su model.ref, tada galima nurodyti kelias property reikšmes atskirtas
        kableliu. Tačiau šiuo atveju taip pat būtina nurodyti ir
        :data:`property.prepare` kelias reikšmes atskirtas kableliu, o
        :data:`property.source` reikšmė turi būti tuščia.
        :data:`property.prepare` stulpelyje nurodomi kiti modelio
        :data:`property` pavadinimai iš kurių duomenų reikšmių turi būti
        formuojamas sudėtinis raktas.


.. _level:

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


.. _access:

Prieigos lygiai
===============

Duomenų prieigos lygis nurodomas :data:`access` stulpelyje.

.. describe:: access

    .. describe:: private

        **Vidiniam naudojimui**

        Duomenys skirti tik vidiniam konkrečios sistemos naudojimui.

    .. describe:: protected

        **Pakartotiniam naudojimui**

        Duomenys gali būti naudojami integracijai su išorinėmis sistemomis.

    .. describe:: public

        **Viešam naudojimui**

        Duomenys skirti viešam naudojimui, tačiau duomenų panaudojimo tikslai
        ribojami.

    .. describe:: open

        **Atviram naudojimui**

        Duomenys skirti viešam naudojimui, neribojant panaudojimo tikslo.


Viešam pakartotiniam naudojimui gali būti teikiami tik `public` ir `open`
prieigos lygio duomenys.

`public` duomenys gali būti teikiami tik autorizuotiems duomenų valdytojams,
kurie yra susipažinę ir sutinka su duomenų naudojimo taisyklėmis ir naudoja
duomenis tik `nurodytu tikslu`__ (*purpose limitation*), laikosi BDAR_
reikalavimų.
Asmens duomenys gali būti viešinami tik public ar žemesniu prieigos lygiu.

.. __: https://gdpr-info.eu/art-5-gdpr/
.. _BDAR: https://gdpr-info.eu/

`open` duomenys turėtu būti teikiami atvirai be jokios autorizacijos ir
neribojant duomenų naudojimo tikslo. Asmens duomenys negali būti teikiami `open`
prieigos lygiu.

Prieigos lygiai gali būti paveldimi iš aukštesneės dimensijos. Tačiau žemesnė
dimensija apsprendžia realų prieigos lygį. Pavyzdžiui jei :data:`dataset.access`
yra `private`, o toje :data:`dataset` dimensijoje esantis :data:`property` yra
`open`, tada visos to :data:`property` aukštesnės dimensijos taip pat tampa
`open`, nors visos kitos dimensijos yra `private`, nes paveldi
:data:`dataset.access` reikšmę.


.. _nuasmeninimas:

Nuasmeninimas
=============

Duomenų laukų reikšmių nuasmeninimas atliekamas :data:`property.prepare`
stulpelio pagalba.

.. function:: randomize(n)

    Reikšmės keičiamos parenkant atsitiktinę vertę ±\ `n` intervale nuo
    tikrosios vertės.

.. function:: permutate()

    Atsitiktine tvarka sumaišomos duomenų reikšmės.

.. function:: hash()

    Taikyti numatytą maišos funkciją.

.. function:: hash(name)

    Taikyti konkrečią `name` maišos funkciją.

.. function:: sample(n)

    Atsitiktine tvarka atrenkama `n` procentų žodžių naudojamų tekste.

.. function:: group(n)

    Pakeičia originalias reikšmes į intervalų grupes taip, kad į vieną intervalą
    patektų ne mažiau nei `n` reikšmių. Jei viena konkreti reikšmė pasikartoja
    daugiau nei `n` kartų, tada intervalas nekuriamas, reikšmė paliekama tokia
    kokia yra šaltinyje.


Struktūros pasikeitimai
=======================

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


Duomenų paruošimas
==================

.. _duomenų-bazės:

Duomenų bazės
-------------

Duomenų bazės URI formuojamas naudojant tokį ABNF_ šabloną:

.. _ABNF: https://en.wikipedia.org/wiki/Augmented_Backus–Naur_form

.. code-block:: abnf

    uri = type ["+" driver] "://"
          [user [":" password] "@"]
          host [":" port]
          "/" database ["?" params]

Šablone naudojamų kintamųjų aprašymas:

.. describe:: type

    Duomenų bazių serverio pavadinimas:

    .. describe:: sqlite

    .. describe:: postgresql

    .. describe:: mysql

    .. describe:: oracle

    .. describe:: mssql

.. describe:: driver

    Konkretaus duomenų bazių serverio tvarkyklė naudojama komunikacijai su
    duomenų baze.

.. describe:: user

    Naudotojo vardas jungimuisi prie duomenų bazės.

.. describe:: password

    Duomenų bazės naudotojo slaptažodis.

.. describe:: host

    Duomenų bazių serverio adresas.

.. describe:: port

    Duomenų bazių serverio prievadas.

.. describe:: database

    Konkrečios duomenų bazės pavadinimas.

.. describe:: params

    Papildomi parametrai Query string formatu.


.. _failai:

Failai
------

Dažnai duomenys teikiami failų pavidalu, kurie gali būti saugomi tiek lokaliai
failų sistemoje, tiek nuotoliniame serveryje. Failai gali būti suspausti ir
patalpinti į archyvo konteinerius. :term:`DSA` leidžia aprašyti įvairius
prieigos prie duomenų, saugomų failuose, atvejus.

.. describe:: resource.source

    Nutolusiame serveryje saugomo failo :term:`URI` arba kelias iki lokalaus
    katalogo. Lokalaus katalogo kelias gali būti pateikiamas tiek :term:`POSIX`,
    tiek :term:`DOS` formatais, priklausomai nuo to, kokioje operacinėje
    sistemoje failai saugomi.

.. describe:: resource.prepare

    .. function:: extract(resource, type)

        :arg resource: Kelias arba URI iki archyvo failo arba failo objektas.
        :arg type: Archyvo tipas.

        Išpakuoja archyvą, kuriame saugomi failai. Galimos `type` reikšmės:

        .. describe:: zip

        .. describe:: tar

        .. describe:: rar

        Funkcijos rezultatas yra archyvo objektas, kuris leidžia pasiekti
        esančius archyvo failus :func:`getitem` funkcijos pagalba.

    .. function:: decompress(resource, type)

        :arg resource: Kelias arba URI iki archyvo failo arba failo objektas.
        :arg type: Archyvo tipas.

        Taikomas srautinis failo glaudinimo filtras. Galimos `type` reikšmės:

        .. describe:: gz

        .. describe:: bz2

        .. describe:: xz

.. _stulpeliai-lentelėje:

Stulpeliai lentelėje
--------------------

CSV ar skaičiuoklių lentelėse stulpelių pavadinimai pateikiami pačioje
lentelėje. Eilutė, kurioje surašyti pavadinimai nebūtinai gali būti pirma.
Stulpelių pavadinimai gali būti pateikti keliose eilutėse iš kurių formuojamos
kompleksinės struktūros (žiūrėti :ref:`kompleksinės-struktūros`). Įvairias
situacijas galima aprašyti formulių pagalba.

.. describe:: model.prepare

    .. function:: header(*line)

        .. describe:: null

            Lentelėje eilučių pavadinimų nėra. Tokiu atveju,
            :data:`property.source` stulpelyje reikia pateikti stulpelio numerį,
            pradedant skaičiuoti nuo 0.

        .. describe:: line

            Nurodomas eilutės numeris, pradedant eilutes skaičiuoti nuo 0, kur
            yra pateikti lentelės stulpelių pavadinimai. Pagal nutylėjimą
            stulpelių pavadinimų ieškoma pirmoje eilutėje.

        .. describe:: *line

            Jei lentelė turi kompleksinę stulpelių struktūrą, tada galima
            pateikti daugiau nei vieną eilutės numerį iš kurių bus nustatomi
            stulpelių pavadinimai.

    .. function:: head(n)

        Praleisti `n` einančių po stulpelių pavadinimų eilutės.

    .. function:: tail(n)

        Ignoruoti `n` eilučių failo pabaigoje.

.. describe:: property.source

    Jei naudojamas :func:`header(null) <header>`, tada nurodomas stulpelio
    numeris, pradedant nuo 0.

    Jei naudojamas :func:`header(line) <header>`, tada nurodomas stulpelio
    pavadinimas, toks koks įrašytas lentelės line eilutėje.

    Jei naudojamas :func:`header(*line) <header>`, tada nurodomas stulpelio
    pavadinimas, toks koks įrašymas lentelės pirmajame line argumente.

.. describe:: property.prepare

    Jei naudojamas `header(*line)`, žiūrėti :ref:`kompleksinės-struktūros`.


.. _kompleksinės-struktūros:

Kompleksinės struktūros
-----------------------

Daugelis duomenų šaltiniu turi galimybę saugoti kompleksines struktūros. Jei
duomenys yra kompleksiniai, tada :data:`property.source` stulpelyje galima
nurodyti tik duomens pavadinimą iš pirmojo lygmens, gilesniuose lygmenyse
esančius duomenis galima aprašyti naudojant formules :data:`property.prepare`
stulpelyje.

Analogiškai duomenų atranką galima daryti ir model eilutėse, jei tai leidžia
duomenų šaltinis.

Kaip pavyzdį naudosime tokią :term:`JSON` duomenų struktūrą:

.. code-block:: json

    {
        "result": {
            "count": 1,
            "results": [
                {
                    "type": "dataset",
                    "tags": ["CSV"]
                }
            ]
        }
    }

.. describe:: property.prepare

    .. function:: getattr(object, name)

        Grąžina `object` savybe `name`.

        .. code-block:: python

            >>> self.result.count
            1

    .. function:: getitem(object, item)

        Grąžina `object` objekto `item` savybę arba `object` masyvo `item`
        elementą.

        .. code-block:: python

            >>> self["result"]["count"]
            1

        :func:`getitem` ir :func:`getattr` gali būti naudojami kartu.

        .. code-block:: python

            >>> self.result.results[0].type
            "dataset"

        :func:`getitem` gali būti naudojamas, kaip masyvo elementų filtras
        pateikiant filtro sąlygą.

        .. code-block:: python

            >>> self.result.results[tags = "CSV"].type
            ["dataset"]

            >>> self.result.results[item(tags) = "CSV"].type
            ["dataset"]

        Norint gauti visus masyvo elementus, galima naudoti tokią išraišką:

        .. code-block:: python

            >>> self.result.results[].tags[]
            ["CSV"]

Analogiška struktūra gali būti gaunama ir lentelėse, kai stulpelių pavadinimai
nurodyti keliose eilutėse, pavyzdyje pateiktą struktūrą atitiktų tokia lentelė:

======  =======  ====
result
count   results
\       type     tags
======  =======  ====
1       dataset  CSV
======  =======  ====


Šioje lentelėje stulpelių pavadinimai pateikti trijose eilutėse, todėl
model.prepare reikėtų naudoti :func:`header(0, 1, 2) <header>`.


.. _duomenų-atranka:

Duomenų atranka
===============

Duomenų filtravimui naudojamas model.prepare stulpelis, kuriame galima naudoti tokius filtrus:

.. describe:: model.prepare

    .. describe:: a = b

        `a` ir `b` reikšmės yra lygios.

    .. describe:: a != b

        `a` nelygu `b`.

    .. describe:: a > b

        `a` daugiau už `b`.

    .. describe:: a < b

        `a` mažiau už `b`.

    .. describe:: a >= b

        `a` daugiau arba lygu `b`.

    .. describe:: a <= b

        `a` mažiau arba lygu `b`.

    .. describe:: a.in(b)

        `a` lygi bent vienai iš `b` sekos reikšmių.

    .. describe:: a.notin(b)

        `a` nelygi nei vienai iš `b` sekos reikšmių.

    .. describe:: a.contains(b)

        `a` seka savyje turi `b` seką.

    .. describe:: a.startswith(b)

        `a` seka prasideda `b` seka.

    .. describe:: a.endswith(b)

        `a` seka baigiasi `b` seka.

    .. describe:: a & b

        `a` ir `b`.

    .. describe:: a | b

        `a` arba `b`.

    .. describe:: sort(+a, -b)

        Rūšiuoti didėjimo tvarka  pagal `a` ir mažėjimo tvarka pagal `b`.


Periodiškumas
=============

Periodiškumui nurodyti naudojamas model.prepare stulpelis, kuriame galima
naudoti tokias formules:

.. describe:: model.prepare

    .. function:: cron(line)

        Duomenų atnaujinimo laikas, analogiškas `cron
        <https://en.wikipedia.org/wiki/Cron>`_ formatui.

        `line` argumentas aprašomas taip:

        `n`\ m
            `n`-toji minutė, `n` ∊ 0-59.

        `n`\ h
            `n`-toji valanda, `n` ∊ 0-23.

        `n`\ d
            `n`-toji mėnesio diena, `n` ∊ 1-31.

        $d
            Paskutinė mėnesio diena.

        `n`\ M
            `n`-tasis mėnuo, `n` ∊ 1-12.

        `n`\ w
            `n`-toji savaitės diena, `n` ∊ 0-6 (sekmadienis-šeštadienis).

        `n`\ #\ `i`\ w
            `n`-toji savaitės diena, `i`-toji mėnesio savaitė, `i` ∊ 1-6.

        `n`\ $\ `i`\ w
            `n`-toji savaitės diena, `i`-toji savaitė nuo mėnesio galo, `i`
            ∊ 1-6.

        ,
            Kableliu galim atskirt kelias laiko vertes.

        \-
            Brūkšneliu galima atskirti laiko verčių intervalą.

        /
            Pasvyruoju brūkšniu galima atskirti laiko verčių kartojimo
            žingsnį.

        Laiko vertės atskiriamos tarpo simbolių. Jei laiko vertė nenurodyta,
        reiškia įeina visos įmanomos laiko vertės reikšmės.

    .. function:: hourly()

        :func:`cron('0m') <cron>`

    .. function:: daily()

        :func:`cron('0m 0d') <cron>`

    .. function:: weekly()

        :func:`cron('0m 0h 0w') <cron>`

    .. function:: monthly()

        :func:`cron('0m 0h 1d') <cron>`

    .. function:: yearly()

        :func:`cron('0m 0h 1d 1M') <cron>`


Statinės reikšmės
=================

Statinės reikšmės arba konstantos duomenų laukams gali būti nurodomos
:data:`property.prepare` stulpelyje naudojant formulės sintaksę. Plačiau apie
formules žiūrėti :ref:`formulas` skyrelyje.


Fiksuotų reikšmių variantai
===========================

Tam tikri duomenų laukai turi fiksuotą reikšmių variantų aibę. Dažnai duomenų
bazėse fiksuotos reikšmės saugomos skaitine forma ar kitais kodiniais
pavadinimais. Tokias fiksuotas reikšmes duomenų struktūros apraše galima
pateikti neužpildant hierarchinių stulpelių ir nurodant type reikšmę choice.

.. data:: choice

    .. data:: choice.source

        Pateikiama originali reikšmė, taip kaip ji saugoma duomenų šaltinyje.

    .. data:: choice.prepare

        Pateikiama reikšmė, tokia kuri bus naudojama atveriant duomenis.
        :data:`model.prepare` filtruose taip pat bus naudojama būtent ši
        reikšmė.

    .. data:: choice.ref

        Pasirinkimų sąrašo pavadinimas, kuris gali būti naudojamas kaip trečias
        :func:`choose` argumentas.

    .. data:: choice.title

        Fiksuotos reikšmės pavadinimas.

    .. data:: choice.description

        Fiksuotos reikšmės aprašymas.

Pagal nutylėjimą, jei :data:`property.prepare` yra tuščias ir :data:`property`
turi :data:`choice` sąrašą, tada jei šaltinis turi neaprašytą reikšmę, turėtų
būti fiksuojama klaida.

Jei yra poreikis fiksuoti tik tam tikras reikšmes, o visas kitas palikti tokias,
kokios yra šaltinyje, tada :data:`property.prepare` stulpelyje reikia įrašyti
`self.choose(self)`.


Dinaminių reikšmių variantai
============================

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
============

Dirbant su :term:`DSA` yra galimybė komentuoti eilutes, naudojant papildomą
:data:`comment` dimensiją, kurią galima naudoti bet kurios kitos dimensijos
kontekste.

.. data:: comment

    .. data:: comment.id

        Komentaro numeris.

    .. data:: comment.title

        Komentaro antraštė, nebūtina.

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


Transformavimas
===============

:data:`property.prepare` stulpelyje gauta šaltinio reikšmė gali būti pasiekiama
per self kintamąjį.

:data:`property.prepare` formulėje gali būti aprašomos kelios reikšmės atskirtos
kableliu, tai naudojama ryšio laukams, kai ryšiui aprašyti reikia daugiau nei
vieno duomenų lauko.

Formulėje galima naudoti kitus to pačio modelio property pavadinimus, kai
aprašomo :data:`property` reikšmės formuojamos dinamiškai naudojant viena ar
kelis jau aprašytus laukus.

:data:`property.prepare` stulpelyje galima naudoti tokias formules:

.. describe:: property.prepare

    .. function:: null()

        Grąžina `null` reikšmę, jei toliau einančios transformacijos grąžina
        `null`.

    .. function:: replace(old, new)

        Pakeičia visus `old` į `new` simbolių eilutėje.

    .. function:: re(pattern)

        Grąžina atitinkančią reguliariosios išraiškos `pattern` reikšmę arba
        pirmos grupės reikšmę jei naudojama tik viena grupė arba reikšmių grupę
        jei `pattern` yra daugiau nei viena grupė.

    .. function:: cast(type)

        Konvertuoja šaltinio tipą į nurodytą `type` tipą. Tipų konvertavimas yra
        įmanomas tik tam tikrais atvejais. Jei tipų konvertuoti neįmanoma, tada
        metodas turėtų grąžinti klaidą.

    .. function:: split()

        Dalina simbolių eilutę naudojant `\s+` :term:`reguliariąją išraišką
        <reguliarioji išraiška>`. Grąžina masyvą.

    .. function:: strip()

        Pašalina tarpo simbolius iš pradžios ir pabaigos.

    .. function:: lower()

        Verčia visas raides mažosiomis.

    .. function:: upper()

        Verčia visas raides didžiosiomis.

    .. function:: len()

        Grąžina elementų skaičių sekoje.

    .. function:: choose(default)

        Jei šaltinio reikšmė nėra viena iš :data:`property.choice`, tada
        grąžinama default reikšmė.

        Jei default nupateiktas, grąžina vieną iš :data:`property.choice`
        reikšmių, jei duomenų šaltinio reikšmė nėra viena iš
        :data:`property.choice`, tada grąžinama klaida.

    .. function:: switch(*cases)
    .. function:: case(cond, value)
    .. function:: case(default)

        Grąžina `value`, jei tenkina `cond` arba `default`. Jei `case(default)`
        nepateiktas, tada grąžina pradinę reikšmę.

        Jei, `cases` nepateikti, grąžina vieną iš :data:`switch.source`
        reikšmių, tenkinančių switch prepare sąlygą.

    .. function:: return()

        Nutraukia transformacijų grandinę ir grąžina reikšmę.

    .. function:: set(name)

        Išsaugo reikšmę į kintamąjį `name`.

    .. function:: url()

        Skaido URI į objektas turintį tokias savybes:

        scheme
            URI schema.

        netloc
            Visada URI dalis tarp scheme ir path.

        username
            Naudotojo vardas.

        password
            Slaptažodis.

        host
            Domeno vardas arba IP adresas.

        port
            Prievado numeris.

        path
            Kelias.

        query
            URL dalis einanti tarp `?` ir `#`.

        fragment
            URL dalis einanti po #.

    .. function:: query()

        Skaido URI query dalį į parametrus.

    .. function:: path()

        Skaido failų sistemos arba URI kelią į tokias savybes:

        parts
            Skaido kelią į dalis (plačiau__).

            .. __: https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parts

        drive
            Diskas (plačiau__).

            .. __: https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.drive

        root
            Šaknis (plačiau__).

            .. __: https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.root


Duomenų šaltiniai
=================

.. _resource-type-sql:

SQL
---

.. describe:: resource.source

    Duomenų bazės URI, žiūrėti :ref:`duomenų-bazės`.

.. describe:: resource.prepare

    Formulė skirta papildomiems veiksmams reikalingiems ryšiui su duomenų baze
    užmezgimui ir duomenų bazės paruošimui, kad būtų galima skaityt duomenis.

.. describe:: resource.type

    Galimos reikšmės: `sql`.

.. describe:: resource.prepare

    .. function:: schema(name)

        Naudojama tais atvejais, kai reikia aktyvuoti tam tikrą duomenų bazės
        schemą.

.. describe:: model.source

    Duomenų bazėje esančios lentelės pavadinimas.

.. describe:: property.source

    Lentelės stulpelio pavadinimas.


CSV
---

.. describe:: resource.type

    Galimos reikšmės: `csv`, `tsv`.

.. describe:: resource.source

    Žiūrėti Failai.

.. describe:: resource.prepare

    .. function:: sep(separator)

        Nurodoma kaip CSV faile atskirti stulpeliai. Pagal nutylėjimą
        `separator` reikšmė yra `,`.

.. describe:: model.source

    Nenaudojama, kadangi CSV resursas gali turėti tik vieną lentelę.

.. describe:: model.prepare

    Žiūrėti :ref:`stulpeliai-lentelėje`.

.. describe:: property.source

    Žiūrėti :ref:`stulpeliai-lentelėje`.


JSON
----

.. describe:: resource.type

    Galimos reikšmės: `json`, `jsonl`.

.. describe:: resource.source

    Žiūrėti :ref:`failai`.

.. describe:: model.source

    JSON objekto savybės pavadinimas, kuri rodo į masyvą reikšmių, kurios bus
    naudojamos kaip modelio duomenų eilutės. Kiekvienas masyvo elementas
    atskirai aprašomas :data:`property` dimensijoje. Jei JSON objektas yra
    kompleksinis žiūrėti :ref:`kompleksinės-struktūros`.

.. describe:: property.source

    JSON objekto savybė, kurioje pateikiami aprašomo stulpelio duomenys.

.. describe:: property.prepare

    Žiūrėti :ref:`kompleksinės-struktūros`.


XML
---

.. describe:: resource.type

    Galimos reikšmės: `xml`, `html`.

.. describe:: resource.source

    Žiūrėti :ref:`failai`.

.. describe:: model.source

    `XPath <https://en.wikipedia.org/wiki/XPath>`_ iki elementų sąrašo kuriame
    yra modelio duomenys.

.. describe:: model.prepare

    Jei neužpildyta, vykdoma :func:`xpath(self) <xpath>` funkcija.

    .. function:: xpath(expr)

        Vykdo nurodyta `expr`, viso XML dokumento kontekste.

.. describe:: property.source

    `XPath <https://en.wikipedia.org/wiki/XPath>`_ iki elemento kuriame yra
    duomenys.

.. describe:: model.prepare

    Jei neužpildyta, vykdoma :func:`xpath(self) <xpath>` funkcija, iš
    :data:`model` gauto elemento kontekste.


Skaičiuoklių lentelės
---------------------

.. describe:: resource.type

    Galimos reikšmės: `xlsx`, `xls` arba `odt`.

.. describe:: resource.source

    Žiūrėti :ref:`failai`.

.. describe:: model.source

    Skaičiuoklės faile esančio lapo pavadinimas.

.. describe:: model.prepare

    Žiūrėti :ref:`stulpeliai-lentelėje`.

.. describe:: property.source

    Žiūrėti :ref:`stulpeliai-lentelėje`.


WSDL
----

.. describe:: resource.type

    Galima reikšmė: `wsdl`.

.. describe:: resource.source

    WSDL URI.

.. describe:: model.source

    Nenaudojamas.

.. describe:: model.prepare

    .. function:: service(name, *args, **kwargs)

        WSDL funkcijos `name` iškvietimas.

    .. function:: wsdl(type, **kwargs)

        Inicializuoja nurodytą `type` WSDL tipą.

.. describe:: property.source

    Rezultato objekto atributas.

.. describe:: property.prepare

    Žiūrėti :ref:`kompleksinės-struktūros`.


.. _parametrizacija:

Parametrizacija
===============

Parametrai leidžia iškelti tam tikras duomenų paruošimo operacijas į parametrus
kurie gali būti naudojami :term:`dimensijos`, kurioje apibrėžtas parametras
kontekste. Parametrai gali gražinti :term:`iteratorius`, kurių pagalba galima
dinamiškai kartoti :data:`resource` duomenų skaitymą, panaudojant aprašytus
parametrus. Taip pat parametrų pagalba galima sudaryti reikšmių sąrašus, kurių
pagalba galima kartoti :data:`resource` su kiekviena reikšme.

Parametrai dažniausiai naudojami žemesnio brandos lygio duomenų šaltiniams
aprašyti, o taip pat API atvejais, kai duomenys atiduodame dinamiškai.

Parametrai aprašomi pasitelkiant papildomą :data:`param` dimensiją.

.. data:: param

    .. data:: param.ref

        Parametro :term:`kodinis pavadinimas`.

    .. data:: param.prepare

        Formulė, kuri grąžina sąrašą reikšmių aprašomam parametrui. Jei
        nepateikta, naudojamas `self`.

    .. data:: param.source

        Nurodoma reikšmė, kuri :data:`param.prepare` pateikiama kaip `self`
        kintamasis.

Jei parametro reikšmė yra :term:`iteratorius`, tada :data:`dimensija`, kurio
:term:`kontekste <dimensijos kontekstas>` yra aprašytas :ref:`parametras
<param>` yra kartojama tiek kartų, kiek reikšmių grąžina :term:`iteratorius`.

Jei yra keli :data:`param` grąžinantys :term:`iteratorius`, tada iš
visų :term:`iteratorių <iteratorius>` sudaroma `Dekarto sandauga`_ ir
:data:`resource` dimensija vykdoma su kiekviena sandaugos rezultato reikšme.

.. _Dekarto sandauga: https://lt.wikipedia.org/wiki/Dekarto_sandauga

Nepriklausomai kurioje :term:`dimensijoje` panaudoti :data:`param`, grąžinantys
iteratorius, visada kartojama visa :data:`resource` :term:`dimensija`.

Jei sekančioje :term:`DSA` eilutėje, einančioje po eilutės, kurioje aprašytas
:data:`param`, nenurodytas :data:`type` ir neužpildytas joks kitas
:term:`dimensijos <dimensija>` stulpelis, tada parametras tampa
:term:`iteratoriumi <iteratorius>`, kurio reikšmių sąrašą sudaro sekančiose
eilutėse patektos :data:`source` ir :data:`prepare` reikšmės.

:data:`param` reikšmės pasiekiamos naudojanti pavadinimą įrašytą :data:`pram
ref` stulpelyje. Pavyzdžiui, jei :data:`pram.ref` stulpelyje įrašyta `x`, tada
`x` parametro reikšmę galima gauti taip:

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


Sąsaja su išoriniais žodynais
=============================

Sąsają su išoriniais žodynais galima pateikti :data:`model.uri` ir
:data:`property.uri` stulpeliuose. Tačiau prieš naudojant žodynus, pirmiausia
reikia apsirašyti žodynų prefiksus. Žodynų prefiksai aprašomi taip:

.. data:: prefix

    .. data:: prefix.ref

        Prefikso pavadinimas.

    .. data:: prefix.uri

        Žodyno URI prefiksas.

    .. data:: prefix.title

        Prefikso antraštė.

    .. data:: prefix.description

        Prefikso aprašymas.

Rekomenduojama naudoti LOV_ prefiksus.

.. _LOV: https://lov.linkeddata.es/dataset/lov/

Aprašyti prefiksai gali būti naudojami :data:`model.uri` ir :data:`property.uri`
stulpeliuose tokiu būdu: `prefix:name`.


.. |id| replace:: :data:`id`
.. |d| replace:: :data:`d <dataset>`
.. |r| replace:: :data:`r <resource>`
.. |b| replace:: :data:`b <base>`
.. |m| replace:: :data:`m <model>`
.. |property| replace:: :data:`property`
.. |title| replace:: :data:`title`
.. |type| replace:: :data:`type`
.. |ref| replace:: :data:`ref`
.. |uri| replace:: :data:`uri`

