.. default-role:: literal

.. _saugykla:

Saugykla
########

Atvirų duomenų Saugykla yra sudedamoji atvirų duomenų Portalo dalis. Saugyklos
paskirtis yra duomenų publikavimas :ref:`aukščiausiu brandos lygiu <level>`,
įvairiais formatais, per patogią mašininio duomenų skaitymo sąsają
(:term:`API`), laikantis aukščiausių duomenų publikavimo standartų.

Visi duomenų rinkiniai publikuojami Saugykloje yra apjungiami į vieną didelę
duomenų bazę, kur duomenys gali būti jungiami tarpusavyje, pateikiami pilna
apimtimi (angl. *in bulk*) arba pageidaujamais pjūviais. Suteikiamos
priemonės duomenis gauti palaipsniniu būdu (angl. `Incremental download`_).

.. _Incremental download: https://en.wikipedia.org/wiki/Incremental_computing


Statusas ir planas
==================

Priemonė „Spinta“ yra eksperimentinis projektas, šiuo metu aktyviai vystomas.
Pagal `programinės įrangos gyvavimo ciklo schema`__, „Spinta“ yra PRE-ALPHA
etape.

__ https://en.wikipedia.org/wiki/Software_release_life_cycle

Nors projektas yra aktyviai vystomas, tačiau jis jau yra naudojamas
gamybinėje aplinkoje, kurią galite pasiekti šiais adresais:

https://get.data.gov.lt/
    Saugyklos sritis skirta viešai atvirų duomenų prieigai. Ši sritis veikia
    tik skaitymo režimu ir skirta plačiajai visuomenės daliai.

https://put.data.gov.lt/
    Saugyklos sritis skirta duomenų tiekėjams, kuriems suteikiama galimybė
    teikti duomenis į saugyklą. Ši sritis yra skirta tik duomenų tiekėjams.

.. _saugyklos-testinė-aplinka:

Taip pat yra analogiškos aplinkos skirtos testavimui, prieš pereinant prie
gamybinės aplinkos:

https://get-test.data.gov.lt/

https://put-test.data.gov.lt/

Kiekvienas pakeitimas projekto „Spinta“ kodo bazėje yra automatiškai
testuojamas vykdant beveik 1000 testų, kurie dengia beveik 90% viso kodo.
Todėl projektas yra gan stabilus.


Preliminarus projekto vystymo planas
------------------------------------

==============  =================  =================
Etapas          Pradžia            Pabaiga
--------------  -----------------  -----------------
PRE-ALPHA       2019 metų pradžia  2021 metų pabaiga
ALPHA           2021 metų pabaiga  2022 metų vidurys
BETA            2022 metų vidurys  2023 metų kovas
STABLE          2023 metų kovas    -
==============  =================  =================


Ko tikėtis kiekvieno etapo metu?
--------------------------------

PRE-ALPHA (iki 2021 metų pabaigos)
    Projektas jau bus naudojamas gamybinėje aplinkoje, tačiau reikėtu tikėtis,
    kad dalykai ne visada veiks, funkcijos bus ne iki galo išbaigtos ir esamas
    funkcionalumas gali keistis. Tačiau nepaisant minėtu trūkumų, esminės atvirų
    duomenų saugyklos funkcijos turėtu veikti gan stabiliai, todėl
    rekomenduojame aktyviai naudotis saugykla tiek teikiant, tiek gaunant
    duomenis, nes tik tokiu būdu geriau suprasime ko reikia galutiniam
    naudotojui.

    Jei į saugyklą teikiate svarbius, didelę paklausą turinčius duomenis,
    rekomenduojame „Spinta“ projektą naudoti tik, kaip alternatyvią duomenų
    publikavimo priemonę, kartu publikuojant duomenis ir kitais kanalais,
    užtikrinančiais didesnį patikimumo lygį.

