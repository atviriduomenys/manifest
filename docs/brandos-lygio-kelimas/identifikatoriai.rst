.. default-role:: literal
.. _identifikatoriai:

Identifikatoriai
################

:data:`level` = 4.


Objektų identifikavimas
=======================

Kadangi atvirų duomenų saugykloje duomenys turėtų būti saugomi normalizuotoje
formoje, susiejat lenteles tarpusavyje ryšiais, labai svarbu tinkamai
identifikuoti objektus.

Tarkim, jei turime tokius duomenis:

========  ===========
COUNTRIES
---------------------
code      country
========  ===========
lt        Lietuva
lv        Latvija
ee        Estija
========  ===========

Šioje lentelėje nėra pirminio rakto, todėl inventorizacijos lentelėje, `model`
eilėtės `ref` stulpelis yra tuščias:

+----+---+---+---+---+-----------+--------+-----+-----------+-------+
| id | d | r | b | m | property  | type   | ref | source    | level |
+====+===+===+===+===+===========+========+=====+===========+=======+
|    | datasets/gov/dc/countries |        |     |           |       |
+----+---+---+---+---+-----------+--------+-----+-----------+-------+
|    |   | sql                   |        |     |           |       |
+----+---+---+---+---+-----------+--------+-----+-----------+-------+
|    |   |   |   | Countries     |        |     | COUNTRIES |       |
+----+---+---+---+---+-----------+--------+-----+-----------+-------+
|    |   |   |   |   | code      | string |     | code      | 2     |
+----+---+---+---+---+-----------+--------+-----+-----------+-------+
|    |   |   |   |   | country   | string |     | country   | 2     |
+----+---+---+---+---+-----------+--------+-----+-----------+-------+

Tam, kad lentelę būtų galima sieti su kitomis lentelėmis reikia turėti patikimą
identifikatorių. Šiuo atveju, galima daryti prielaidą, kad laukas `code`
unikaliai identifikuoja `countries` modelio įrašus, todėl `model` ielutės `ref`
stulpeliui galima priskirti `code` reikšmę taip pakeliand modelio brandos lygį
iki 4.

+----+---+---+---+---+-----------+--------+------+-----------+-------+
| id | d | r | b | m | property  | type   | ref  | source    | level |
+====+===+===+===+===+===========+========+======+===========+=======+
|    | datasets/gov/dc/countries |        |      |           |       |
+----+---+---+---+---+-----------+--------+------+-----------+-------+
|    |   | sql                   |        |      |           |       |
+----+---+---+---+---+-----------+--------+------+-----------+-------+
|    |   |   |   | Countries     |        | code | COUNTRIES |       |
+----+---+---+---+---+-----------+--------+------+-----------+-------+
|    |   |   |   |   | code      | string |      | code      | 4     |
+----+---+---+---+---+-----------+--------+------+-----------+-------+
|    |   |   |   |   | country   | string |      | country   | 4     |
+----+---+---+---+---+-----------+--------+------+-----------+-------+

Šiuo atveju, laukas `code` yra šalies kodas, kuris unikaliai identifikuoja
objektą. Todėl galima šį lauką naudoti, kaip unikaliai identifikuojančią šalies
reikšmę.

Dažnai pasitaiko, kad neužtenka vieno lauko norint unikaliai identifikuoti
objektą, tokiu atveju, galima pateikti kelis laukus `ref` stulpelyje,
atskiriant juos kableliu.

Po pertvarkymų taip pat reikėtų nepamiršti atnaujinti `level` stulpelio
reikšmių, nurodant pasikeitusį brandos lygį. Kadangi atsirado galimybė
identifikuoti modelio objektus, `code` laukui suteikėme 4 brandos lygį.
Atitinkamai, pakeliam ir kitų laukų brandos lygį, kadangi įsitikinome, kad
automatiškai suteiktas `string` tipas yra teisingas, kas leidžia suteikti 3
brandos lygį, tačiau taip pat įsitikinome, kad nei vienas iš laukų nėra ryšio
su kita lentele laukas, todėl galime suteikti 4 brandos lygį.

