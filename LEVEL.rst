.. default-role:: literal

Brandos lygio vertinimas
########################

Čia rasti komentarų pavyzdžius, kurie įrašomi struktūros apraše, nurodant
kokius trūkumus reikia pašalinti, norint gauti didesnį brandos lygį.

Prefiksai
*********

Dažniausiai naudojami prefiksai komentaruose::

    ,,,,,,prefix,spinta,,,,,https://github.com/atviriduomenys/spinta/issues/,,
    ,,,,,,,manifest,,,,,https://github.com/atviriduomenys/manifest/issues/,,
    ,,,,,,,vadovas,,,,,https://atviriduomenys.readthedocs.io/,,


Nuorodos
********

Dažniausiai naudojamos nuorodos komentaruose.

Neįgyvendintas funkcionalumas:

============  =================================================
spinta:40_    IVPK: `money` duomenų tipo palaikymas
spinta:204_   IVPK: `text` duomenų tipo palaikymas
spinta:205_   IVPK: modelio bazės (`base`) palaikymas
spinta:213_   IVPK: `date` type with `ref=Y`
spinta:216_   IVPK: Denormalizuotų duomenų laukų palaikymas
spinta:269_   IVPK: μ/m³ vienetų palaikymas.
spinta:270_   IVPK: °C vienetų palaikymas.
spinta:279_   IVPK: ZIP šaltinio failų konteinerio palaikymas.
spinta:283_   IVPK: Shape failų šaltinio palaikymas.
============  =================================================

Neatverti arba per žemos brandos lygio duomenys:

===============  =========================================
manifest:1280_   RC: AR Patalpos
manifest:1263_   RC: AR Savivaldybės
manifest:1256_   RC: AR Apskritys
manifest:1290_   RC: JAR Įregistruoti
manifest:1476_   SD: duomenų susiejimo ryšiais palaikymas
===============  =========================================

Dokumentacija ir kiti šaltiniai:

=====================================================  ======================
epsg:3346_                                             LKS94
epsg:4326_                                             WGS84
`vadovas:dsa/dimensijos.html#model.ref`_               Pirminis raktas
`vadovas:dsa/duomenu-tipai.html#erdviniai-duomenys`_   Erdviniai duomenys
`vadovas:dsa/ref.html#susiejimas-neimanomas`_          Susiejimas neįmanomas
`vadovas:dsa/kodiniai-pavadinimai.html`_               Kodiniai pavadinimai
`vadovas:dsa/ref.html`_                                Ryšiai tarp modelių
`vadovas:dsa/dimensijos.html#modelio-baze`_            Modelio bazė
`vadovas:dsa/dimensijos.html#klasifikatoriai`_         Klasifikatoriai
=====================================================  ======================


0 brandos lygis: Duomenų nėra
*****************************

Duomenų nėra arba duomenys nėra atviri.


1 brandos lygis: Atviri duomenys
********************************

Duomenys yra ir jie atviri, pateikiami bet kokia forma ir bet kokiu formatu.


2 brandos lygis: Struktūrizuoti duomenys
****************************************

- Natūraliosios kalbos tipas::

    ,,,,,pavadinimas,string,,,,2,open,,,
    ,,,,,,comment,type,,"update(property: ""pavadinimas@lt"", type: ""text"")",4,open,spinta:204,,

  - spinta:204_ - IVPK: `text` duomenų tipo palaikymas.

- Duomenų susiejimas ryšiais įmanomas::

    ,,,,,imone,string,,,,2,open,,,
    ,,,,,,comment,type,,"update(type: ""ref"", ref: ""Istaiga"")",4,open,"manifest:1476,vadovas:dsa/ref.html",,

    ,,,,,licencijos_id,integer,,,,2,open,,Licencijos identifikatorius,
    ,,,,,,comment,type,,"update(property: ""licencija"", type: ""ref"", ref: ""Licencija"")",4,open,"manifest:1476,vadovas:dsa/ref.html",,

  - manifest:1476_ - SD: duomenų susiejimo ryšiais palaikymas.
  - `vadovas:dsa/ref.html`_ - Ryšiai tarp modelių