ALPHA (iki 2022 metų vidurio)
    Šio etapo metu didžiausias dėmesys bus skiriamas esamų funkcijų išbaigtumo
    didinimui, greitaveikos optimizavimui ir stabilumo didinimui. Šio etapo
    metu.

    Taip pat šio etapo metu bus dirbama ir prie duomenų brandos kėlimo funkcijų
    įgyvendinimo, peržiūrint visus saugykloje publikuojamus duomenis ir siekiant
    juos transformuoti taip, kad jie būtų suderinami su Europos ir
    tarptautiniais standartais, kiek įmanoma atitiktų vieningą duomenų žodyną.

BETA (iki 2023 metų kovo mėnesio)
    Šio etapo metu, jokių naujų funkcijų kurti nebeplanuojama, bus didinamas
    esamų funkcijų stabilumas, greitaveika, taisomos pastebėtos klaidos.

    Šio etapo metu rekomenduojame naudoti saugyklą, kaip pagrindinį atvirų
    duomenų publikavimo šaltinį.

STABLE (nuo 2023 metų kovo mėnesio)
    Šio etapo metu, bus vykdomas projekto palaikymas ir priežiūra, pastebėtų
    klaidų taisymas.


Prieš pradedant
===============

Pavyzdžių skaitymas
-------------------

Prieš pradedant skaityti verta susipažinti kokie įrankiai naudojami šios
dokumentacijos pavyzdžiuose.

Pavyzdžiuose HTTP užklausos atliekamos naudojant patogią httpie_ programėlę.

.. _httpie: https://httpie.io/

Pavyzdžiui::

    http /version

.. code-block:: http

    HTTP/1.1 200 OK
    content-type: application/json

    {
        "api": {
            "version": "0.0.1"
        },
        "build": null,
        "implementation": {
            "name": "Spinta",
            "version": "0.1.6"
        }
    }

Šiame pavyzdyje `http` komanda buvo įvykdyta su `/version` argumentu.

Pavyzdžiuose nepateikiamas konkretus domenas, kadangi domenas gali skirtis
priklausomai nuo to, kurią atvirų duomenų saugyklą naudojate, tačiau adreso
dalis einanti po domeno visada vienoda.

Apart to, kad pavyzdžiuose nenurodomas domenas, visa kita veikia taip kaip
parašyta httpie_ dokumentacijoje. Todėl rekomenduojame pirmiausia
pasiskaityti su httpie_ dokumentacija, prieš pradedant gilintis į šią atvirų
duomenų saugyklos dokumentaciją.


Duomenų modelis
---------------

Visuose pavyzdžiuose bus naudojamas vienas ir tas pats žemynų, šalių ir miestų
duomenų modelis, kurios struktūra atrodo taip:

+---+---+-------------+---------+-----------+
| d | m | property    | type    | ref       |
+===+===+=============+=========+===========+
| datasets/gov/dc/geo |         |           |
+---+---+-------------+---------+-----------+
|   | Continent       |         |           |
+---+---+-------------+---------+-----------+
|   |   | name        | string  |           |
+---+---+-------------+---------+-----------+
|   | Country         |         |           |
+---+---+-------------+---------+-----------+
|   |   | code        | string  |           |
+---+---+-------------+---------+-----------+
|   |   | name        | string  |           |
+---+---+-------------+---------+-----------+
|   |   | continent   | ref     | continent |
+---+---+-------------+---------+-----------+
|   |   | capital     | ref     | city      |
+---+---+-------------+---------+-----------+
|   | City            |         |           |
+---+---+-------------+---------+-----------+
|   |   | name        | string  |           |
+---+---+-------------+---------+-----------+
|   |   | country     | ref     | country   |
+---+---+-------------+---------+-----------+

Šalys priklauso žemynams, o miestai šalims. Kiekviena šalis turi vieną miestą
sostinę.


API adreso struktūra
====================

API yra generuojamas dinamiškai iš :term:`DSA` `model` stulpelyje esančių
modelio :term:`kodinių pavadinimų <kodinis pavadinimas>`. Modelių pavadinimai
gali turėti vardų erdves, vardų erdvės yra atskirtos `/` simboliu, pavyzdžiui::

    /datasets/gov/dc/geo/Continent