Nei vienam iš šių laukų negalima suteikti 5 brandos lygio, kadangi `base`
eilutė yra tuščia.


Objektai be identifikatoriaus
=============================

Duomenų šaltinis ne visada leidžia unikaliai identifikuoti objektą. Pavyzdžiui,
jei turime tokią šaltinio lentelę:

===========  ==========
VILLAGES
-----------------------
name         population
===========  ==========
Gudeliai     28
Gudeliai     27
Gudeliai     19
===========  ==========

Lentelė objektas yra kaimo gyvenvietė, tačiau nėra jokio kaimo gyvenvietės
unikalaus identifikatoriaus. Lietuvoje gali būti daug gyvenviečių tokiu pačiu
pavadinimu, ką ir matome lentelėje. Jungti gyvenvietės pavadinimo su gyventojų
skaičiumi taip pat negalime, nes gyventojų skaičius gali sutapti su pavadinimu,
be to gyventojų skaičius nuolat kinta.

Šiuo atveju neturim jokios išeities ir vienintelis būdas pakelti šio rinkinio
brandos lygį, keičiant originalų duomenų šaltinį. Susidūrėme su nepakankamų
duomenų atveju.

Galutinė inventorizacijos lentelė turėtų atrodyti taip:

+----+---+---+---+---+------------+--------+-----+------------+-------+
| id | d | r | b | m | property   | type   | ref | source     | level |
+====+===+===+===+===+============+========+=====+============+=======+
|    | datasets/gov/dc/villages   |        |     |            |       |
+----+---+---+---+---+------------+--------+-----+------------+-------+
|    |   | sql                    |        |     |            |       |
+----+---+---+---+---+------------+--------+-----+------------+-------+
|    |   |   |   | Villages       |        |     | VILLAGES   |       |
+----+---+---+---+---+------------+--------+-----+------------+-------+
|    |   |   |   |   | name       | string |     | name       | 4     |
+----+---+---+---+---+------------+--------+-----+------------+-------+
|    |   |   |   |   | population | string |     | population | 4     |
+----+---+---+---+---+------------+--------+-----+------------+-------+


`name` ir `population` laukams suteikėme 4 brandos lygį, kadangi šie laukai
nėra `ref` tipo. Tačiau bendro modelio brandos lygio skaičiavime, šių laukų
brandos lygis bus nuleistas iki 3, kadangi modelis neturi identifikatoriaus,
todėl nė vienas laukas išskyrus `ref` tipo laukus, negali turėti didesnio
brandos lygio nei 4.

Inventorizacijos lentelėse, kiekvieno lauko brandos lygį galima žymėti
individualiai. Net jei modelis neturi identifikatoriaus, tačiau tam tikras
laukas nėra `ref` tipo ir to lauko duomenys tvarkingi ir atitinka lauko duomenų
tipą, lauko pavadinimai naudoja manifesto žodyno pavadinimus, tada tam laukui
galima suteikti 5 brandos lygį. Tačiau reikia atkreipti dėmesį, kad bendro
brandos lygio skaičiavimuose, šio lauko brandos lygis gali būti sumažintas, jei
modelis neatitinka tam tikrų kriterijų, pavyzdžiui jei modelis neturi unikalaus
identifikatoriaus.


Ryšiai tarp lentelių
====================

Labai svarbu atveriant duomenis nepamesti ryšių tarp lentelių. Turint
veikiančius ryšius tarp lentelių atsiranda galimybė duomenis jungti
tarpusavyje, o tai yra labai svarbu.

Tarkime, duomenų šaltinyje yra tokios dvi lentelės:


=======  ========  ===========
COUNTRIES
------------------------------
id       code      country
=======  ========  ===========
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ===========


=======  ========  ===========
CITIES
------------------------------
id       country   city
=======  ========  ===========
1        1         Vilnius
2        1         Kaunas
3        1         Klaipėda
=======  ========  ===========

Iš šių lentelių gauname tokią inventorizacijos lentelę:

+----+---+---+---+---+------------+---------+-----------+-----------+-------+
| id | d | r | b | m | property   | type    | ref       | source    | level |
+====+===+===+===+===+============+=========+===========+===========+=======+
|    | datasets/gov/dc/countries  |         |           |           |       |
+----+---+---+---+---+------------+---------+-----------+-----------+-------+
|    |   | sql                    |         |           |           |       |
+----+---+---+---+---+------------+---------+-----------+-----------+-------+
|    |   |   |   | Countries      |         | id        | COUNTRIES |       |
+----+---+---+---+---+------------+---------+-----------+-----------+-------+
|    |   |   |   |   | id         | integer |           | id        | 4     |
+----+---+---+---+---+------------+---------+-----------+-----------+-------+
|    |   |   |   |   | code       | string  |           | code      | 4     |
+----+---+---+---+---+------------+---------+-----------+-----------+-------+
|    |   |   |   |   | country    | string  |           | country   | 4     |
+----+---+---+---+---+------------+---------+-----------+-----------+-------+
|    |   |   |   | Cities         |         | id        | CITIES    |       |
+----+---+---+---+---+------------+---------+-----------+-----------+-------+
|    |   |   |   |   | id         | integer |           | id        | 4     |
+----+---+---+---+---+------------+---------+-----------+-----------+-------+
|    |   |   |   |   | country    | ref     | countries | country   | 4     |
+----+---+---+---+---+------------+---------+-----------+-----------+-------+
|    |   |   |   |   | city       | string  |           | city      | 4     |
+----+---+---+---+---+------------+---------+-----------+-----------+-------+

Kaip matome ryšys tarp lentelių buvo aptiktas automatiškai, kadangi tokia
informacija yra pateikta duomenų bazės schemoje. Tačiau gali pasitaikyti
atvejai, kad ryšiai tarp lentelių nėra aprašyti duomenų bazės schemoje, tokiais
atvejais, ryšius reikia aprašyti rankiniu būdu.

Norint nurodyti ryšį su kita lentele, reikia lauko `type` stulpelyje nurodyti
`ref`, o `ref` stulpelyje nurodyti kitos lentelės pavadinimą iš `model`
stulpelio.

Ryšiai tarp lentelių gali būti nurodomi tik vieno duomenų rinkinio resurso
ribose.

Laukai naudojami ryšiams tarp lentelių automatiškai nustatomi pagal rodomo
modelio `ref` reikšmes. Pavyzdžiui šiuo atveju modelio `countries` eilutės
`ref` reikšmė yra `id`, todėl modelio `cities` savybė `country` automatiškai
siejama su `id` lauku. Tačiau galima laukus, nurodyti ir rankiniu būdu taip:
`countries[id]`.

Atveriant duomenis, vidinės duomenų bazės identifikatoriai nėra perkeliami.
Visi identifikatoriai generuojami naujai, kad neatskleisti vidinės duomenų
bazės detalių.

Jei šaltinio lentelės yra susietos naudojant daugiau nei vieną lauką, `source`
stulpelyje galima nurodyti kelis laukus, atskiriant juos kableliu. Arba
`property` eilutės `ref` stulpelyje galima nurodyti kelis laukus taip
`countries[id,code]`.


Sudėtiniai identifikatoriai
===========================

Dažnai pasitaiko, kad informacinių objektų negalima identifikuoti kurios nors
vienos savybės pagalba. Tokiais atvejais, tenka pasitelkti sudėtinius
identifikatorius, kur vienas informacinis objektas identifikuojamas kelių
savybių pagalba.

Kaip pavyzdį galime panagrinėti šį duomenų šaltinį

========  ===========
CITIES
---------------------
COUNTRY   CITY
========  ===========
Lietuva   Vilnius
Lietuva   Kaunas
Latvija   Ryga
========  ===========


=======  ========  ===========  =================
STREETS
-------------------------------------------------
ID       COUNTRY   CITY         STREET
=======  ========  ===========  =================
1        Lietuva   Vilnius      Gedimino pr.
2        Lietuva   Vilnius      Vilniaus g.
3        Lietuva   Vilnius      Konstitucijos pr.
=======  ========  ===========  =================

