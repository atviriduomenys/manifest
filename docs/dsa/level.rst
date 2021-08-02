.. default-role:: literal
.. _level:

Brandos lygiai
==============

Duomenų brandos lygis nurodomas :data:`level` stulpelyje.

Duomenų brandos lygis atitinka `5 ★ Open Data`_ skalę, tačiau adaptuota duomenų
struktūros aprašo kontekstui. Papildomai įtrauktas nulinis lygis, kai duomenys
nekaupiami, tačiau yra reikalingi ir yra parengtas jų :term:`duomenų struktūros
aprašas <DSA>`.

.. _5 ★ Open Data: https://5stardata.info/

Tim Berners Lee brandos lygius aprašo, kaip pavyzdį pasitelkiant duomenų
distribucijų formatus. Tačiau duomenų distribucijų formatai yra labai
netikslus pavyzdys. Rengiant duomenų struktūros aprašą, brandos lygis
vertinamas kiekvienam duomenų laukui atskirai, todėl tarkime CSV failas, gali
būti didesnio arba mažesnio nei trečias brandos lygis, priklausomai nuo CSV
faile esančių duomenų turinio. Tačiau grubiai vertinant, vidutiniškai CSV
failai turi daugiau ar mažiau 3 brandos lygį, koks ir yra nurodytas Tim
Berners Lee pavyzdžiuose.

Taip pat reikėtų atkreipti dėmesį, kad duomenų brandos lygis ar formatas nėra
susijęs su duomenų atvirumu. Duomenys gali būti pateikti aukščiausiu 5
brandos lygiu, tačiau pats duomenų prieinamumas gali būti visiškai uždaras,
siauram naudotojų ratui, kurie turi ribotą ir saugų prieigos kanalą prie
duomenų.

Rengiant duomenų struktūros aprašą, reikėtų nurodyti ne šaltinio duomenų
brandos lygį, o galutinį brandos lygį, kuris yra gaunamas atlikus visas
duomenų struktūros apraše nurodytas transformacijas.