Šis adresas sudarytas iš `datasets/gov/dc/geo` vardų erdvės ir `Continent`
modelio pavadinimo.

`datasets` vardų erdvė rodo, kad duomenys yra žali, t.y. tokie kokie pateikti
tam tikros įstaigos. Su laiku visų įstaigų duomenys bus transformuoti į vieningą
šalies masto žodyną ir pavyzdžiui `datasets/gov/dc/geo/Continent` gali būti
sulietas į vieną bendrą `Continent` modelį, šakninėje vardų erdvėje. Tačiau
užtikrinant stabilų ir nekintantį API bus paliekami ir pradiniai žalių duomenų
API taškai.

Konkrečiai visi `datasets` vardų erdvėje esantys modeliai turi aiškiai apibrėžtą
struktūrą, pavyzdžiui nagrinėjant `datasets/gov/dc/geo/Continent` pavyzdį
atskirų kelio komponentų prasmės būdų tokios:

- `datasets/` - vardų erdvė skirta žaliems pirminiams įstaigų duomenimis.
- `gov/` - vardų erdvė skirta valstybinių įstaigų duomenimis.
- `dc/` - konkrečios valstybinės įstaigos trumpinys.
- `geo/` - įstaigos atverto duomenų rinkinio trumpinys.
- `Continent` - duomenų modelis (arba lentelė).


Adreso parametrai
-----------------

Adresas gali turėti parametrus, parametrai atrodo taip::

    /:ns
    /:changes
    /:format/csv

Jei adreso kelio elementas prasideda `:` simboliu, tai po jo seka parametro
pavadinimas ir jei konkretus parametras turi argument, gali sekti vienas ar
daugiau argumentų.


Identifikatorius
----------------

Identifikatorius pat yra adreso parametras, tik jis neprasideda `:` simboliu, o
eina iš karto po modelio pavadinimo ir tai turi būti UUID simbolių eilutė,
pavyzdžiui::

    /datasets/gov/dc/geo/Continent/77e0bb52-f8ae-448f-b4c2-7de6bb150ff0

Identifikatorius taip pat gali turėti argumentus, identifikatoriaus
argumentai yra modelio savybė, pavyzdžiui::

    /datasets/gov/dc/geo/City/7d473db2-d363-4318-9b84-138eb5d70f70/continent

Tokiu būdu yra galimybė gauti tik konkrečios modelio savybės duomenis.


Užklausa
--------

URL Query dalyje, po `?` simbolio galima pateikti papildomus užklausos
parametrus, pavyzdžiui::

    /datasets/gov/dc/geo/Continent?select(name)&sort(name)


Rezervuoti pavadinimai
----------------------

Įvairiose API vietose, įskaitant ir adreso struktūrą naudojami rezervuoti
pavadinimai, kurie prasideda simboliu `_`.


Vardų erdvės
============

Atvirų duomenų saugykla yra didelis katalogas, kuriame sudėta įvairių modelių
duomenys. Katalogai vadinami vardų erdvėmis.

Aukščiausiame lygyje yra globali vardų erdvė::

    http /

.. code-block:: http

    HTTP/1.1 200 OK
    content-type: application/json

    {
        "_data": [
            {
                "_id": "datasets/:ns",
                "_type": "ns",
                "title": "datasets"
            }
        ]
    }


Globalioje vardų erdvėje yra kita vardų erdvė `datasets`. Žinome, kad `datasets`
yra vardų erdvė, kadangi tai nurodyta `_type` savybėje, kurios reikšmė `ns`, kas
reiškia *Name Space* arba *Vardų Erdvė* išvertus į Lietuvių kalbą.

Į vardu erdves reikia kreiptis nurodant `/:ns` parametrą::

    http /datasets/gov/dc/geo/:ns

