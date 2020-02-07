.. default-role:: literal

.. _inventorying:

Inventorizavimas
################

Pirminė inventorizacija atliekama metaduomenų lentelės pagalba. Tokią lentelę
galima automatiškai generuoti iš duomenų šaltinio naudojantis
`scripts/list-sql-schema.py` įrankio pagalba.

Tarkime, jei turime duomenų šaltinį, kuriame yra lentelė pavadinimu
`COUNTRIES`, o lentelės turinys atrodo taip:

=======  ========  ===========
COUNTRIES
------------------------------
id       code      country
=======  ========  ===========
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ===========

Tada galime leisti įrankį nurodant inventorizacijos lentelės generavimo
taisykles. Pavyzdžiui tai galėtų atrodyti taip:

.. code-block:: sh

    scripts/list-sql-schema.py \
      driver://user:password@host/name \
      --dataset=gov/dc/countries \
      --resource=sql \
      --model='raw/dc/{table}' \
      -o inventorizacija.csv

Komanda sukurs `inventorizacija.csv` failą, kuriame bus tokie duomenys:

================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref  const  title   description  table         column
================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     _id       pk      \    \      \       \            COUNTRIES     id
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \    \      \       \            COUNTRIES     code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     country   string  \    \      \       \            COUNTRIES     country
================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======


Kol kas nesigilinsime į visų lentelės stulpelių paskirtį, kadangi tam tikrų
stulpelių panaudojimas bus aptartas atskirai. Kas šiame pavyzdyje yra aktualu:

:dataset:
  Tai yra duomenų rinkinio pavadinimas, kuris atitinka `dcat:Dataset`_.

  Duomenų rinkinio pavadinime galima naudoti vardų erdves. Pavyzdyje, duomenų
  rinkinio `gov/dc/countries` vardų erdvė yra `gov/dc`. Rekomenduojama
  valstybinėms įstaigoms naudoti `gov/` vardų erdvę, taip pat nurodant įstaigos
  trumpinį, kuris šiuo atveju yra `dc/`. Paskutinis komponentas yra toje
  įstaigoje esančio duomenų rinkinio pavadinimas. Jei įstaiga turi daug duomenų
  rinkinių, galima pasitelkti daugiau vardų erdvės dalių, pavyzdžiui
  `gov/dc/geo/countries`.

  Duomenų rinkinio pavadinimas naudojamas automatiniam duomenų rinkinių
  sinchronizavimui su atvirų duomenų vitrina `data.gov.lt`_.

.. _`dcat:Dataset`: https://www.w3.org/TR/vocab-dcat-2/#Class:Dataset
.. _data.gov.lt: https://data.gov.lt/

:resource:
  Duomenų rinkinyje esančio resurso pavadinimas, atitinka `dcat:Resource`_.

.. _`dcat:Resource`: https://www.w3.org/TR/vocab-dcat-2/#Class:Distribution

:model:
  Duomenų modelio, pavadinimas. Generuojant inventorizacijos lentelę šis
  pavadinimas atitinka nurodytą šabloną `--model='raw/dc/{table}'`. Jei
  nekeičiami originalūs duomenų šaltinio pavadinimai, rekomenduojama naudoti
  `raw/` prefiksą, kuris nurodo, kad duomenys yra žali, netvarkyti.

  Modelio pavadinime galima naudoti vardų erdves. Šiuo atveju modelio
  `raw/dc/COUNTRIES` vardų erdvė yra `raw/dc`.

:property:
  Duomenų lauko pavadinimas. Kaip matote, laukas `id` buvo automatiškai
  pakeistas į `_id`. Taip atsitiko todėl, kad įrankis automatiškai atpažino
  lentelėje esantį pirminį raktą. Atvirų duomenų saugykloje pirminis raktas
  gali būti tik vienas ir pirminio rakto laukas yra privalomas. Todėl visi
  modeliai privalomai turi `_id` lauką, kuris visada yra pirminis raktas.

  Dar vienas pastebėjimas, kad visi laukų pavadinimai, kurie prasideda `_`
  simboliu yra rezervuoti ir turi tam tikrą paskirtį. Įprastiniai laukų
  pavadinimai negali prasidėti `_` simboliu.

  Jei `property` stulpelio reikšmė yra tuščia, tada kai kurie laukai keičia
  prasmę ir persijungia iš laukams skirtų metaduomenų į modeliui skirtus
  metaduomenis. Laukai kurie keičia prasmę yra `title`, `description` ir
  `table`.

