.. default-role:: literal

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

    Kodinis duomenų rinkinio pavadinimas. Atitinka `dcat:Dataset`_ prasmę.
    Žiūrėti :ref:`duomenų-rinkinys`.

    .. _dcat:Dataset: https://www.w3.org/TR/vocab-dcat-2/#Class:Dataset

.. data:: resource

    **Duomenų šaltinis**

    Kodinis duomenų šaltinio pavadinimas. Atitinka `dcat:Distribution`_ prasmę.
    Žiūrėti :ref:`duomenų-šaltinis`.

    .. _dcat:Distribution: https://www.w3.org/TR/vocab-dcat-2/#Class:Distribution

.. data:: base

    **Modelio bazė**

    Kodinis bazinio modelio pavadinimas. Atitinka `rdfs:subClassOf`_ prasmę
    (:data:`model` `rdfs:subClassOf` :data:`base`). Žiūrėti :ref:`modelio-bazė`.

    .. _rdfs:subClassOf: https://www.w3.org/TR/rdf-schema/#ch_subclassof

.. data:: model

    **Modelis (lentelė)**

    Kodinis modelio pavadinimas. Atitinka `rdfs:Class`_ prasmę. Žiūrėti
    :ref:`duomenų-modelis`.

    .. _rdfs:Class: https://www.w3.org/TR/rdf-schema/#ch_class

.. data:: property

    **Savybė (stulpelis)**

    Kodinis savybės pavadinimas. Atitinka `rdfs:Property`_ prasmę. Žiūrėti
    :ref:`savybė`.

    .. _rdfs:Property: https://www.w3.org/TR/rdf-schema/#ch_property

.. data:: type

    **Tipas**

    Prasmė priklauso nuo dimensijos. Žiūrėti :ref:`duomenų-tipai`.

.. data:: ref

    **Ryšys**

    Prasmė priklauso nuo dimensijos. Žiūrėti :ref:`ryšiai`.

.. data:: source

    **Šaltinis**

    Duomenų šaltinio struktūros elementai. Žiūrėti :ref:`duomenų-šaltiniai`.

.. data:: prepare

    **Formulė**

    Formulė skirta duomenų atrankai, nuasmeninimui, transformavimui, tikrinimui
    ir pan. Žiūrėti :ref:`formulės`.

.. data:: level

    **Brandos lygis**

    Duomenų brandos lygis, atitinka `5 Star Data`_. Žiūrėti
    :ref:`brandos-lygiai`.

    .. _5 Star Data: https://5stardata.info/en/

.. data:: access

    **Prieiga**

    Duomenų prieigos lygis. Žiūrėti :ref:`prieigos-lygiai`.

.. data:: uri

    **Žodyno atitikmuo**

    Sąsaja su išoriniu žodynu. Žiūrėti :ref:`išoriniai-žodynai`.

.. data:: title

    **Pavadinimas**

    Elemento pavadinimas.

.. data:: description

    **Aprašymas**

    Elemento aprašymas. Galima naudoti Markdown_ sintaksę.

    .. _Markdown: https://en.wikipedia.org/wiki/Markdown

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


.. _kodiniai-pavadinimai:

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

+-------+-----+-----+-----+-----+--------------+
| id    | d   | r   | b   | m   | property     |
+=======+=====+=====+=====+=====+==============+
| **0** |     |     |     | ****dcat/dataset** |
+-------+-----+-----+-----+-----+--------------+
|     1 |     |     |     |     | title        |
+-------+-----+-----+-----+-----+--------------+
| **2** | **datasets/gov/ivpk/adk**            |
+-------+-----+-----+-----+-----+--------------+
|     3 |     | adk                            |
+-------+-----+-----+-----+-----+--------------+
|     4 |     |     | **/dcat/dataset**        |
+-------+-----+-----+-----+-----+--------------+
| **5** |     |     |     | **dataset**        |
+-------+-----+-----+-----+-----+--------------+
|     6 |     |     |     |     | title        |
+-------+-----+-----+-----+-----+--------------+

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

Toliau 4 eilutėje nurodyta modelio bazė `/dcat/dataset`. Kadangi modelio bazės
pavadinimas prasideda `/` simboliu, tai modelio pavadinimas nesiejamas su
duomenų rinkinio vardų erdve ir rodo į pirmoje eilutėje apibrėžtą modelį.

5 eilutėje pateiktas modelio pavadinimas `dataset` neturi priekyje `/`, todėl
yra siejamas su duomenų rinkinio vardų erdve. Pilnas 5 eilutėje aprašyto modelio
pavadinimas bus `/datasets/gov/ivpk/adk/dataset`.

Visose vietose, kur naudojamas modelio pavadinimas, jei eilutė yra `dataset`
dimensijos sudėtyje, tada modelio pavadinimas bus jungiamas prie duomenų
rinkinio vardų erdvės, nebent modelio pavadinimas prasideda `/` simboliu.