.. code-block:: http

    HTTP/1.1 200 OK
    content-type: application/json

    {
        "_data": [
            {
                "_id": "datasets/gov/dc/geo/Continent",
                "_type": "model",
                "title": "Continent"
            },
            {
                "_id": "datasets/gov/dc/geo/Country",
                "_type": "model",
                "title": "Country"
            },
            {
                "_id": "datasets/gov/dc/geo/City",
                "_type": "model",
                "title": "City"
            }
        ]
    }

Jei `/:ns` parametras nebūtų nurodytas, tada saugykla bandytų ieškoti modelio
pavadinimu `datasets/gov/dc/geo` ir neradus tokio modelio būtų gražintas `404
Not Found` klaidos kodas.


.. _autorizacija:

Autorizacija
============

Norint gauti atvirus duomenis autorizacija nereikalinga, tačiau norint keisti
saugykloje esančius duomenis are įkelti naujus, būtina autorizacija.

Autorizacija atliekama OAuth_ standarto pagalba. Kol kas yra palaikoma tik
`client credentials`_ autorizavimo būdas.

.. _Oauth: https://en.wikipedia.org/wiki/OAuth
.. _client credentials: https://auth0.com/docs/flows/client-credentials-flow

Norint atlikti rašymo operacijas, pirmiausiai reikia, kad saugykloje jums
būtų sukurta paskyra. Tada naudodamiesi paskyros prisijungimo duomenimis
galite gauti autorizacijos raktą, kuris leis atlikti rašymo operacijas.

Autorizacijos raktas gaunamas taip:

.. code-block:: sh

    http -a $client:$secret -f /auth/token \
        grant_type=client_credentials \
        scope="$scopes" \
        | jq -r .access_token

Pavyzdyje `$scopes` kintamasis yra tarpo simboliais atskirtų leidimu sąrašas.
Leidimų pavadinimai formuojami taip:

.. code-block:: sh

    spinta:$ns/:$action
    spinta:$model/:$action
    spinta:$model.$property/:$action

`$action` reikšmės gali būti tokios:

:getone:
    Galimybė gauti vieną objektą pagal nurodytą objekto `_id`.
:getall:
    Galimybė gauti visus `model` objektus.
:search:
    Galimybė filtruoti `model` objektus.
:changes:
    Galimybė prieiti prie duomenų keitimo žurnalo.
:insert:
    Galimybė kurti naujus objektus.
:upsert:
    Galimybė vykdyti `upsert` veiksmus.
:update:
    Galimybė perrašyti esamus duomenis.
:patch:
    Galimybė keisti esamus duomenis.
:delete:
    Galimybė trinti esamus duomenis.
:wipe:
    Galimybė pilnai šalinti duomenis.

Gautasis autorizacijos raktas `$token`, vykdant užklausas turi būti paduodamas
per HTTP `Authorization` antraštę tokiu būdu:

.. code-block:: sh

    Authorization:Bearer $token

Toliau pavyzdžiuose ši autorizacijos antraštė bus priskirta kintamajam $auth
tokiu būdu:

.. code-block:: sh

    auth="Authorization:Bearer $token"


Skaitymo veiksmai
=================

.. _getall:

getall
------

.. code-block:: sh

    http GET /datasets/gov/dc/geo/Continent

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "_type": "datasets/gov/dc/geo/Continent",
        "_id": "abdd1245-bbf9-4085-9366-f11c0f737c1d",
        "_revision": "16dabe62-61e9-4549-a6bd-07cecfbc3508",
        "_txn": "792a5029-63c9-4c07-995c-cbc063aaac2c",
        "continent": "Europe"
    }


changes
-------


.. code-block:: sh

    http GET /datasets/gov/dc/geo/Continent/:changes

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "_id": "1",
        "_type": "datasets/gov/dc/geo/Continent",
        "_rid": "abdd1245-bbf9-4085-9366-f11c0f737c1d",
        "_revision": "16dabe62-61e9-4549-a6bd-07cecfbc3508",
        "_txn": "792a5029-63c9-4c07-995c-cbc063aaac2c",
        "_created": "2021-07-30T14:03:14.645198",
        "_op": "insert",
        "continent": "Europe"
    }