:type:
  Atvirų duomenų saugykla turi turtingą tipų sistemą, todėl svarbu nurodyti
  rinkamus tipus. Įrankis automatiškai bando atpažinti tipus automatiškai,
  tačiau automatinis atpažinimas ne visada suveikia. Pavyzdžiui `date` laukas
  gali būti atpažintas, kaip `string`.

  Galima naudoti šiuos tipus: `pk`, `ref`, `string`, `integer`, `number`,
  `boolean`, `binary`, `date`, `datetime`, `file`.

:title:
  Modelio ar duomenų lauko pavadinimas skirtas žmonėms. Norint nurodyti modelio
  pavadinimą, `property` stulpelis turi būti tuščias.

:description:
  Modelio ar duomenų lauko aprašymas. Norint pateikti modelio aprašymą
  `property` stulpelis turi būti tuščias. Iš šio aprašymo generuojama
  dokumentacija, todėl aprašyme reikėtų pateikti informaciją, kuri padėtų
  suprasti kaip naudoti duomenis.

:table:
  Originalus duomenų šaltinio lentelės pavadinimas. Automatinės priemonės
  automatiškai skaitys duomenis iš šios lentelės ir nuskaitytus duomenis saugos
  atitinkamoje `model` stulpelio lentelėje.

  Jei `property` stulpelio reikšmė yra tuščia, tuomet šiame stulpelyje galima
  įrašyti RQL užklausą lentelei filtruoti.

:column:
  Originalus duomenų šaltinio lentelės lauko pavadinimas. Analogiškai, kaip ir
  su `table` stulpeliu, duomenys bus skaitomi iš šio stulpelio ir saugomi
  atitinkamame `property` stulpelyje atveriant duomenis.

Jei yra poreikis, galima pridėti daugiau stulpelių, savo nuožiūra, visi kiti
stulpeliai einantys po `column` bus ignoruojami. Visi kiti stulpelių
pavadinimai turi būti tiksliai tokie, kokie pateikti pavyzdyje.

Tokia automatiškai parengta inventorizacijos lentelė gali būti naudojama
atveriant duomenis.

Inventorizacijos lentelė yra tik pagalbinė priemonė atveriamų duomenų laukų
sąrašams. Šios lentelės pagrindu yra kuriama manifesto YAML failai, tai galima
padaryti taip:

.. code-block:: sh

    scripts/csv-to-manifest inventorizacija.csv

Ši komanda sukurs `manifest/datasets/gov/dc/countries.yml` failą. Šį YAML failą
naudoja praktiškai visos priemonės, kadangi inventorizacijos lentelėje yra
pateikia tik pati svarbiausia metaduomenų dalis, o YAML faile, galima pateikti
žymiai daugiau metaduomenų.

Keičiant YAML failus, galima juos perrašyti naudojant inventorizacijos lentelę.
Perrašymo metu, bus išlaikomi visi pakeitimai YAML faile, kurių nėra
inventorizacijos lentelėje. Tai leidžia keisti tiek inventorizacijos lentelę,
tiek YAML failą vienu metu.

Inventorizacijos lentelė, gali generuoti daug YAML failų. YAML failo kelias
atitinka `dataset` stulpelio reikšmę.

Galiausiai, naudojantis YAML faile esančiais duomenų aprašais, galima
importuoti duomenis iš šaltinio į atvirų duomenų saugyklą:


.. code-block:: sh

  spinta pull gov/dc/countries

Po šio žingsnio pirminis duomenų atvėrimas yra baigas. Žinoma duomenys yra žali
ir visiškai netvarkyti. Yra visa eilė metaduomenų tvarkymo darbų, kuriuos
aptarsime žemiau.


Duomenų laukų atranka
=====================