- Duomenų susiejimas ryšiais neįmanomas::

    ,,,,,adresas,string,,,,1,open,,,
    ,,,,,,comment,type,,"update(type: ""ref"", ref: ""/datasets/gov/rc/ar/pastatas/Pastatas"")",4,open,vadovas:vadovas:dsa/ref.html#susiejimas-neimanomas,,
    ,,,,,,comment,type,,"update(type: ""ref"", ref: ""/datasets/gov/rc/ar/patalpa/Patalpa"")",4,open,vadovas:vadovas:dsa/ref.html#susiejimas-neimanomas,,

  - `vadovas:dsa/ref.html#susiejimas-neimanomas`_ - Susiejimas neįmanomas.

- Nenurodyta dubliuojamo modelio bazė::

    ,,,,Istaiga,,,,,,2,,,,
    ,,,,,,comment,base,,"update(base: ""/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo"", ref: ""ja_kodas"")",4,open,"spinta:205, manifest:1290",,

  - spinta:205_ - IVPK: modelio bazės (`base`) palaikymas.
  - manifest:1290_ - RC: JAR.

- Dubliojami duomenys::

    ,,,,,pavadinimas,string,,,,2,open,,,
    ,,,,,,comment,type,,"update(property: ""pavadinimas@lt"", type: """")",4,open,"spinta:204, spinta:205, manifest:1290",,

  - spinta:204_ - IVPK: `text` duomenų tipo palaikymas.
  - spinta:205_ - IVPK: modelio bazės (`base`) palaikymas.
  - manifest:1290_ - RC: JAR.

- Denormalizuoti duomenys::

    ,,,,,kodas,string,,,,2,open,,,
    ,,,,,,comment,type,,"create(property: ""istaiga"", type: ""ref"", ref: ""/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo"")",4,open,"spinta:216,vadovas:dsa/ref.html#denormalizuoti-duomenys",,
    ,,,,,,comment,type,,"update(property: ""istaiga.kodas"", type: """")",4,open,"spinta:216,vadovas:dsa/ref.html#denormalizuoti-duomenys",,

  - spinta:216_ - IVPK: denormalizuotų duomenų laukų palaikymas.
  - `vadovas:dsa/ref.html#denormalizuoti-duomenys`_ - Denormalizuoti duomensy.

- Koordinatės::

    ,,,,,ilguma,number,,,,2,open,,,
    ,,,,,,comment,type,,delete(),3,open,vadovas:dsa/duomenu-tipai.html#erdviniai-duomenys,,
    ,,,,,platuma,number,,,,2,open,,,
    ,,,,,,comment,type,,"update(type: ""geometry(point, 4326)""))",3,open,vadovas:dsa/duomenu-tipai.html#erdviniai-duomenys,,

  - epsg:4326_ - WGS84.
  - epsg:3346_ - LKS94.
  - `vadovas:dsa/duomenu-tipai.html#erdviniai-duomenys`_ - Erdviniai duomenys.

- Neteisingai užrašyti kodiniai pavadinimai::

    ,,,,,ja_kodas,string,,,,2,open,,,,,
    ,,,,,,comment,property,,"update(property: ""kodas"")",4,open,vadovas:dsa/kodiniai-pavadinimai.html,,

    ,,,,,isakymo_id,ref,Isakymas,,,2,open,,,
    ,,,,,,comment,property,,"update(property: ""isakymas"")",4,open,vadovas:dsa/kodiniai-pavadinimai.html,,

  - `vadovas:dsa/kodiniai-pavadinimai.html`_ - Kodiniai pavadinimai.

- Nepateiktas enum, kai reikšmės pateiktos kodais::

    ,,,,,asmuo_visuomene,integer,,,,2,open,,"Žyma, ar tai asmens, ar visuomenės sveikatos priežiūros įstaigos licencija",
    ,,,,,,comment,ref,,"update(ref: ""enum"")",4,open,vadovas:dsa/dimensijos.html#klasifikatoriai,,

  - `vadovas:dsa/dimensijos.html#klasifikatoriai`_ - Klasifikatoriai.


3 brandos lygis: Standartinė forma
**********************************