Duomenų užklausos
=================

Visos duomenų užklausos yra pateikiamos URL query dalyje, po `?` žymės.

Rūšiavimas
----------

Duomenis rūšiuoti galima pasitelkus `sort()` funkciją:

- `sort(column)` - rūšiuoja didėjančia tvarka.
- `sort(-column)` - rūšiuoja mažėjančia tvarka.

Kalima rūšiuoti pagal kelis stulpelius, pavyzdžiui:

    /my/Data?sort(col1,-col2,col3)


Rašymo veiksmai
===============

insert
------

.. code-block:: sh

    http POST /datasets/gov/dc/geo/Continent $auth <<EOF
    {
        "continent": "Europe"
    }
    EOF

.. code-block:: http

    HTTP/1.1 201 Created
    Content-Type: application/json
    Location: /datasets/gov/dc/geo/Continent/abdd1245-bbf9-4085-9366-f11c0f737c1d

    {
        "_type": "datasets/gov/dc/geo/Continent",
        "_id": "abdd1245-bbf9-4085-9366-f11c0f737c1d",
        "_revision": "16dabe62-61e9-4549-a6bd-07cecfbc3508",
        "_txn": "792a5029-63c9-4c07-995c-cbc063aaac2c",
        "continent": "Europe"
    }


upsert
------

`upsert` veiksmas pirmiausiai patikrina ar jau yra sukurtas objektas
atitinkantis `_where` sąlygą, jei yra, tada vykdo `patch` veiksmą, jei nėra,
tada vykdo `update` veiksmą.

.. code-block:: sh

    http POST /datasets/gov/dc/geo/Continent $auth <<EOF
    {
        "_op": "upsert",
        "_where": "name='Africa'",
        "continent": "Africa"
    }
    EOF

.. code-block:: http

    HTTP/1.1 201 Created
    Content-Type: application/json
    Location: /datasets/gov/dc/geo/Continent/b8f1edaa-220d-4e0b-b59b-dc27555a0fb5

    {
        "_type": "datasets/gov/dc/geo/Continent",
        "_id": "b8f1edaa-220d-4e0b-b59b-dc27555a0fb5",
        "_revision": "988969c3-663b-4edf-bd64-861a3f1b1d1c",
        "_txn": "2c5feac6-1d72-48f6-ae63-8f2304693b21",
        "continent": "Africa"
    }


update
------

`update` veiksmas pilnai perrašo objektą. Jei tam tikros objekto savybės
nenurodomos, data tū savybių reikšmės pakeičiamos pagal nutylėjimą
naudojamomis reikšmėmis.

Vykdant `update` taip pat būtina perduoti `_revision` revizijos numeri. Jei
revizijos numeris nesutaps, su tuo, kas jau yra duomenų bazėje, tada duomenys
nebus keičiami ir bus gražinta klaida. Tai reikalinga tam, kad būtų
užtikrintas duomenų vientisumas.

.. code-block:: sh

    http PUT /datasets/gov/dc/geo/Continent/b8f1edaa-220d-4e0b-b59b-dc27555a0fb5 $auth <<EOF
    {
        "_revision": "988969c3-663b-4edf-bd64-861a3f1b1d1c",
        "continent": "Africa"
    }
    EOF

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Location: /datasets/gov/dc/geo/Continent/b8f1edaa-220d-4e0b-b59b-dc27555a0fb5

    {
        "_type": "datasets/gov/dc/geo/Continent",
        "_id": "b8f1edaa-220d-4e0b-b59b-dc27555a0fb5",
        "_revision": "988969c3-663b-4edf-bd64-861a3f1b1d1c",
        "_txn": "2c5feac6-1d72-48f6-ae63-8f2304693b21",
    }