.. describe:: level

    .. describe:: 0

        **Nekaupiama**

        Duomenys nekaupiami. Duomenų rinkinys užregistruotas atvirų duomenų
        portale. Užpildyta :data:`dataset` eilutė.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-0`.

    .. describe:: 1

        **Publikuojama**

        Duomenys publikuojami bet kokia forma. Užpildyta :data:`resource`
        eilutė.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-1`.

        Pirmu brandos lygiu žymimi duomenų laukai, kurių reikšmės neturi
        vientisumo, tarkime ta pati reikšmė gali būti pateikta keliais
        skirtingais variantais.

        **Pavyzdžiai**

        =================== ========== ============== ================
        datos               vienetai   pavadinimai    numeriai
        =================== ========== ============== ================
        vakar               1 m.       Įmonė          +370 345 36522
        2021 rugpjūčio 1 d. 1 m        UAB Įmonė      8 345 36 522
        1/9/21              1 metras   Įmonė, UAB     (83) 45 34522
        21/9/1              0.001 km   „ĮMONĖ“, UAB   037034536522
        =================== ========== ============== ================

        Pirmas brandos lygis suteikiamas tais atvejais, kei neįmanoma arba
        sudėtinga automatinėmis priemonėmis sutapatinti unikalią prasmę
        turinčių reikšmių arba kai duomenų struktūra nėra aiški ir neatitinka
        kokio nors vieno konkretaus šablono.

    .. describe:: 2

        **Struktūruota**

        Duomenys kaupiami struktūruota, mašininiu būdu nuskaitoma forma, bet
        kokiu formatu. Užpildytas :data:`property.source` stulpelis.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-2`.

        Antru brandos lygiu žymimi duomenų laukai, kurie pateikti vieninga
        forma arba pagal aiškų ir vienodą šabloną. Tačiau pateikimo būdas nėra
        standartinis. Nestandartinis duomenų formatas yra toks, kuris neturi
        viešai skelbiamos ir atviros formato specifikacijos arba kuris nėra
        priimtas kaip standartas, kurį prižiūri tam tikra standartizacijos
        organizacija.

        **Pavyzdžiai**

        ============== ============ ====================== ===================
        datos          vienetai     pavadinimai            numeriai
        ============== ============ ====================== ===================
        1/9/21         1 m.         UAB Pavadinimas        (83\) 111 11111
        2/9/21         2 m.         UAB Įmonė              (83\) 222 22222
        3/9/21         3 m.         UAB Organizacija       (83\) 333 33333
        4/9/21         4 m.         UAB Grupė              (83\) 444 44444
        ============== ============ ====================== ===================

        Pavyzdyje, datos formatas visur pateiktas vieningu formatu, tačiau pats
        formatas nėra standartinis. Lietuvoje, data yra užrašoma naudojanti
        ISO 8601 formatu.

        Skaičiai užrašyti tais pačiais vienetais, tačiau nėra nurodyta kokie
        tai vienetai, todėl neaišku, kaip interpretuoti šiuos skaičius.

        Įmonių pavadinimai nurodyti naudojanti valstybinį įmonių registrą,
        tačiau pavadinimai gali keistis, todėl geriausia vietoj pavadinimo
        naudoti tam tikrus identifikatorius, pavyzdžiui įmonės registracijos
        numerį.

    .. describe:: 3

        **Standartizuota**

        Duomenys saugomi atviru, standartiniu formatu. Užpildytas
        :data:`property.type` stulpelis ir duomenys atitinka nurodytą tipą.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-3`.

        Trečias brandos lygis suteikiamas tada, kai duomenys pateikti vieninga
        forma, vieningu masteliu, naudojamas formatas yra standartinis, tai
        reiškia, kad yra viešai skelbiama ir atvira formato specifikacija arba
        pats formatas yra patvirtintas ir prižiūrimas kokios nors
        standartizacijos organizacijos.

        **Pavyzdžiai**

        ============== =========== ================= ===================
        datos          vienetai    pavadinimai       numeriai
        ============== =========== ================= ===================
        2021-09-01     1           123456790         +37011111111
        2021-09-02     2           123456791         +37022222222
        2021-09-03     3           123456782         +37033333333
        2021-09-04     4           123456783         +37044444444
        ============== =========== ================= ===================

        Šiuo atveju, visos reikšmės pateiktos standartinėmis formomis.
        Vienetai pateikti ne prie skaičių, o atskirai metaduomenyse
        :data:`property.ref` stulpelyje.

    .. describe:: 4

        **Identifikuojama**

        Duomenų objektai turi aiškius, unikalius identifikatorius. Užpildyti
        :data:`model.ref` ir :data:`property.ref` stulpeliai.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-4`.

        Ketvirtas duomenų brandos lygis labiau susijęs ne su pačių duomenų
        formatu, bet su metaduomenimis, kurie lydi duomenis.

        Duomenų struktūros apraše :data:`model.ref` stulpelyje, pateikiamas
        objektą unikaliai identifikuojančių laukų sąrašas, o
        :data:`property.type` stulpelyje įrašomas `ref` tipas, kuris nurodo
        ryšį tarp dviejų objektų.

        **Pavyzdžiai**

        =============== ============ ============ =============== =============
        _id             datos        vienetai     pavadinimai     numeriai
        =============== ============ ============ =============== =============
        353e3a6d941b    2021-09-01   1            101ea064649b    +37011111111
        16d7418b8e1c    2021-09-02   2            1c0fa5297c0d    +37022222222
        495b9fb0f0b1    2021-09-03   3            0f14859b357a    +37033333333
        0a539b7e7e3c    2021-09-04   4            b14377855766    +37044444444
        =============== ============ ============ =============== =============

        Šiame pavyzdyje kiekvienam objektui arba kiekvienai lentelės eilutei
        yra sutiktas unikalus identifikatorius `_id`, kurio reikšmė niekada
        nesikeičia. Taip pat vietoj pavadinimu naudojami nesikeičiantys
        identifikatoriai.

        Kadangi kiekviena duomenų lentelės eilutė turi identifikatorių, todėl
        visi kiti stulpeliai įgauna 4 brandos lygį. Tai reiškia, kad 4
        brandos lygis susijęs, ne su konkrečių stulpelių reikšmėmis, o su tuo,
        ar eilutė, kurioje yra stulpelio reikšmė, turi unikalų identifikatorių
        ar ne.

        Rengiant duomenų struktūros aprašą, šiais identifikatoriais pasirūpinama
        automatiškai, jums reikia tik užpildyti `model.ref` ir pažymėti ryšius
        tarp modelių, užpildant `property.ref`, kuri `property.type` yra `ref`.


    .. describe:: 5

        **Susieta su išoriniu žodynu**

        Modeliai iš įstaigų duomenų rinkinių vardų erdvės susieti su modeliais
        iš standartų vardų erdvės, užpildytas :data:`base` eilutė. Standartų
        vardų erdvėje esantiems :term:`modeliams <modelis>` ir jų
        :term:`savybėms <savybė>` užpildytas :data:`uri` stulpelis.

        Daugiau apie vardų erdves skaitykite skyrelyje: :ref:`vardų-erdvės`.

        Plačiau apie brandos lygio kėlimą skaitykite skyriuje :ref:`to-level-5`.

        Penkto brandos lygio duomenys yra lygiai tokie patys, kaip ir ketvirto
        brandos lygio, tačiau penktame brandos lygyje, duomenys yra praturtinami
        metaduomenimis, pateikiant nuorodas į išorinius žodynus arba bend jau
        pateikiant aiškius pavadinimus ir aprašymus, užpildant `title` ir
        `description` stulpelius.

        Penktame brandos lygyje visas dėmesys yra sutelkiamas yra semantinę
        duomenų prasmę.


Daugeliu atveju brandos lygis gali būti nustatomas automatiškai pagal tai ar yra
užpildyti tam tikri stulpeliai. Automatiškai brandos lygio negalima nustatyti
tarp `2` ir `3` brandos lygio, todėl automatinės priemonės visada turėtų
parinkti žemesnį `2` brandos lygį, jei nenurodyta kitaip.

Jei žemesnėje dimensijoje nėra nurodytas joks brandos lygis, jis yra paveldimas
iš aukštesnės dimensijos.