Dažniausiai negalima atverti visų duomenų laukų, todėl reikia vykdyti atvertinų
duomenų laukų atranką.

Norint, kad tam tikri laukai nepatektų į YAML failus, užtenka ištrinti
`dataset` stulpelio reikšmę. Jei lauko nebus YAML faile, šis laukas nebus
atvertas.

Rekomenduojama netrinti laukų, kurių neplanuojama atverti, o tiesiog ištrinti
`dataset` stulpelio reikšmę. Tokiu būdu mus galimybė, bet kada apsigalvoti ir
grąžinti lauką atvėrimui.

Imant tą patį pavyzdį:

================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref  const  title   description  table         column
================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     _id       pk      \    \      \       \            COUNTRIES     id
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \    \      \       \            COUNTRIES     code
\                 sql       \       raw/dc/COUNTRIES     country   string  \    \      \       \            COUNTRIES     country
================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======

Kadangi `country` duomenų lauko `dataset` reikšmė yra tuščia, šis laukas nebus
atvertas.


Objektų identifikavimas
=======================

Kadangi į atvirų duomenų saugykloje duomenys turėtų būti perkeliami
normalizuotoje formoje, susiejat lenteles tarpusavyje ryšiais, labai svarbu
tinkamai identifikuoti objektus.

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

Šioje lentelėje nėra pirminio rakto, todėl inventorizacijos lentelėje nėra
privalomo `_id` lauko:

================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref  const  title   description  table         column
================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \    \      \       \            COUNTRIES     code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     country   string  \    \      \       \            COUNTRIES     country
================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======

Atveriant duomenis, kiekvienas įrašas privalo turėti unikalų identifikatorių.
Jei lentelė neturi pirminio rakto, `_id` lauką reikia pridėti rankomis,
įterpiant naują eilutę:

================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref  const  title   description  table         column
================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     _id       pk      \    \      \       \            COUNTRIES     code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \    \      \       \            COUNTRIES     code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     country   string  \    \      \       \            COUNTRIES     country
================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======

Šiuo atveju, laukas `code` yra šalies kodas, kuris tikriausiai unikaliai
identifikuoja objektą. Todėl galima šį lauką naudoti, kaip unikaliai
identifikuojantį šalies objektą.

Dažnai pasitaiko, kad neužtenka vieno lauko norint unikaliai identifikuoti
objektą, tokiu atveju, galima pateikti kelis laukus `column` stulpelyje,
atskiriant juos kableliu.

Jei vis dėl to pasirinktas stulpelis unikaliai neidentifikuoja objekto, tada
duomenų importavimo metu, besidubliuojantys objektai nebus importuoti. Pirmas
importuotas objektas bus pažymėtas, kaip turintis klaidą.


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

================  ========  ======  ===================  ========  ======  ================  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref               const  title   description  table         column
================  ========  ======  ===================  ========  ======  ================  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     _id       pk      \                 \      \       \            COUNTRIES     id
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \                 \      \       \            COUNTRIES     code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     country   string  \                 \      \       \            COUNTRIES     country
gov/dc/countries  sql       \       raw/dc/CITIES        _id       pk      \                 \      \       \            CITIES        id
gov/dc/countries  sql       \       raw/dc/CITIES        country   ref     raw/dc/COUNTRIES  \      \       \            CITIES        country
gov/dc/countries  sql       \       raw/dc/CITIES        city      string  \                 \      \       \            CITIES        city
================  ========  ======  ===================  ========  ======  ================  =====  ======  ===========  ============  =======

Kaip matome ryšys tarp lentelių buvo aptiktas automatiškai, kadangi tokia
informacija yra pateikta duomenų bazės schemoje. Tačiau gali pasitaikyti
atvejai, kad ryšiai tarp lentelių nėra aprašyti duomenų bazės schemoje, tokiais
atvejais, ryšius reikia aprašyti rankiniu būdu.

Norint nurodyti ryšį su kita lentele, reikia lauko `type` stulpelyje nurodyti
`ref`, o `ref` stulpelyje nurodyti kitos lentelės pavadinimą iš `model`
stulpelio.

