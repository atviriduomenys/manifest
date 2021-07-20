.. default-role:: literal

.. _spinta:

Spinta
######

Kad būtų paprasčiau, duomenų atvėrimui rekomenduojame naudoti įrankį pavadinimu
`Spinta`__, kuris sukurtas būtent duomenų atvėrimo automatizavimui. Spinta
leidžia automatizuotai generuoti duomenų struktūros aprašus, juos patikrinti ar
nėra klaidų, perduoti duomenis į :ref:`saugyklą <saugykla>` ir :ref:`publikuoti
<saugykla>` atvertus duomenis aukščiausiu :ref:`brandos lygiu <level>` ir
laikantis geriausių atvirų duomenų publikavimo praktikų.

__ https://gitlab.com/atviriduomenys/spinta/

Jei naudodamiesi Spinta radote kokių nors klaidų ar turite kitų pastabų,
galite `pranešti apie klaidą`__, kad galėtume ją pataisyti.

__ https://gitlab.com/atviriduomenys/spinta/-/issues/new


Diegimas
========

Techniniai reikalavimai
-----------------------

Duomenų atvėrimo priemonė Spinta yra sukurta naudojant Python_ technologiją.
Todėl prieš diegiant, jūsų naudojamoje aplinkoje turi būti `įdiegta`__ Python
3.9 arba naujesnė versija.

.. _Python: https://www.python.org/

__ https://www.python.org/downloads/


.. _install-debian-ubuntu:

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
    $ sudo apt upgrade
    $ sudo apt install -y \
         git make build-essential libssl-dev zlib1g-dev \
         libbz2-dev libreadline-dev libsqlite3-dev wget \
         curl llvm libncurses5-dev libncursesw5-dev \
         xz-utils tk-dev libffi-dev liblzma-dev \
         python-openssl
    $ curl https://pyenv.run | bash
    $ cd
    $ PYVER=$(.pyenv/bin/pyenv install --list | grep -v - | grep 3.9. | tail -1 | xargs)
    $ .pyenv/bin/pyenv install $PYVER

Jei diegiate Spintą kitoje Linux distribucijoje, reikalingų paketų sąrašą
galite rasti `pyenv dokumentacijoje`_.

.. _pyenv dokumentacijoje: https://github.com/pyenv/pyenv/wiki#suggested-build-environment

Kai jau turite tinkamą Python_ versiją, reikia sukurti izoliuotą aplinką į
kurią bus diegiama Spinta:

.. code-block:: sh

    $ .pyenv/versions/$PYVER/bin/python -m venv spinta

Paskutinis žingsnis, Spinta paketo diegimas:

.. code-block:: sh

    $ spinta/bin/pip install spinta

Galiausiai, įdiegus Spinta paketą, reikia aktyvuoti izoliuotą aplinką, kad
galėtumėte toliau dirbti su Spinta paketo teikiama komanda `spinta`:

.. code-block:: sh

    $ source spinta/bin/activate

Tai padarius, galite patikrinti ar komanda `spinta` veikia:

.. code-block:: sh

    $ spinta --version
    0.1.9

Ši komanda turi išvesti, Spinta priemonės versijos numerį.

.. note::

    Atkreipkite dėmesį, kad `spinta` komanda yra pasiekiama tik tada, kai yra
    aktyvuota Python virtuali aplinka:

    .. code-block:: sh

        $ source spinta/bin/activate

    Python virtualios aplinkos aktyvavimas galioja tol, kol yra aktyvi terminalo
    sesija.


Windows
-------

Tiesioginio Windows palaikymo nėra, tačiau Spinta galima įdiegti ir naudoti
per Windows Subsystem for Linux (WSL). Informaciją apie tai, kaip įsidiegti
WSL galite rasti `Microsoft Windows dokumentacijoje`__.

__ https://docs.microsoft.com/en-us/windows/wsl/install-win10

Renkantis Linux distribuciją iš Microsoft Store rekomenduojame rinktis Ubuntu_.

.. _Ubuntu: https://www.microsoft.com/en-in/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab

Įsidiegus ir pasileidus Ubuntu per WSL, toliau sekite
:ref:`install-debian-ubuntu` instrukcijas.

Galimos problemos ir jų sprendimai
``````````````````````````````````

Jei įvykdžius sekančią komandą:

.. code-block:: sh

    $ curl https://pyenv.run | bash

Gaunate tokią klaidą::

    % Total % Received % Xferd Average Speed Time Time Time Current
    Dload Upload Total Spent Left Speed
    100 285 100 285 0 0 396 0 --:--:-- --:--:-- --:--:-- 395
    curl: (60) SSL certificate problem: self signed certificate in certificate chain
    More details here: https://curl.haxx.se/docs/sslcerts.html

    curl failed to verify the legitimacy of the server and therefore could not
    establish a secure connection to it. To learn more about this situation and
    how to fix it, please visit the web page mentioned above.

Tuomet įsitikinkite, kad jūsų ugniasienė neblokuoja  prieigos prie išorinių
resursų. Taip pat galite laikinai sustabdyti antivirusinė, kuri taip pat gali
blokuoti tokio pobūdžio komandų vykdymą.

Kitas variantas, `curl` komandą galite vykdyti su `-k` argumentu.

Panaši situacija gali pasitaikyti ir vykdant:

.. code-block:: sh

    .pyenv/bin/pyenv install $PYVER

Šios komandos vykdymo metu galite gauti tokią klaidą::

    Downloading Python-3.9.5.tar.xz...
    -> https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tar.xz
    error: failed to download Python-3.9.5.tar.xz

    BUILD FAILED (Ubuntu 20.04 using python-build 2.0.0)

Tokių atveju įsitikinkite ar ugniasienė leidžia kreiptis į išore ir
pabandykite laikinai sustabdyti antivirusinę programą.


ŠDSA generavimas
================

Spinta leidžia automatiškai generuoti :term:`DSA` lentelę iš duomenų
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

Jei norima :term:`DSA` lentelę išsaugoti į Excel lentelę, tada argumento `-o`
pagalba galima nurodyti kelią iki failo, kuriame reikia išsaugoti :term:`DSA`
lentelę XLSX formatu:

.. code-block:: sh

    $ spinta inspect -r sql sqlite:///sqlite.db -o manifest.xlsx

:term:`DSA` lentelę, išsaugotą XLSX formatu galima atsidaryti ir redaguoti
naudojant LibreOffice Calc, Excel ar kitomis skaičiuoklės programomis. Tačiau
taip pat lentelės turinį galima peržiūrėti ir Spintos pagalba:

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

    $ spinta init manifest.xlsx

Ši komanda sugeneruos tuščią :term:`DSA` lentelę:

.. code-block:: sh

    $ spinta show manifest.xlsx
    d | r | b | m | property | type   | ref | source

Tada, šią lentelę galite atsidaryti su jūsų `mėgiama skaičiuoklės programa`__ ir
užpildyti turimus duomenų šaltinius, pavyzdžiui, tokia užpildyta lentelė galėtų
atrodyti taip:

__ https://www.libreoffice.org/discover/calc/

.. code-block:: sh

    $ spinta show resources.xlsx

    d | r | b | m | property | type   | ref | source
    dataset                  |        |     |
      | sql                  | sql    |     | sqlite:///sqlite.db


Struktūros generavimas daromas panašiai, kaip ir nurodant resursus `-r`
argumentų pagalba, tik šį karta reikia nurodyti kelia iki :term:`DSA` lentelės:

.. code-block:: sh

    $ spinta inspect resources.xlsx -o manifest.xlsx
    $ spinta show manifest.xlsx
    d | r | b | m | property | type   | ref | source
    dataset                  |        |     |
      | sql                  | sql    |     | sqlite:///sqlite.db
                             |        |     |
      |   |   | Country      |        |     | COUNTRY
      |   |   |   | name     | string |     | NAME


Analogiškai :term:`DSA` lentelės generuojamos ir visiems kitiems
:data:`resource.type` formatams.