Čia matome, kad `STREETS` lentelė siejasi su `CITIES` lentele, tačiau sąsajai
tarp lentelių neužtenka vieno lauko. Norinti unikaliai identifikuoti `CITIES`
:term:`objektą <objektas>` būtina naudoti dvi `country` ir `city` :term:`savybes
<savybė>`.

Tokią duomenų struktūrą galima aprašyti taip:

+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
| id | d | r | b | m | property   | type    | ref       | source  | prepare            | level | access  |
+====+===+===+===+===+============+=========+===========+=========+====================+=======+=========+
|  1 | datasets/gov/dc/countries  |         |           |         |                    |       |         |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
|  2 |   | db                     | sql     |           |         |                    |       |         |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
|  3 |   |   |   | City           |         | id        | CITIES  |                    |       |         |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
|  4 |   |   |   |   | id         | array   |           |         | country, name      | 4     | private |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
|  5 |   |   |   |   | country    | string  |           | COUNTRY |                    | 3     | open    |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
|  6 |   |   |   |   | name       | string  |           | CITY    |                    | 3     | open    |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
|  7 |   |   |   | Street         |         | id        | STREET  |                    |       |         |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
|  8 |   |   |   |   | id         | integer |           | ID      |                    | 4     | private |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
|  9 |   |   |   |   | country    | string  |           | COUNTRY |                    | 3     | open    |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
| 10 |   |   |   |   | city_name  | string  |           | CITY    |                    | 3     | private |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
| 11 |   |   |   |   | city       | ref     | city      |         | country, city_name | 4     | open    |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+
| 12 |   |   |   |   | name       | string  |           | STREET  |                    | 3     | open    |
+----+---+---+---+---+------------+---------+-----------+---------+--------------------+-------+---------+

Tam, kad `city` lentelei aprašyti kompozicinį raktą, 4-oje eilutėje buvo
įtraukta nauja savybė `id`, kuri tiesioginio analogo pirminiame duomenų
šaltinyje neturi, todėl šios savybės :data:`property.source` yra tuščias, tačiau
šios savybės reikšmė gaunama :data:`property.prepare` pagalba, kur nurodyta, kad
reikšmė gaunama apjungiant `country` ir `name` :term:`savybes <savybė>`.

Analogiška situacija ir su `street` :term:`modeliu <modelis>`.

`street.city_name` :data:`property.access` pažymėtas `private`, kadangi miesto
pavadinimas yra perteklinė informacija. Miesto pavadinimą galima gauti
apjungiant `city` ir `street` :term:`modelius <modelis>`.


Globalūs identifikatoriai
=========================

Dažniausiai nėra didelių problemų su lokaliais, vieno duomenų rinkinio ribose
naudojamais identifikatoriais. Objektus galima jungti tarpusavyje, tačiau tik
vieno duomenų rinkinio ribose.

Atsiveria žymiai didesnės galimybės, jei objektus galima jungti ir už vieno
rinkinio ribų, su visais kitais, visuose kituose rinkiniuose esančiais
objektais.

Kad tai veiktų, naudojami globalūs objektų identifikatoriai. Iliustruosiu, kaip
visa tai veikia pavyzdžiu. Tarkime turime tokią lentelę viename duomenų
rinkinyje:

=======  ========  ===========
COUNTRIES
------------------------------
id       code      country
=======  ========  ===========
1        ltu       Lithuania
2        lva       Latvia
3        est       Estonia
=======  ========  ===========

Ir kitą lentelę, kitame duomenų rinkinyje:

=======  ========  ===========
SALYS
------------------------------
id       kodas     salis
=======  ========  ===========
9        lt        Lietuva
8        lv        Latvija
7        ee        Estija
=======  ========  ===========