Duomenys yra ne tik struktūruoti, bet pateikti laikantis standartų reikalavimų
nurodytų `duomenų struktūros aprašo specifikacijoje`__.

__ https://atviriduomenys.readthedocs.io/dsa/index.html

- Nenurodytas pirminis raktas::

    ,,,,Institucija,,,,,,3,,,,
    ,,,,,,comment,ref,,"update(ref: ""kodas"")",4,open,vadovas:dsa/dimensijos.html#model.ref,,

  - `vadovas:dsa/dimensijos.html#model.ref`_ - Pirminis raktas.

- Vienetų palaikymas::

    ,,,,,koncentracija,number,,,,3,open,,,
    ,,,,,,comment,ref,,"update(ref: ""μ/m³"")",4,open,spinta:269,,
    ,,,,,,comment,ref,,"update(ref: ""°C"")",4,open,spinta:270,,

  - spinta:269_ - IVPK: μ/m³ vienetų palaikymas.
  - spinta:270_ - IVPK: °C vienetų palaikymas.


4 brandos lygis: Identifikatoriai ir vienetai
*********************************************

Pateikiami metaduomenys apie pirminius ir išorinius raktus, vienetus, laiko ir
vietos matavimų tikslumą.


5 brandos lygis: Standartiai žodynai ir ontologijos
***************************************************

Pateikiama sąsaja su standartiniais žodynai ir ontologijomis.


Informacijos šaltiniai
**********************

- `Duomenų atvėrimo vadovas: Brandos lygiai`__

  __ https://atviriduomenys.readthedocs.io/dsa/level.html

- `Duomenų atvėrimo vadovas: Ryšiai tarp modelių: Brandos lygis`__

  __ https://atviriduomenys.readthedocs.io/dsa/ref.html#brandos-lygis

- `Brandos lygių žymėjimo lentelė su kodais`__

  __ https://docs.google.com/spreadsheets/d/1mIwOW462-AMBiN1prveXcqjXi2JpEsR6X-_kUaIB6Q0/edit?usp=sharing

.. _spinta:40: https://github.com/atviriduomenys/spinta/issues/40
.. _spinta:204: https://github.com/atviriduomenys/spinta/issues/204
.. _spinta:205: https://github.com/atviriduomenys/spinta/issues/205
.. _spinta:213: https://github.com/atviriduomenys/spinta/issues/213
.. _spinta:216: https://github.com/atviriduomenys/spinta/issues/216
.. _spinta:269: https://github.com/atviriduomenys/spinta/issues/216
.. _spinta:270: https://github.com/atviriduomenys/spinta/issues/216

.. _manifest:1290: https://github.com/atviriduomenys/manifest/issues/1290
.. _manifest:1476: https://github.com/atviriduomenys/manifest/issues/1476

.. _vadovas:dsa/ref.html#susiejimas-neimanomas: https://atviriduomenys.readthedocs.io/dsa/ref.html#susiejimas-neimanomas
.. _vadovas:dsa/duomenu-tipai.html#erdviniai-duomenys: https://atviriduomenys.readthedocs.io/dsa/duomenu-tipai.html#erdviniai-duomenys
.. _vadovas:dsa/dimensijos.html#model.ref: https://atviriduomenys.readthedocs.io/dsa/dimensijos.html#model.ref
.. _vadovas:dsa/kodiniai-pavadinimai.html: https://atviriduomenys.readthedocs.io/dsa/kodiniai-pavadinimai.html
.. _vadivas:dsa/ref.html: https://atviriduomenys.readthedocs.io/dsa/ref.html
.. _vadovas:dsa/dimensijos.html#modelio-baze: https://atviriduomenys.readthedocs.io/dsa/dimensijos.html#modelio-baze
.. _vadovas:dsa/dimensijos.html#klasifikatoriai: https://atviriduomenys.readthedocs.io/dsa/dimensijos.html#klasifikatoriai
.. _vadovas:dsa/ref.html#denormalizuoti-duomenys: https://atviriduomenys.readthedocs.io/dsa/ref.html#denormalizuoti-duomenys

.. _epsg:3346: https://epsg.io/3346
.. _epsg:4326: https://epsg.io/4326