SQL DDL dump
------------

.. warning::

    Kol kas šis funkcionalumas nėra pilnai įgyvendintas. Spinta gali sugeneruoti
    :term:`DSA` tik lentelėms.

Jei tam tikras resursas reikalauja formulių panaudojimo, tada formulę galite
nurodyti `-f` argumento pagalba. Pavyzdžiui, jei neturite prieigos prie
pačios duomenų bazės, bet turite prieigą, prie duomenų bazės SQL DDL skripto,
o skriptas yra užkoduotas `UTF-16` koduote. Tada :term:`DSA` lentelė bus
generuojama taip:

.. code-block:: sh

    $ spinta inspect -r sqldump dump.sql -f 'file(encoding: "utf-16")'
    d | r | b | m | property | type   | ref | source              | prepare
    dataset                  |        |     |                     |
      | sql                  | sql    |     | sqlite:///sqlite.db | file(encoding: "utf-16")
                             |        |     |                     |
      |   |   | Country      |        |     | COUNTRY             |
      |   |   |   | name     | string |     | NAME                |

Šiuo atveju, `dump.sql` failas atrodytų taip:

.. code-block:: sql

    CREATE TABLE COUNTRY (
        NAME TEXT
    );


MySQL
-----

Generuojant :term:`DSA` iš MySQL duomenų bazės, jums papildomai reikia
įdiegti tokį Python paketą:

.. code-block:: sh

    $ pip install pymysql

O `inspect` komanda atrodys taip:

.. code-block:: sh

    $ spinta inspect -r sql mysql+pymysql://user:pass@host:port/db -o manifest.xlsx


Microsoft SQL Server
--------------------

Generuojant :term:`DSA` iš Microsoft SQL Server duomenų bazės, jums
papildomai reikia įdiegti FreeTDS_ paketą:

.. _FreeTDS: http://www.freetds.org/

.. code-block:: sh

    $ sudo apt install freetds-bin

Ir pymssql_ Python paketą:

.. _pymssql: https://www.pymssql.org/

.. code-block:: sh

    $ pip install pymssql

Toliau reikia `sukonfigūruoti FreeTDS`_, rekomenduojame naudoti tokį
konfigūracijos failą:

.. _sukonfigūruoti FreeTDS: https://www.pymssql.org/freetds.html

.. code-block:: conf

    [global]
    tds version = 7.4
    port = 1433
    client charset = utf-8

`inspect` komanda atrodys taip:

.. code-block:: sh

    $ spinta inspect -r sql mssql+pymssql://user:pass@host:port/db -o manifest.xlsx


CSV
---

.. note::

    Kol kas Spinta neturi CSV formato palaikymo, todėl norint generuoti duomenų
    struktūros aprašą iš CSV formato failų, pirmiausia CSV reikėtų importuoti į
    kokią nors SQL duomenų bazę, pavyzdžiui SQLite, o tada duomenų struktūros
    aprašą generuoti  iš SQL duomenų bazės. Toks apėjimo būdas yra laikinas, kol
    Spintoje dar nėra CSV palaikymo.




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


Duomenų publikavimas į Saugyklą
===============================

Prieš publikuojant duomenis į :ref:`Saugyklą <saugykla>`, Saugykloje turi būti
įkeltas :ref:`duomenų struktūros aprašas <dsa>`. Saugykla gali priimti tik
duomenis, turinčius :term:`DSA`.

Taip pat, prieš publikuojant duomenis, Saugykloje turi būti užregistruotas
klientas, kuriam suteikiamos rašymo į saugyklą teisės. Klientui suteikiamos
rašymo teisės į tam tikrą vardų erdvę, todėl skirtingi klientai, gali rašyti
duomenis tik į tam tikrą, jiems skirtą vardų erdvę.

Kliento autorizacijos duomenys turėtu būti pateikiami `credentials.cfg` faile.
`credentials.cfg` failo ieškoma `$XDG_CONFIG_HOME/spinta kataloge`__
(pavyzdžiui
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
