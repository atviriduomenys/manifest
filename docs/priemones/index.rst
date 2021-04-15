.. default-role:: literal

.. _priemonės:

Priemonės
#########

Siekiant užtikrinti sklandų ir kiek įmanoma paprastesnį duomenų atvėrimą,
pateikiame ne tik metodinę medžiagą, kaip atverti duomenis ar rengti
:term:`DSA` lenteles, tačiau taip pat pateikiame ir įrankius, kurie padeda
automatizuoti daugelį su duomenų atvėrimu susijusių veiklų.

Kad būtų paprasčiau, duomenų atvėrimui rekomenduojame naudoti įrankį pavadinimu
Spinta_, kuris sukurtas būtent duomenų atvėrimo automatizavimui.

.. _Spinta: https://gitlab.com/atviriduomenys/spinta/

Jei naudodamiesi Spinta_ radote kokių nors klaidų ar turite kitų pastabų,
galite `pranešti apie klaidą`__, kad galėtume ją pataisyti.

__ https://gitlab.com/atviriduomenys/spinta/-/issues/new


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



Diegimas
========

Techniniai reikalavimai
-----------------------

Duomenų atvėrimo priemonė Spinta_ yra sukurta naudojant Python_ technologiją.
Todėl prieš diegiant, jūsų naudojamoje aplinkoje turi būti `įdiegta`__ Python
3.9 arba naujesnė versija.

.. _Python: https://www.python.org/

__ https://www.python.org/downloads/


Debian/Ubuntu
-------------

Kadangi Debian ir Ubuntu sisteminio Python versija dažnai yra senesnė,
rekomenduojama įsidiegti naujausią Python versiją naudojant pyenv_ priemonę.
Nebent, Debian ar Ubuntu naujausia versija yra nesenai išleista ir turi
pakankamai naują, 3.9 ar vėlesnę python versiją.

.. _pyenv: https://github.com/pyenv/pyenv

Naujausios Python versijos diegimas naudojant pyenv_ daromas taip:

.. code-block:: sh

    $ sudo apt update
    $ sudo apt install -y \
         git make build-essential libssl-dev zlib1g-dev \
         libbz2-dev libreadline-dev libsqlite3-dev wget \
         curl llvm libncurses5-dev libncursesw5-dev \
         xz-utils tk-dev libffi-dev liblzma-dev \
         python-openssl
    $ curl https://pyenv.run | bash
    $ cd
    $ PYVER=$(.pyenv/bin/pyenv install --list | grep -v - | tail -1 | xargs)
    $ .pyenv/bin/pyenv install $PYVER

Kai jau turite tinkamą Python_ versiją, reikia sukurti izoliuotą aplinką į
kurią bus diegiama Spinta_:

.. code-block:: sh

    $ .pyenv/versions/$PYVER/bin/python -m venv spinta

Paskutinis žingsnis, Spinta_ paketo diegimas:

.. code-block:: sh

    $ spinta/bin/pip install spinta

Galiausiai, įdiegus Spinta_ paketą, reikia aktyvuoti izoliuotą aplinką, kad
galėtumėte toliau dirbti su Spinta_ paketo teikiama komanda `spinta`:

.. code-block:: sh

    $ source spinta/bin/activate

Tai padarius, galite patikrinti ar komanda `spinta` veikia:

.. code-block:: sh

    $ spinta --version
    0.1.9

Ši komanda turi išvesti, Spinta_ priemonės versijos numerį.


Windows
-------

Deja dėl žmogiškųjų resursų trūkumo, Windows OS šiuo metu nėra palaikoma.


DSA generavimas
===============

Spinta_ leidžia automatiškai generuoti :term:`DSA` lentelę iš duomenų
šaltinio.

Tarkime, jei turime SQLite duomenų bazę su viena lentele:

.. code-block:: sh

    $ sqlite3 sqlite.db <<EOF
    CREATE TABLE COUNTRY (
        NAME TEXT
    );
    EOF

Tada iš tokio duomenų šaltinio, :term:`DSA` lentelę galima sugeneruoti taip:

.. code-block:: sh

    $ spinta inspect -r sql sqlite:///sqlite.db
    d | r | b | m | property | type   | ref | source
    dataset                  |        |     |
      | sql                  | sql    |     | sqlite:///sqlite.db
                             |        |     |
      |   |   | Country      |        |     | COUNTRY
      |   |   |   | name     | string |     | NAME

