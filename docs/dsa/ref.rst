.. default-role:: literal

.. _ryšiai:

Ryšiai tarp modelių
###################

Pateikiant metaduomenis apie ryšius tarp modelių, duomenų :ref:`brandos lygis
<level>` pakeliamas iki ketvirto lygio.

Ryšiai tarp modelių aprašomi tais atvejais, kai vienoje duomenų lentelėje
naudojami identifikatoriai iš kitos lentelės.

Jungimas per pirminį raktą
==========================

Pavyzdžiui, jei turime tokias dvi duomenų lenteles:

== ======= ====
Country
---------------
id name    code
== ======= ====
1  Lietuva lt
2  Latvija lv
== ======= ====

== ======= =======
City
------------------
id name    country
== ======= =======
1  Vilnius lt
2  Kaunas  lt
3  Ryga    lv
== ======= =======

Šiuo atveju, jei norime parengti aukčiau pateiktų duomenų struktūros aprašą,
jis atrodytų taip:


== == == == == ================== ========= =========== =====
d  d  r  b  m  property           type      ref         level
== == == == == ================== ========= =========== =====
1  datasets/gov/example/countries
-- ------------------------------ --------- ----------- -----
2           Country                         code
-- -- -- -- --------------------- --------- ----------- -----
3              id                 integer               4
4              name               string                4
5              code               string                4
6           City                            id
-- -- -- -- --------------------- --------- ----------- -----
7              id                 integer               4
8              name               string                4
9              country            ref       Country     4
== == == == == ================== ========= =========== =====

Šiame duomenų struktūros apraše, 9-oje eilutėje `country` stulpelio tipas yra
`ref`, tai reiškia, kad šis stulpelis yra kito modelio išorinis raktas.
`property.ref` stulpelyje nurodyta kurio modelio išorinis raktas šis
stulpelis yra. Šiuo atveju, tai yra `Country` modelis, kuris apibrėžtas 2-oje
eilutėje.

Pagal nutylėjimą, ryšys su kitu modeliu nustatomas naudojant kitos lentelės
pirminį raktą nurodytą :data:`model.ref` stulpelyje. Šiuo atveju, `City
.country` yra jungiamas per `Country.code`. Tai reiškia, kad `City.country`
duomenų tipas turi sutapti su `Country.code` duomenų tipu, kuris yra `string`.

`property.ref` reikšmė gali būti pateikiama vienu iš šių variantų:

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
        :data:`model.ref`, galima nurodyti :data:`property` iš :data:`model`.

    .. describe:: model[*property]

        Jei susiejimui reikia daugiau nei vieno duomenų lauko ir jie nesutampa
        su model.ref, tada galima nurodyti kelias property reikšmes atskirtas
        kableliu. Tačiau šiuo atveju taip pat būtina nurodyti ir
        :data:`property.prepare` kelias reikšmes atskirtas kableliu, o
        :data:`property.source` reikšmė turi būti tuščia.
        :data:`property.prepare` stulpelyje nurodomi kiti modelio
        :data:`property` pavadinimai iš kurių duomenų reikšmių turi būti
        formuojamas sudėtinis raktas.


Jungimas per nepirminį raktą
============================

Jei modelius reikia jungti ne per pirminį raktą, o per kitus laukus, tada
naudojama `model[property]` forma.

Pavyzdžiui, jei turime tokius duomenis:

== ======= ====
Country
---------------
id name    code
== ======= ====
1  Lietuva lt
2  Latvija lv
== ======= ====

== ======= =======
City
------------------
id name    country
== ======= =======
1  Vilnius lt
2  Kaunas  lt
3  Ryga    lv
== ======= =======

Kur `Country` pirminis raktas yra `id` ir norime jungti `City.country` per
`Country.code`, tuomet duomenų struktūros aprašas atrodys taip:

== == == == == ================== ========= ================= =====
d  d  r  b  m  property           type      ref               level
== == == == == ================== ========= ================= =====
1  datasets/gov/example/countries
-- ------------------------------ --------- ----------------- -----
2           Country                         id
-- -- -- -- --------------------- --------- ----------------- -----
3              id                 integer                     4
4              name               string                      4
5              code               string                      4
6           City                            id
-- -- -- -- --------------------- --------- ----------------- -----
7              id                 integer                     4
8              name               string                      4
9              country            ref       Country[code]     4
== == == == == ================== ========= ================= =====

9-oje eilutėje `property.ref` stulpelyje pateikta `Country[code]` reikšmė, kuri
`Country` nurodo su kokiu modeliu jungiame, o `code` nurodo su kokiu `Country`
stulpeliu jungiame. Jei pateiktas tik modelis, tada jungiama per to modelio
pirminį raktą, jei pateiktas stulpelis laužtiniuose skliausteliuose, tada
jungiama per nurodytą stulpelį.


Jungimas per kompozicinį raktą
==============================

Jei modelius reikia jungti per kelis laukus, tada naudojama
`model[*property]` forma, kur laužtiniuose skliaustuose pateikiami keli
stulpeliai atskirti kableliais.

Pavyzdžiui, jei turime tokius duomenis:

== ======= ====
Country
---------------
id name    code
== ======= ====
1  Lietuva lt
2  Latvija lv
== ======= ====

== ======= ======= ==========
City
-----------------------------
id name    country country_id
== ======= ======= ==========
1  Vilnius lt      1
2  Kaunas  lt      1
3  Ryga    lv      2
== ======= ======= ==========

Kur `City` su `Country` yra jungiamas per du `country` ir `country_id`
stulpelius, tuomet reikia įtraukti išvestinį duomenų lauką, kuriame formulės
įrašomos į :data:`property.prepare` pagalba apjungiami keli laukai į vieną
kompozicinį raktą. Šiuo atveju duomenų struktūros aprašas atrodys taip:

== == == == == ================== ========= ================ ========================== =====
d  d  r  b  m  property           type      ref              prepare                    level
== == == == == ================== ========= ================ ========================== =====
1  datasets/gov/example/countries
-- ------------------------------ --------- ---------------- -------------------------- -----
2           Country                         id
-- -- -- -- --------------------- --------- ---------------- -------------------------- -----
3              id                 integer                                               4
4              name               string                                                4
5              code               string                                                4
6           City                            id
-- -- -- -- --------------------- --------- ---------------- -------------------------- -----
7              id                 integer                                               4
8              name               string                                                4
9              country_code       string                                                4
10             country_id         integer                                               4
11             country            ref       Country[id,code] country_id, country_code   4
== == == == == ================== ========= ================ ========================== =====

Čia matome, kad 11-oje eilutėje buvo įtrauktas išvestinis laukas `country`,
kuris išskaičiuojamas apjungiant `country_id` ir `country_code`. O ryšiui su
`Country`, laužtiniuose skliausteliuose nurodyti du laukai iš jungiamo
`Country` modelio. Abiejų jungiamų pusių pateiktas laukų sąrašas turi būti
vienodo eiliškumo, o jungiami laukai turi turėti vienodus tipus.

Jei `Country` pirminis raktas būtų kompozicinis, pavyzdžiui `id, code`,
tuomet, 11-oje eilutėje `property.ref` užtektu nurodyti tik `Country`.


.. _atgalinis-ryšys:

Jungimas atgaliniu ryšiu
========================

.. note:: Tokio tipo jungimas kol kas dar nėra įgyvendintas.

Jungiant modelius atgaliniu ryšiu kuriamas išvestinis arba virtualus laukas,
kuriame analogiškai kaip ir paprasto ryšio atveju, apjungiami du modeliai,
tik šiuo atveju kuriamas daug su vienas tipo ryšys.

Pavyzdžiui, jei turime tokius duomenis:

== =======
Country
----------
id name
== =======
1  Lietuva
2  Latvija
== =======

== ======= =======
City
------------------
id name    country
== ======= =======
1  Vilnius 1
2  Kaunas  1
3  Ryga    2
== ======= =======

Tai norint sukurti atgalinį ryšį iš `City` modelio į `Country` modelį, duomenų
struktūros aprašas atrodys taip:

== == == == == ================== ========= ================ =====
d  d  r  b  m  property           type      ref              level
== == == == == ================== ========= ================ =====
1  datasets/gov/example/countries
-- ------------------------------ --------- ---------------- -----
2           Country                         id
-- -- -- -- --------------------- --------- ---------------- -----
3              id                 integer                    4
4              name               string                     4
5              cities             backref   City             4
6           City                            id
-- -- -- -- --------------------- --------- ---------------- -----
7              id                 integer                    4
8              name               string                     4
9              country            ref       Country          4
== == == == == ================== ========= ================ =====

Čia atgalinis ryšys nurodytas 5-oje eilutėje, pateikiant virtualų
`Country.cities` lauką, kuris jungiamas per `City.country` lauką, kadangi
`City.country` turi ryšį su `Country`.

Jei `City` modelyje būtų pateikti keli stulpeliai susieti su `Country`, tada
5-oje eilutėje `property.ref` reikšmė turėtų nurodyti konkretų lauką, per
kurį jungiama, pavyzdžiui `City[country]`.


.. _polimorfinis-ryšys:

Polimorfinis jungimas
=====================

.. note:: Tokio tipo jungimas kol kas dar nėra įgyvendintas.

Polimorfinis jungimas yra toks ryšys tarp modelių, kai vieno modelio laukas
yra siejamas su daugiau nei vienu kitu modeliu. Tokiam ryšiui nurodyti
polimorfinis laukas turi dvi reikšmes, išorinio modelio pavadinimą ir to
modelio stulpelio per kurį jungiama reikšmę.

== =======
Country
----------
id name
== =======
1  Lietuva
2  Latvija
== =======

== ======= =======
City
------------------
id name    country
== ======= =======
1  Vilnius 1
2  Ryga    2
== ======= =======

== ============ ========= ======================================
Event
----------------------------------------------------------------
id name         object_id object_model
== ============ ========= ======================================
1  Gimtadienis  1         datasets/gov/example/countries/Country
2  Gimtadienis  2         datasets/gov/example/countries/Country
3  Gimtadienis  1         datasets/gov/example/countries/City
4  Gimtadienis  2         datasets/gov/example/countries/City
== ============ ========= ======================================

Pavyzdyje aukščiau matome, kad yra du modeliai `Country` ir `City`, kuriuos
jungia `Event` modelis per `object_id` ir `object_model` laukus. Pavyzdžiui
`Event` kurio `id` yra 1, siejamas su `Country` modeliu, kurio `id` yra 1.

Tokių duomenų struktūros aprašas atrodys taip:

== == == == == ================== ========= ======= ======================= =====
d  d  r  b  m  property           type      ref     prepare                 level
== == == == == ================== ========= ======= ======================= =====
1  datasets/gov/example/countries
-- ------------------------------ --------- ------- ----------------------- -----
2           Country                         id
-- -- -- -- --------------------- --------- ------- ----------------------- -----
3              id                 integer                                   4
4              name               string                                    4
5              cities             backref   City                            4
6           City                            id
-- -- -- -- --------------------- --------- ------- ----------------------- -----
7              id                 integer                                   4
8              name               string                                    4
9              country            ref       Country                         4
10          Event                           id
-- -- -- -- --------------------- --------- ------- ----------------------- -----
11             id                 integer                                   4
12             name               string                                    4
13             object_id          integer                                   4
14             object_model       string                                    4
15             object             generic   Country object_model, object_id 4
16                                          City
== == == == == ================== ========= ======= ======================= =====

15-oje eilutėje įtrauktas virtualus `Event.object` laukas, kuris 15-oje ir
16-oje eilutėse, :data:`property.ref` stulpelyje išvardina du modelius
`Country` ir City`, su kuriais jungiamas šis laukas, per `object_model` ir
`object_id` laukus, kurie aprašyti atskirai.

`object_id` ir `object_model` aprašomi atskirai tik todėl, kad duomenys
ateina iš išorinio šaltinio. Jie duomenys rašomi tiesiogiai į :ref:`Saugyklą
<saugykla>`, tada atskirai `generic` laukų apsirašyti nereikia.