Kadangi visi atvirų duomenų objektai turi privalomą `_id` lauką, kuris yra
pirminis raktas, užtenka nurodyti tik modelio pavadinimą.

Atveriant duomenis, vidinės duomenų bazės identifikatoriai nėra perkeliami.
Visi identifikatoriai generuojami naujai.

Jei šaltinio lentelės yra susietos naudojant daugiau nei vieną lauką, `column`
stulpelyje galima nurodyti kelis laukus, atskiriant juos kableliu.


Duomenų modelio normalizavimas
==============================

Dažnai pasitaiko, kad duomenų šaltiniuose pateikiam denormalizuoti duomenys.
Atvirų duomenų saugykloje rekomenduojama saugoti normalizuotus duomenis.

Tarkime, turime tokią denormalizuotą lentelę:

=======  ========  ===========  ===========
CITIES                                     
-------------------------------------------
id       code      country      city
=======  ========  ===========  ===========
1        lt        Lietuva      Vilnius
2        lv        Latvija      Kaunas
3        ee        Estija       Klaipėda
=======  ========  ===========  ===========

Gauname tokią inventorizacijos lentelę:

================  ========  ======  ===================  ========  ======  ================  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref               const  title   description  table         column
================  ========  ======  ===================  ========  ======  ================  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/CITIES        _id       pk      \                 \      \       \            CITIES        id
gov/dc/countries  sql       \       raw/dc/CITIES        code      string  \                 \      \       \            CITIES        code
gov/dc/countries  sql       \       raw/dc/CITIES        country   string  \                 \      \       \            CITIES        country
gov/dc/countries  sql       \       raw/dc/CITIES        city      string  \                 \      \       \            CITIES        city
================  ========  ======  ===================  ========  ======  ================  =====  ======  ===========  ============  =======

`CITIES` lentelėje yra pateikti du objektai, šalis ir miestas. Todėl
pirmiausiai mums reikia atskirti kur yra šalis, kur mietas, pakeičiant šalies
laukų `model` reikšmes iš `raw/dc/CITIES` į `raw/dc/COUNTRIES`.

Sekantis žingsnis, unikalus šalies identifikatorius. Miesto identifikatorių jau
turime. Šalies objektams, kaip identifikatorių panaudojam `code` lauką. Po
pertvarkymų, normalizuota inventorizacijos lentelė turėtų atrodyti taip:

Paskutinis žingsnis, šalies ir miesto objektų susiejimas pridedant `ref` tipo
lauką, panaudojant tą patį `code` stulpelį, kurį naudojome šalies pirminiam
raktui.

================  ========  ======  ===================  ========  ======  ================  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref               const  title   description  table         column
================  ========  ======  ===================  ========  ======  ================  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     _id       pk      \                 \      \       \            CITIES        code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \                 \      \       \            CITIES        code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     country   string  \                 \      \       \            CITIES        country
gov/dc/countries  sql       \       raw/dc/CITIES        _id       pk      \                 \      \       \            CITIES        id
gov/dc/countries  sql       \       raw/dc/CITIES        country   ref     raw/dc/COUNTRIES  \      \       \            CITIES        code
gov/dc/countries  sql       \       raw/dc/CITIES        city      string  \                 \      \       \            CITIES        city
================  ========  ======  ===================  ========  ======  ================  =====  ======  ===========  ============  =======

Po tokio pertvarkymo, vykdant duomenų importavimą į saugyklą, duomenys bus
automatiškai normalizuoti ir vietoje dviejų modelių vienoje lentelėje, turėsime
du atskirus modelius atskirose lentelėse. O svarbiausia, nebus prarasta ryšio
tarp modelių informacija.

Tai yra svarbu siekiant duomenų dubliavimo. Rekomenduojame atvirų duomenų
saugykloje laikyti normalizuotus duomenis. Normalizacijos dėka, atsiranda
galimybė nesudėtingai gauti bet kokio pavidalo denormalizuotas lenteles
analitiniams tikslams. Tačiau iš denormalizuotų duomenų padaryti normalizuotus
nėra taip paprastai, kai kuriais atvejai iš vis neįmanoma.