Šiuo atveju, kadangi nenurodėme kur saugoti sugeneruotą :term:`DSA` lentelę,
ji buvo tiesiog išvesta į ekraną.

`-r` argumentui perduoti du argumentai `sql` ir `sqlite:///sqlite.db`, kurie
atitinka :data:`resource.type` ir :data:`resource.source`.

Jei norima :term:`DSA` lentelę išsaugoti į CSV failą, tada argumento `-o`
pagalba galima nurodyti kelią iki failo, kuriame reikia išsaugoti :term:`DSA`
lentelę CSV formatu:

.. code-block:: sh

    $ spinta inspect -r sql sqlite:///sqlite.db -o manifest.csv

:term:`DSA` lentelę, išsaugotą CSV formatu galima peržiūrėti šios komandos
pagalba:

.. code-block:: sh

    $ spinta show manifest.csv
    d | r | b | m | property | type   | ref | source
    dataset                  |        |     |
      | sql                  | sql    |     | sqlite:///sqlite.db
                             |        |     |
      |   |   | Country      |        |     | COUNTRY
      |   |   |   | name     | string |     | NAME


Jei turite daug duomenų šaltinių, galima juos visus surašyti į :term:`DSA`
lentelę, ir tada paleisti `inspect` komandą, kuri nuskaitys visus lentelėje
esančius duomenų šaltinius ir kiekvienam iš jų sugeneruos duomenų struktūros
aprašus.

Naują :term:`DSA` lentelę galite pradėti kurti taip:

.. code-block:: sh

    $ spinta init manifest.csv

Ši komanda sugeneruos tuščią :term:`DSA` lentelę:

.. code-block:: sh

    $ spinta show manifest.csv
    d | r | b | m | property | type   | ref | source

Tada, šią lentelę galite atsidaryti su jūsų `mėgiama skaičiuoklės programa`__ ir
užpildyti turimus duomenų šaltinius, pavyzdžiui, tokia užpildyta lentelė galėtų
atrodyti taip:

__ https://www.libreoffice.org/discover/calc/

.. code-block:: sh

    $ spinta show manifest.csv

    d | r | b | m | property | type   | ref | source
    dataset                  |        |     |
      | sql                  | sql    |     | sqlite:///sqlite.db


Struktūros generavimas daromas panašiai, kaip ir nurodant resursus `-r`
argumentų pagalba, tik šį karta reikia nurodyti kelia iki :term:`DSA` lentelės:

.. code-block:: sh

    $ spinta inspect manifest.csv
    d | r | b | m | property | type   | ref | source
    dataset                  |        |     |
      | sql                  | sql    |     | sqlite:///sqlite.db
                             |        |     |
      |   |   | Country      |        |     | COUNTRY
      |   |   |   | name     | string |     | NAME


Analogiškai :term:`DSA` lentelės generuojamos ir visiems kitiems
:data:`resource.type` formatams.

Jei tam tikras resursas reikalauja formulių panaudojimo, tada formulę galite
nurodyti `-f` argumento pagalba. Pavyzdžiui, jei neturite prieigos prie
pačios duomenų bazės, bet turite prieigą, prie duomenų bazės SQL DDL skripto,
o skriptas yra užkoduotas `UTF-16` koduote. Tada :term:`DSA` lentelė bus
generuojama taip:

.. code-block:: sh

    $ spinta inspect -r sqldump dump.sql -f 'file(self, encoding: "utf-16")'
    d | r | b | m | property | type   | ref | source               | prepare
    dataset                  |        |     |                      |
      | sql                  | sql    |     | sqlite:///sqlite.db  | file(self, encoding: "utf-16")
                             |        |     |                      |
      |   |   | Country      |        |     | COUNTRY              |
      |   |   |   | name     | string |     | NAME                 |

Šiuo atveju, `dump.sql` failas atrodytų taip:

.. code-block:: sql

    CREATE TABLE COUNTRY (
        NAME TEXT
    );


ŠDSA vertimas į ADSA
====================

ŠDSA yra toks duomenų struktūros aprašas, kuris yra susietas su duomenų
šaltiniu, yra užpildytas :data:`source` stulpelis.