Jei duomenys duomenų bazėje ir duomenys perduoti `update` užklausos metu yra
identiški, tada duomenų bazėje niekas nekeičiama. Tačiau, jei duomenys
skiriasi, tada į keitimų žurnalą išsaugoma tai, kas buvo pakeista ir sukuriam
nauja revizija. Taip pat fiksuojama nauja transakcija.

`update` atsakyme grąžinamos tiks tos savybės, kurių reikšmės buvo pakeistos,
Jei reikšmės nepasikeitė, tada jos pateikiamos atsakyme.


patch
-----

`patch` veikia panašiai, kaip ir `update`, tačiau objekto pilnai neperrašo,
keičia tik tas savybes, kurios nurodytos.

.. code-block:: sh

    http PATCH /datasets/gov/dc/geo/Continent/b8f1edaa-220d-4e0b-b59b-dc27555a0fb5 $auth <<EOF
    {
        "_revision": "988969c3-663b-4edf-bd64-861a3f1b1d1c",
        "continent": "Africa"
    }
    EOF

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Location: /datasets/gov/dc/geo/Continent/b8f1edaa-220d-4e0b-b59b-dc27555a0fb5

    {
        "_type": "datasets/gov/dc/geo/Continent",
        "_id": "b8f1edaa-220d-4e0b-b59b-dc27555a0fb5",
        "_revision": "988969c3-663b-4edf-bd64-861a3f1b1d1c",
        "_txn": "2c5feac6-1d72-48f6-ae63-8f2304693b21",
    }


delete
------

Trina objektą. Objektas pilnai nėra ištrinamas, jis vis dar lieka keitimų
žurnale ir gali būti atstatytas.

.. code-block:: sh

    http DELETE /datasets/gov/dc/geo/Continent/b8f1edaa-220d-4e0b-b59b-dc27555a0fb5 $auth

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "_type": "datasets/gov/dc/geo/Continent",
        "_id": "b8f1edaa-220d-4e0b-b59b-dc27555a0fb5",
        "_revision": "7c2d7b98-498f-49c6-bbb2-b0fd0b03b815",
        "_txn": "448045c6-9993-4845-b889-56483a20f8f3"
    }


.. _wipe:

wipe
----

Pilnai ištrina objektą, įskaitant ir objekto pėdsakus keitimo žurnale. Tokiu
būdu ištrinto objekto atstatyti neįmanoma.

.. note::

    **Naudoti tik išimtiniais atvejais.**

    `wipe` operacija naudojama tik išimtiniais atvejais, jei pastebėta
    esminių klaidų duomenų įkėlimo skriptuose, duomenys dėl įvairių klaidų
    buvo sugadinti ir pan. Duomenų įkėlimo procesą geriausia išsitestuoti
    :ref:`testinėje aplinkoje <saugyklos-testinė-aplinka>`.

    Duomenų įkėlimo praktika, kai visi publikuoti duomenys ištrinami ir
    įkeliami iš naujo nerekomenduotina, kadangi tokiu atveju dingsta duomenų
    keitimo istorija, gali pasikeisti objektų identifikatoriai. Duomenys turi
    būti pirmą kartą įkeliame, o tada atnaujinama tik tai, kas pasikeitė.

.. code-block:: sh

    http DELETE /datasets/gov/dc/geo/Continent/b8f1edaa-220d-4e0b-b59b-dc27555a0fb5/:wipe $auth

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "_type": "datasets/gov/dc/geo/Continent",
        "_id": "b8f1edaa-220d-4e0b-b59b-dc27555a0fb5",
        "_revision": "7c2d7b98-498f-49c6-bbb2-b0fd0b03b815",
        "_txn": "448045c6-9993-4845-b889-56483a20f8f3"
    }



Grupiniai rašymo veiksmai
=========================

Vienos HTTP užklausos metu galima vykdyti rašymo veiksmus grupei objektų. Tokiu
būdu, veiksmai vykdomi vienoje duomenų bazės transakcijoje užtikrinant duomenų
vientisumą.