Lentelių apjungimas
===================

Kartais yra poreikis, skirtingas šaltinio lenteles apjungti į vieną.
Pavyzdžiui:


=======  ===========
APSKRITYS
--------------------
id       pavadinimas
=======  ===========
1        Vilniaus
2        Kauno
3        Klaipėdos
=======  ===========


=======  =========  ===============
SAVIVALDYBES
-----------------------------------
id       apskritis  pavadinimas
=======  =========  ===============
1        1          Vilniaus miesto
2        1          Vilniaus rajono
3        1          Trakų rajono
=======  =========  ===============


Kadangi skirtingos šalis naudoja skirtingus administracinius suskirstymus, tai
mes norime normalizuoti šias lenteles, ir padaryti iš jų vieną administracijų
lentelė.

Tarkime, apskrities administracinis vienetas bus žymimas skaičiumi `1`, o
savivaldybės skaičiumi `2`. Turime dvi konstantas administraciniam vienetui.

Mūsų pradinė inventorizacijos lentelė atrodys taip:

======================  ========  ======  ===================  ===========  ======  ================  =====  ======  ===========  ============  ===========
dataset                 resource  origin  model                property     type    ref               const  title   description  table         column
======================  ========  ======  ===================  ===========  ======  ================  =====  ======  ===========  ============  ===========
gov/dc/administracijos  sql       \       raw/dc/APSKRITYS     _id          pk      \                 \      \       \            APSKRITYS     id
gov/dc/administracijos  sql       \       raw/dc/APSKRITYS     pavadinimas  string  \                 \      \       \            APSKRITYS     pavadinimas
gov/dc/administracijos  sql       \       raw/dc/SAVIVALDYBES  _id          pk      \                 \      \       \            SAVIVALDYBES  id
gov/dc/administracijos  sql       \       raw/dc/SAVIVALDYBES  apskritis    ref     raw/dc/APSKRITYS  \      \       \            SAVIVALDYBES  apskritis
gov/dc/administracijos  sql       \       raw/dc/SAVIVALDYBES  pavadinimas  string  \                 \      \       \            SAVIVALDYBES  pavadinimas
======================  ========  ======  ===================  ===========  ======  ================  =====  ======  ===========  ============  ===========

Mums reikia pertvarkyti inventorizacijos lentelę taip, kad gautume tokį duomenų
pavidalą:

=======  =========  =========  ===============
ADMINISTRACIJOS           
----------------------------------------------
id       priklauso  lygis      pavadinimas
=======  =========  =========  ===============
1        NULL       1          Vilniaus
2        NULL       1          Kauno
3        NULL       1          Klaipėdos
4        1          2          Vilniaus miesto
5        1          2          Vilniaus rajono
6        1          2          Trakų rajono
=======  =========  =========  ===============

Kad tai gautume, mums reikia atlikti tokius pakeitimus:

- Visų `model` stulpelio eilučių reikšmes keičiame į `raw/dc/ADMINISTRACIJOS`,
  kadangi rezultate norime turėti vieną lentelę, vietoj dviejų.

- Pakeitus visas `model` reikšmes į `raw/dc/ADMINISTRACIJOS`, turime problemą.
  Tam pačiam modeliui, pavadinimu `raw/dc/ADMINISTRACIJOS` duomenis gauname iš
  dviejų skirtingų lentelių. Tam, kad atskirti kuriuo atveju naudoti vieną,
  kuriuo kitą šaltinį, mums reikia panaudoti `origin` stulpelį ir ten įrašyti
  `APSKRITYS` ir `SAVIVALDYBES`. Kad būtų lengviau suprasti šią gan painią
  vietą, reikėtų žiūrėti, kaip atrodys manifesto YAML failas:

  .. code-block:: yaml

      name: gov/dc/administracijos
      resources:
        sql:
          objects:
            APSKRITYS:
              raw/dc/ADMINISTRACIJOS:
                source: APSKRITYS
            SAVIVALDYBES:
              raw/dc/ADMINISTRACIJOS:
                source: SAVIVALDYBES

  `origin` stulpelis, tiesiog padeda atskirti modelius, tais pačiais
  pavadinimais, kai vienas modelis gauna duomenis iš kelių skirtingų vietų.
  Tokiu atveju, `origin` nurodo modelio duomenų kilmę.