Verčiant ŠDSA į ADSA, iš esmės pašalinami :data:`source` ir :data:`prepare`
stulpelių duomenys, o taip pat pašalinamos visos eilutės, kurių
:data:`access` yra mažesnis, nei `open`.

ŠDSA vertimą į ADSA galima daryti automatiškai taip:

.. code-block:: sh

    $ spinta copy sdsa.csv --no-source --access open -o adsa.csv


Duomenų publikavimas į saugyklą
===============================

Prieš publikuojant duomenis į Saugyklą, Saugykloje turi būti įkeltas duomenų
struktūros aprašas. Saugykla gali priimti tok tokius duomenis, kurie yra
aprašyti duomenų struktūros apraše.

Taip pat, prieš publikuojant duomenis, Saugykloje turi būti užregistruotas
klientas, kuriam suteikiamos rašymo į saugyklą teisės. Klientui suteikiamos
rašymo teisės į tam tikrą vardų erdvę, todėl skirtingi klientai, gali rašyti
duomenis tik į tam tikrą, jiems skirtą vardų erdvę.

Kliento autorizacijos duomenys turėtu būti pateikiami `credentials.cfg` faile.
`credentials.cfg` failo ieškoma `$XDG_CONFIG_HOME/spinta kataloge`__ (pavyzdžiui
`~/.config/spinta/credentials.cfg`). Šio failo formatas atrodo taip:

__ https://specifications.freedesktop.org/basedir-spec/latest/ar01s03.html

.. code-block:: ini

    [ivpk@put.data.gov.lt]
    client = ivpk
    secret = verysecret
    scopes =
      spinta_getall
      spinta_getone
      spinta_search
      spinta_changes
      spinta_datasets_gov_ivpk_insert
      spinta_datasets_gov_ivpk_upsert
      spinta_datasets_gov_ivpk_update
      spinta_datasets_gov_ivpk_patch
      spinta_datasets_gov_ivpk_delete

Čia nurodomas kliento pavadinimas, slaptažodis ir leidimai (`scopes`).
Suteiktas leidimas skaityti visus duomenis ir rašyti tik į
`datasets/gov/ivpk` vardų erdvę.

Kol kas kliento kūrimas Saugykloje yra daromas rankiniu būdu, atskiru
paklausimu, tačiau planuojama tai `automatizuoti`__.

__ https://gitlab.com/atviriduomenys/spinta/-/issues/92

Galiausiai, įkėlus duomenų struktūros aprašą į Katalogą, iš Katalogo įkėlus
aprašą į saugyklą ir turinti klientą Saugykloje, galima publikuoti duomenis į
saugyklą tokiu būdu:

.. code-block:: sh

    $ spinta push sdsa.csv -o spinta+https://ivpk@put.data.gov.lt

Dar vienas dalykas, į kurį reikėtu atkreipti dėmesį yra būsenos failas. Kadangi
`spinta push` komanda į saugyklą siunčia tik tuos duomenis kurie dar nebuvo
siųsti arba kurie pasikeitė, kad tai veiktų saugoma duomenų perdavimo į saugyklą
būsena. Būsena saugoma SQLite duomenų bazėje,
`$XDG_DATA_HOME/spinta/pushstate.db`__ faile (pavyzdžiui
`~/.local/share/spinta/pushstate.db`). Priklausomai nuo duomenų kiekio šis
failas gali užimti gan daug vietos. Būsenos faile saugomi Saugykloje suteikti
objektų identifikatoriai, vietiniai identifikatoriai ir duomenų kontrolinė suma.

__ https://specifications.freedesktop.org/basedir-spec/latest/ar01s03.html

Kadangi `spinta push` komanda saugo būseną, šią komandą galima leisti daug
kartų ir ji tęs duomenų perdavimą nuo tos vietose kur buvo baigta paskutinį
kartą.

Rekomenduojama šią duomenų publikavimo komanda įtraukti į automatiškai
vykdomų užduočių sąrašą, kad duomenys būtų publikuojamai automatiškai,
pavyzdžiui kas naktį arba kas valandą.

Reikėtu atkreipti dėmesį į tai, kad vienu metu reikėtu leisti tik vieną
`spinta push` komandos procesą.