Grupiniai veiksmai gali būti vykdomi dviem būdais, paprastuoju ir srautiniu.

Paprastasis grupinis rašymas
----------------------------

Paprastasis grupinis rašymas vykdomas per POST užklausą, kurioje yra
pateiktas `_data` masyvas veiksmų.

Vykdant grupinius veiksmus būdina nurodyti `_op` veiksmą ir `_type` modelio
pavadinimą, kuriam taikomas veiksmas.

Grupinis rašymas gali būti vykdomas konkrečiam vienam modeliui, arba keliems
skirtingiems modeliams, vykdant užklausą vardų erdvės kontekste.

.. code-block:: sh

    http POST /datasets/gov/dc/geo/Continent $auth <<EOF
    {
        "_data": [
            {
                "_op": "insert",
                "_type": "datasets/gov/dc/geo/Continent",
                "continent": "Africa"
            },
            {
                "_op": "insert",
                "_type": "datasets/gov/dc/geo/Continent",
                "continent": "Europe"
            }
        ],
    }
    EOF

.. code-block:: http

    HTTP/1.1 207 Multi-Status
    Content-Type: application/json

    {
        "_data": [
            {
                "_type": "datasets/gov/dc/geo/Continent",
                "_id": "b8f1edaa-220d-4e0b-b59b-dc27555a0fb5",
                "_revision": "988969c3-663b-4edf-bd64-861a3f1b1d1c",
                "_txn": "2c5feac6-1d72-48f6-ae63-8f2304693b21",
                "continent": "Africa"
            },
            {
                "_type": "datasets/gov/dc/geo/Continent",
                "_id": "abdd1245-bbf9-4085-9366-f11c0f737c1d",
                "_revision": "16dabe62-61e9-4549-a6bd-07cecfbc3508",
                "_txn": "2c5feac6-1d72-48f6-ae63-8f2304693b21",
                "continent": "Europe"
            }
        ]
    }


Srautinis grupinis rašymas
--------------------------

Paprastasis grupinis rašymas skirtas situacijoms, kai reikia atlikti veiksmus su
nedidele grupe objektų. Tačiau jei objektų labai daug, galima vykdyti srautinį
rašymą.

Srautinis rašymas priima duomenis JSONL formatu ir įeinančiame JSONL sraute
skaito po vieną eilutę ir toje eilutėje pateiktą objektą iš karto vykdo. Tuo
tarpu paprasto grupinio rašymo metu, visi objektai užkraunami į atmintį ir
tik data įrašomi į duomenų bazę.

Kadangi srautinio grupinio rašymo metu objektai skaitomi ir rašomi vienas po
kito, tai leidžia perduoti neribotą kiekį objektų rašymui.

Srautinio grupinio rašymo užklausa atrodo taip:

.. code-block:: sh

    http POST /datasets/gov/dc/geo/Continent $auth Content-Type:application/x-ndjson <<EOF
    {"_op": "insert", "_type": "datasets/gov/dc/geo/Continent", "continent": "Africa"}
    {"_op": "insert", "_type": "datasets/gov/dc/geo/Continent", "continent": "Europe"}
    EOF

.. code-block:: http

    HTTP/1.1 207 Multi-Status
    Content-Type: application/json

    {
        "_txn": "2c5feac6-1d72-48f6-ae63-8f2304693b21",
        "_status": {
            "insert": 2
        }
    }

Srautinio rašymo užklausai būtina perduoti `Content-Type` antrašte su viena
iš šių reikšmių::

    application/x-ndjson
    application/x-jsonlines

Tada bus vykdomas srautinis veiksmų vykdymas.

Srautinės užklausos atsakymas yra santrauka api tai, kiek kokių veiksmų buvo
įvykdyta ir transakcijos numeris. Naudojant transakcijos numerį, atskiros
užklausos metu, galima gauti visų pakeistų objektų identifikatorius `_id` ir
revizijos numerius `_revision` ir informaciją apie tai, kas tiksliai buvo pakeista.