- `SAVIVALDYBES.apskritis` laukui keičiame `ref` reikšmę į
  `raw/dc/ADMINISTRACIJOS`, kadangi tokio dalyko kaip `raw/dc/APSKRITYS`
  nebeliko.

- Keičiame lauko `SAVIVALDYBES.apskritis` `property` reikšmę į `priklauso`,
  kadangi apskrities savoka išnyksta ir apskritis tampa tiesiog vienu iš
  administracinių vienetų.

- Pridedam `priklauso` savybę apskritims, kadangi nenurodome `table` ir
  `column`, tai rezultate, `priklauso` reikšmė bus `NULL`.

- Paskutinis pakeitimas, tiek apskritims, tiek savivaldybėms pridėti `lygis`
  savybę nurodant konstantas `1` ir `2`.

Po pertvarkymų, mūsų inventorizacijos lentelė turėtų atrodyti taip:

======================  ========  ============  ======================  ===========  =======  ======================  =====  ======  ===========  ============  ===========
dataset                 resource  origin        model                   property     type     ref                     const  title   description  table         column
======================  ========  ============  ======================  ===========  =======  ======================  =====  ======  ===========  ============  ===========
gov/dc/administracijos  sql       APSKRITYS     raw/dc/ADMINISTRACIJOS  _id          pk       \                       \      \       \            APSKRITYS     id
gov/dc/administracijos  sql       APSKRITYS     raw/dc/ADMINISTRACIJOS  priklauso    ref      raw/dc/ADMINISTRACIJOS  \      \       \                                   
gov/dc/administracijos  sql       APSKRITYS     raw/dc/ADMINISTRACIJOS  lygis        integer  \                       1      \       \                                   
gov/dc/administracijos  sql       APSKRITYS     raw/dc/ADMINISTRACIJOS  pavadinimas  string   \                       \      \       \            APSKRITYS     pavadinimas
gov/dc/administracijos  sql       SAVIVALDYBES  raw/dc/ADMINISTRACIJOS  _id          pk       \                       \      \       \            SAVIVALDYBES  id
gov/dc/administracijos  sql       SAVIVALDYBES  raw/dc/ADMINISTRACIJOS  priklauso    ref      raw/dc/ADMINISTRACIJOS  \      \       \            SAVIVALDYBES  apskritis
gov/dc/administracijos  sql       SAVIVALDYBES  raw/dc/ADMINISTRACIJOS  lygis        integer  \                       2      \       \                                   
gov/dc/administracijos  sql       SAVIVALDYBES  raw/dc/ADMINISTRACIJOS  pavadinimas  string   \                       \      \       \            SAVIVALDYBES  pavadinimas
======================  ========  ============  ======================  ===========  =======  ======================  =====  ======  ===========  ============  ===========


Lentelės skaidymas
==================

Prieš tai aptarėme kaip apjungti kelias lenteles į vieną modelį. O dabar
aptarsime, kaip daryti atvirkštinį procesą, kaip skaidyti vieną lentelę į kelis
modelius.

Tarkime turime tokią lentelę:

=======  =========  =========  ===============
ADMINISTRACIJOS           
----------------------------------------------
id       priklauso  lygis      pavadinimas
=======  =========  =========  ===============
1        NULL       1          Vilniaus
2        NULL       1          Kauno
3        NULL       1          Klaipėdos
4        1          2          Vilniaus miesto
5        1          2          Vilniaus rajono
6        1          2          Trakų rajono
=======  =========  =========  ===============

Norime šią lentelę suskaidyti į dvi atskiras lenteles. Įrašai, kurių `lygis`
reikšmė yra `1` turėtų keliauti į apskričių modelį, o įrašai, kurių `lygis`
reikšmė yra `2` turėtų keliauti į savivaldybių modelį.

Pirminė inventorizacijos lentelė atrodo taip:

======================  ========  ============  ======================  ===========  =======  ======================  =====  ======  ===========  ===============  ===========
dataset                 resource  origin        model                   property     type     ref                     const  title   description  table            column
======================  ========  ============  ======================  ===========  =======  ======================  =====  ======  ===========  ===============  ===========
gov/dc/administracijos  sql       \             raw/dc/ADMINISTRACIJOS  _id          pk       \                       \      \       \            ADMINISTRACIJOS  id
gov/dc/administracijos  sql       \             raw/dc/ADMINISTRACIJOS  priklauso    ref      raw/dc/ADMINISTRACIJOS  \      \       \            ADMINISTRACIJOS  priklauso
gov/dc/administracijos  sql       \             raw/dc/ADMINISTRACIJOS  lygis        integer  \                       \      \       \            ADMINISTRACIJOS  lygis
gov/dc/administracijos  sql       \             raw/dc/ADMINISTRACIJOS  pavadinimas  string   \                       \      \       \            ADMINISTRACIJOS  pavadinimas
======================  ========  ============  ======================  ===========  =======  ======================  =====  ======  ===========  ===============  ===========

Tam, kad suskaidyti vienos lentelės duomenis į kelis skirtingus modelius, mums
reikia panaudoti filtrus lentelės lygmenyje. Metaduomenys lentelės lygmenyje
taikomi tada, kai `property` reikšmė yra tuščia.

Lentelės metaduomenų lygmenyje `table` stulpelyje galima nurodyti RQL užklausą
duomenims filtruoti.

Šiuo atveju, mums reikia filtruoti duomenis pagal stulpelio `lygis` reikšmes.

Galutinė inventorizacijos lentelė, po pertvarkymų atrodo taip:

======================  ========  ============  ======================  ===========  =======  ======================  =====  ======  ===========  ===============  ===========
dataset                 resource  origin        model                   property     type     ref                     const  title   description  table            column
======================  ========  ============  ======================  ===========  =======  ======================  =====  ======  ===========  ===============  ===========
gov/dc/administracijos  sql       \             raw/dc/APSKRITYS        \            \        \                       \      \       \            lygis=1          \ 
gov/dc/administracijos  sql       \             raw/dc/APSKRITYS        _id          pk       \                       \      \       \            ADMINISTRACIJOS  id
gov/dc/administracijos  sql       \             raw/dc/APSKRITYS        priklauso    ref      raw/dc/APSKRITYS        \      \       \            ADMINISTRACIJOS  priklauso
gov/dc/administracijos  sql       \             raw/dc/APSKRITYS        lygis        integer  \                       \      \       \            ADMINISTRACIJOS  lygis
gov/dc/administracijos  sql       \             raw/dc/APSKRITYS        pavadinimas  string   \                       \      \       \            ADMINISTRACIJOS  pavadinimas
gov/dc/administracijos  sql       \             raw/dc/SAVIVALDYBES     \            \        \                       \      \       \            lygis=2          \ 
gov/dc/administracijos  sql       \             raw/dc/SAVIVALDYBES     _id          pk       \                       \      \       \            ADMINISTRACIJOS  id
gov/dc/administracijos  sql       \             raw/dc/SAVIVALDYBES     priklauso    ref      raw/dc/SAVIVALDYBES     \      \       \            ADMINISTRACIJOS  priklauso
gov/dc/administracijos  sql       \             raw/dc/SAVIVALDYBES     lygis        integer  \                       \      \       \            ADMINISTRACIJOS  lygis
gov/dc/administracijos  sql       \             raw/dc/SAVIVALDYBES     pavadinimas  string   \                       \      \       \            ADMINISTRACIJOS  pavadinimas
======================  ========  ============  ======================  ===========  =======  ======================  =====  ======  ===========  ===============  ===========


Vieningo žodyno naudojimas
==========================

Tam, kad iš pirminio duomenų chaoso padaryti aukščiausio brandos lygio atvirus
duomenis, būtina išversti `model` ir `property` stulpelių pavadinimus į
pavadinimus iš vieningo žodyno.

Kaip pavyzdį galime imti tokius duomenis:

=======  ========  ===========
COUNTRIES
------------------------------
id       code      country
=======  ========  ===========
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ===========

Šiuose duomenyse yra šalių kodai ir pavadinimai. Kadangi, tai gan dažnai
naudojami duomenys, tikėtina, kad skirtinguose duomenų šaltiniuose panaši
lentelė ir jos laukai turės kitokius pavadinimus.

Tam, kad suvienodinti pavadinimus, mums reikia pasitelkti vieningą žodyną.

Žodynų sudarymas, yra gan sudėtingas darbas, todėl, jei tik yra galimybė
reikėtų remtis egzistuojančiais žodynais. Egzistuojančius žodynus galima rasti
LOV_ svetainėje, WikiData_ dažniausiai taip pat būna labai naudingas.

Tačiau nebūtina tiksliai atkartoti tai, kas pateikiama žodynuose, nes dažnai
žodynai yra labai bendro pobūdžio ir ne viską apimantys. Todėl sudarant žodynus
yra laisvė 

.. _LOV: https://lov.linkeddata.es/dataset/lov
.. _WikiData: https://www.wikidata.org/

Vieningam žodynui sudaryti naudojama kiek kitokios struktūros lentelė, kuri
atrodo taip:

=================================  ===========  =======  ===  =====================  ===================  ===========
model                              property     type     ref  uri                    title                description
=================================  ===========  =======  ===  =====================  ===================  ===========
place/country                      \            \        \    schema:Country         Šalis                \
place/country                      code         string   \    esco:isoCountryCodeA2  ISO 3166-1 A2 kodas  \
place/country                      name         string   \    og:country-name        Pavadinimas          \
=================================  ===========  =======  ===  =====================  ===================  ===========

Modelio pavadinimui galima naudoti vardų erdves, kas būtų galima suskirstyti
modelius į tamp tikras kategorijas.

`model`, `property`, `type`, `ref`, `title` ir `description` stulpelių
paskirtis yra tokia pati, kaip ir inventorizacijos lentelėje. Tačiau atsiranda
vienas papildomas laukas `uri`, kurio pagalba, galima susieti vidinį manifesto
žodyną, su pasauliniais žodynais.

Inventorizacijos lentelė, naudojant vieningą žodyną atrodytų taip:

================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref  const  title   description  table         column
================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       place/country        _id       pk      \    \      \       \            COUNTRIES     id
gov/dc/countries  sql       \       place/country        code      string  \    \      \       \            COUNTRIES     code
gov/dc/countries  sql       \       place/country        name      string  \    \      \       \            COUNTRIES     country
================  ========  ======  ===================  ========  ======  ===  =====  ======  ===========  ============  =======

Kaip matote, `raw/dc/COUNTRIES` modelio pavadinimas pasikeitė į
`place/country`. Taip pat pasikeitė ir `property` stulpelio pavadinimai. Visi
šie pavadinimai atitinka vieningą žodyną.

Iš pirmo žvilgsnio atrodytų, kad pasikeitė tik pavadinimai, tačiau iš tikrųjų
pasikeitimų yra daugiau. Visiems duomenų rinkiniams naudojantiems žodyno
pavadinimą bandoma suteikti tą patį identifikatorių. Tai reiški, kad visuose
duomenų šaltiniuose aprašyti šalie objektai naudojantys žodyno `place/country`
pavadinimą, turės tuos pačius identifikatorius.

Tai suteikia galimybę tarpusavyje jungti modelių lenteles iš skirtingų duomenų
šaltinių.


Nuasmeninimas
=============

Nuasmeninimas yra labai sudėtinga problema ir inventorizacijos metu iš esmės
sprendžiama naudojanti `person` žodyno pavadinimą tose vietose, kur duomenų
objektas yra asmuo.

Vieningo žodyno naudojimas suteikia galimybe jungti skirtingų duomenų rinkinių
lenteles tarpusavyje. Todėl identifikavus `person` modelius, šiek tiek
automatizuoti nuasmeninimo procedūrą.

Kol kas nėra sukurta jokių priemonių nuasmeninimo automatizavimui.