Abu duomenų rinkiniais valdomi skirtingose įstaigose, nors abu rinkiniai apie
tą patį šalies objektą, tačiau vidiniai identifikatoriai skirtingi, žodynas
taip pat skirtingas ir net patys duomenys yra skirtingi. Iš esmės nėra
galimybės šių duomenų sujungti tarpusavyje.

Tačiau mums pasisekė, nes yra dar trečias duomenų šaltinis su šalių kodais:

==  ===
CODES
-------
A2  A3
==  ===
lt  ltu
lv  lva
ee  est
==  ===

Pasitelkus šį trečiąjį duomenų šaltinį sujungti visas lenteles pasidaro
įmanoma.

Galutinė, pilnai sutvarkyta visų trijų duomenų rinkinių inventorizacijos
lentelė atrodytų taip:

+----+---+---+---+---+------------+-----------+---------+--------+-------+
| id | d | r | b | m | property   | source    | type    | ref    | level |
+====+===+===+===+===+============+===========+=========+========+=======+
|    | datasets/gov/dp1/countries |           |         |        |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   | sql                    |           |         |        |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   | /place/Country     |           |         | a3code |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   |   | Countries      | COUNTRIES |         | id     |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   |   |   | id         | id        | integer |        | 3     |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   |   |   | a3code     | code      | string  |        | 2     |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   |   |   | name.en    | country   | text    |        | 2     |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    | datasets/gov/dp2/countries |           |         |        |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   | sql                    |           |         |        |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   | /place/Country     |           |         | a2code |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   |   | Salys          | SALYS     |         | id     |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   |   |   | id         | id        | integer |        | 5     |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   |   |   | a2code     | kodas     | string  |        | 5     |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   |   |   | name.lt    | salis     | text    |        | 5     |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    | datasets/gov/dp3/countries |           |         |        |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   | sql                    |           |         |        |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   | /place/Country     |           |         | a3code |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   |   | Codes          | CODES     |         | a3code |       |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   |   |   | a2code     | A2        | string  |        | 5     |
+----+---+---+---+---+------------+-----------+---------+--------+-------+
|    |   |   |   |   | a3code     | A3        | string  |        | 5     |
+----+---+---+---+---+------------+-----------+---------+--------+-------+


Žodyno lentelė turėtų atrodyti taip:

+----+---+-----------+--------+
| id | m | property  | type   |
+====+===+===========+========+
|    | place/Country |        |
+----+---+-----------+--------+
|    |   | a2code    | string |
+----+---+-----------+--------+
|    |   | a3code    | string |
+----+---+-----------+--------+
|    |   | name      | text   |
+----+---+-----------+--------+

Duomenų atvėrimo metu, visi inventorizuoti duomenų rinkiniai bus siejami su
žodyno modeliais pasitelkiant identifikatorių nurodytą :data:`base.ref`
stulpelyje. Jei duomenų rinkinio modelis neturi tokio lauko, tada susiejimas
nebus daromas ir viso modelio brandos lygis nukris iki 4 brandos lygio.

Duomenų atvėrimo metu atskirų duomenų rinkinių duomenys bus saugomi atskirai,
kadangi jie gali turėti laukų ne iš žodyno. Iš visų duomenų rinkinių bus kuriami
ir globalūs, nuo konkretaus duomenų rinkinio nepriklausomi žodynų objektai.

Konkrečiai šiuo atveju `place/country` žodyno lentelė atvėrus duomenis atrodys
taip:

=======  ======  ======  ===========  ===========
place/country
-------------------------------------------------
id       a2code  a3code  name.en      name.lt
=======  ======  ======  ===========  ===========
1        lt      ltu     Lithuania    Lietuva
2        lv      lva     Latvia       Latvija
3        ee      est     Estonia      Estija
=======  ======  ======  ===========  ===========

Kaip matote, iš pirmo žvilgsnio atrodė, kad dviejų duomenų rinkinių neįmanoma
sujungti tarpusavyje, tačiau prijungus dar daugiau duomenų rinkinių, kaip kokia
dėlionė iš mažų detalių susidėliojo pilna ir išsami modelio `place/country`
lentelė.
