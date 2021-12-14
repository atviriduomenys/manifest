.. default-role:: literal

.. _spinta:

Spinta
######

Kad būtų paprasčiau atverti duomenis, rekomenduojame naudoti įrankį pavadinimu
`Spinta`__, kuris sukurtas duomenų atvėrimo automatizavimui. Spinta leidžia
automatizuotai generuoti duomenų struktūros aprašus, juos patikrinti ar nėra
klaidų, perduoti duomenis į :ref:`saugyklą <saugykla>` ir :ref:`publikuoti
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

Pirmiausia, prieš atliekant diegimą, reikėtų pasirinkti kokiame failų
sistemos kataloge diegsite priemones. Rekomenduojame diegti į `/opt/spinta`
katalogą.

Jei diegimą atliekate serveryje, tuomet verta sukurti atskirą naudotoją,
kurio teisėmis bus leidžiamos priemonės, tai padaryti galite taip:

.. code-block:: sh

    $ sudo useradd --system --create-home --home-dir /opt/spinta spinta
    $ sudo -u spinta -s --set-home
    $ cd

Toliau visus veiksmus atliksime `/opt/spinta` kataloge.

Pirmiausia reikėtų įsitikinti ar jūsų naudojama distribucijos versija turi
reikalinga Python versiją, tai galite pažiūrėti taip:

.. code-block:: sh

    $ python3 --version

Jei turite 3.9 ar naujesnę versiją, tuomet galite pereiti prie
:ref:`install-debian-python-packages` žingsnio.

Naujesnę Python versiją galite įsidiegti pasirinkdami vieną iš dviejų galimų
variantų:

- :ref:`Variantas 1 <install-debian-pyenv>`: naudojant pyenv_, kuris atsisiūs
  Python išeities kodą ir sukompiliuos reikiamą Python versiją. Šis variantas
  yra universalesnis, tačiau sudėtingesnis ir reikalaujantis daugiau laiko.

- :ref:`Variantas 2 <install-debian-ppa>` Naudojant PPA_ repozitoriumus, kurie
  veiks tik Ubuntu aplinkoje, tačiau reikiamą Python versiją gausite žymiai
  paprasčiau.

.. _PPA: https://help.ubuntu.com/community/PPA
.. _pyenv: https://github.com/pyenv/pyenv

.. _install-debian-pyenv:

Naujesnės Python versijos diegimas naudojant pyenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pirmiausia mums reikia įdiegti pyenv_ ir visus šiai priemones ir Python
kompiliavimui reikalingus paketus:

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

Naujausios Python versijos diegimas naudojant pyenv_ daromas taip:

.. code-block:: sh

    $ .pyenv/bin/pyenv install 3.9.9

Jei diegiate Spintą kitoje Linux distribucijoje, reikalingų paketų sąrašą
galite rasti `pyenv dokumentacijoje`_.

.. _pyenv dokumentacijoje: https://github.com/pyenv/pyenv/wiki#suggested-build-environment

Atlikus naujos Python versijos diegimo veiksmus susikuriame izoliuotą aplinką,
kurioje diegsime reikalingus Python paketus:

.. code-block:: sh

    $ .pyenv/versions/3.9.9/bin/python -m venv venv


.. _install-debian-ppa:

Naujesnės Python versijos diegimas naudojant PPA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Naujausios Python versijos diegimas naudojant PPA_ daromas taip:

Pirmiausiai mums reikia įdiegti PPA_ repozitoriumų valdymo priemones:

.. code-block:: sh

    $ sudo apt update
    $ sudo apt install software-properties-common
    $ sudo add-apt-repository ppa:deadsnakes/ppa

Ir galiausiai įdiegiame pageidaujamą Python versiją:

.. code-block:: sh

    $ sudo apt update
    $ sudo apt install python3.9 python3.9-venv

Atlikus naujos Python versijos diegimo veiksmus susikuriame izoliuotą aplinką,
kurioje diegsime reikalingus Python paketus:

.. code-block:: sh

    $ python3.9 -m venv venv


.. _install-debian-python-packages:

Python paketų diegimas
~~~~~~~~~~~~~~~~~~~~~~

Kai jau turite tinkamą Python_ versiją ir esate susikūrė izoliuotą Python
aplinką, Spinta galima įdiegti taip:

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

.. _šdsa-generavimas:

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

    $ spinta inspect -r sql sqlite:///sqlite.db -o sdsa.xlsx

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

    $ spinta init sdsa.xlsx

Ši komanda sugeneruos tuščią :term:`DSA` lentelę:

.. code-block:: sh

    $ spinta show sdsa.xlsx
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

    $ spinta inspect resources.xlsx -o sdsa.xlsx
    $ spinta show sdsa.xlsx
    d | r | b | m | property | type   | ref | source
    dataset                  |        |     |
      | sql                  | sql    |     | sqlite:///sqlite.db
                             |        |     |
      |   |   | Country      |        |     | COUNTRY
      |   |   |   | name     | string |     | NAME


Analogiškai :term:`DSA` lentelės generuojamos ir visiems kitiems
:data:`resource.type` formatams.


CSV
---

.. note::

    Kol kas Spinta neturi įmontuoto CSV formato palaikymo, todėl
    ši rekomendacija yra laikinas trūkstamo CSV palaikymo apėjimas. Ateityje
    planuojama integruoti Dask_ karkasą, kurio dėka atsiras CSV ir `daugelio
    kitų formatų`__ palaikymas.

    .. _Dask: https://dask.org/

    __ https://docs.dask.org/en/latest/dataframe-api.html#create-dataframes

Norint gauti pradinė ŠDSA variantą iš CSV failų, pirmiausiai CSV failus
reikėtų importuoti į SQLite duomenų bazę:

.. code-block:: sh

    $ sqlite3 data.db -csv ".import table1.csv table1"
    $ sqlite3 data.db -csv ".import table2.csv table2"
    $ sqlite3 data.db -csv ".import table3.csv table3"

Tokiu būdu importavus duomenis į SQLite, duomenų struktūros aprašas
generuojamas taip:

.. code-block:: sh

    $ spinta inspect -r sql sqlite:///data.db -o sdsa.xlsx

Jei pageidaujate, trūkstamus metaduomenis, tokius kaip duomenų laukus,
pirminius raktus ar ryšius galite pateikti naudodami `DB Browser for SQLite`_
programą. Tačiau tą patį galite padaryti ir skaičiuoklės pagalba, redaguodami
ŠDSA lentelę.

.. _DB Browser for SQLite: https://sqlitebrowser.org/


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


SQLite
------

Generuojant :term:`DSA` iš SQLite duomenų bazės, jokių papildomų paketų
diegti nereikia. `inspect` komanda atrodys taip:

.. code-block:: sh

    $ spinta inspect -r sql sqlite:///data.db -o sdsa.xlsx

Atkreipkite dėmesį, kad absoliutus kelias atrodo taip::

    sqlite:////data.db

O reliatyvus atrodo taip::

    sqlite:///data.db


PostgreSQL
----------

Generuojant :term:`DSA` iš PostgreSQL duomenų bazės, jums papildomai reikia
įdiegti tokį Python paketą:

.. code-block:: sh

    $ pip install psycopg2-binary

O `inspect` komanda atrodys taip:

.. code-block:: sh

    $ spinta inspect -r sql postgresql+psycopg2://user:pass@host:port/db -o sdsa.xlsx


MySQL
-----

Generuojant :term:`DSA` iš MySQL duomenų bazės, jums papildomai reikia
įdiegti tokį Python paketą:

.. code-block:: sh

    $ pip install pymysql

O `inspect` komanda atrodys taip:

.. code-block:: sh

    $ spinta inspect -r sql mysql+pymysql://user:pass@host:port/db -o sdsa.xlsx


MySQL (<5.6)
------------

`pymysql` biblioteka palaiko MySQL >= 5.6 ir MariaDB >= 10 versijas. Jei
naudojate labai seną MySQL versiją, tuomet, vietoj `pymysql` reikėtų naudoti
senesnę mysqlclient_ biblioteką, kuri palaiko MySQL >= 3.23.32. `mysqlclient`
diegimui pirmiausia reikės įsidiegti tokius sisteminius paketus:

.. _mysqlclient: https://pypi.org/project/mysqlclient/

.. code-block:: sh

    $ sudo apt install build-essential python3-dev default-libmysqlclient-dev

O data ir pačią `mysqlclient` biblioteką:

.. code-block:: sh

    pip install mysqlclient

`inspect` komanda atrodys taip:

.. code-block:: sh

    spinta inspect -r sql mysql+mysqldb://user:pass@host:port/db -o sdsa.xlsx

*p.s. jei vis dar naudojate tokią seną MySQL versiją, laikas atsinaujinti!*


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

    $ spinta inspect -r sql mssql+pymssql://user:pass@host:port/db -o sdsa.xlsx


Oracle
------

Generuojant :term:`DSA` iš Oracle duomenų bazės, jums
papildomai reikia įdiegti cx_Oracle_ paketą:

.. _cx_Oracle: https://oracle.github.io/python-cx_Oracle/

.. code-block:: sh

    $ pip install cx_Oracle

Dėl papildomos informacijos apie Oracle jungtį, skaitykite `cx_Oracle
dokumentacijoje`__.

__ https://cx-oracle.readthedocs.io/en/latest/index.html

`inspect` komanda atrodys taip:

.. code-block:: sh

    $ spinta inspect -r sql oracle+cx_oracle://user:pass@host:port/db -o sdsa.xlsx


ŠDSA atnaujinimas
=================

Po to, kai yra sugeneruojamas pradinis ŠDSA ir papildomas trūkstamais
duomenimis, dažniausiai po tam tikro laiko, šaltinio duomenų struktūra
keičiasi ir karts nuo karto reikia atnaujinti esamą ŠDSA ir šaltinio,
įtraukiant naujausius pakeitimus šaltinyje.

Tai galima padaryti tokiu būdu:

.. code-block:: sh

    $ spinta inspect sdsa.xlsx -o sdsa_updated.xlsx

`sdsa_updated.xlsx` faile išliks visi metaduomenys, kuris buvo pradiniame `sdsa
.xlsx`, papildant juos naujais metaduomenimis iš šaltinio.


.. _šdsa-vertimas-į-adsa:

ŠDSA vertimas į ADSA
====================

ŠDSA yra toks duomenų struktūros aprašas, kuris yra susietas su duomenų
šaltiniu, yra užpildytas :data:`source` stulpelis.

Verčiant ŠDSA į ADSA, iš esmės pašalinami :data:`source` ir :data:`prepare`
stulpelių duomenys, o taip pat pašalinamos visos eilutės, kurių
:data:`access` yra mažesnis, nei `open`.

ŠDSA vertimą į ADSA galima daryti automatiškai taip:

.. code-block:: sh

    $ spinta copy sdsa.xlsx --no-source --access open -o adsa.csv


.. _automatinis-atvėrimas:

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

Dar vienas dalykas, į kurį reikėtu atkreipti dėmesį yra būsenos ir objektų
identifikatorių failai. Kadangi `spinta push` komanda į Saugyklą siunčia tik
tuos duomenis kurie dar nebuvo siųsti arba kurie pasikeitė, kad tai veiktų
saugoma duomenų perdavimo į Saugyklą būsena ir identifikatoriai. Būsena saugoma
SQLite duomenų bazėje, `$XDG_DATA_HOME/spinta/push/{remote}.db`__ faile (pavyzdžiui
`~/.local/share/spinta/push/get_data_gov_lt.db`). Identifikatoriai saugomie
`$XDG_DATA_HOME/spinta/keymap.db` SQLite faile (pavyzdžiui
`~/.local/share/spinta/keymap.db`. Priklausomai nuo duomenų kiekio šie failai
gali užimti gan daug vietos. Būsenos ir identifikatorių failuose saugomi
Saugykloje suteikti objektų identifikatoriai, vietiniai identifikatoriai ir
duomenų kontrolinės sumos.

__ https://specifications.freedesktop.org/basedir-spec/latest/ar01s03.html

Kadangi `spinta push` komanda saugo būseną, šią komandą galima leisti daug
kartų ir ji tęs duomenų perdavimą nuo tos vietose kur buvo baigta paskutinį
kartą.

Rekomenduojama šią duomenų publikavimo komanda įtraukti į automatiškai
vykdomų užduočių sąrašą, kad duomenys būtų publikuojamai automatiškai,
pavyzdžiui kas naktį arba kas valandą.

Reikėtu atkreipti dėmesį į tai, kad vienu metu reikėtu leisti tik vieną
`spinta push` komandos procesą.
