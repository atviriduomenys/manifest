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

================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref  const  level  title   description  table         column
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     _id       pk      \    \      4      \       \            COUNTRIES     id
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \    \      3      \       \            COUNTRIES     code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     country   string  \    \      3      \       \            COUNTRIES     country
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======


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

:level:
  Duomenų brandos lygis, šiuo atveju automatinis įrankis atpažino visiems
  laukams suteikė trečią brandos lygį.

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

================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref  const  level  title   description  table         column
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     _id       pk      \    \      4      \       \            COUNTRIES     id
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \    \      3      \       \            COUNTRIES     code
\                 sql       \       raw/dc/COUNTRIES     country   string  \    \      3      \       \            COUNTRIES     country
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======

Kadangi `country` duomenų lauko `dataset` reikšmė yra tuščia, šis laukas nebus
atvertas.


Brandos lygio vertinimas
========================

Brandos lygis vertinamas naudojant `5 ★  open data`_ vertinimą skalę.

.. _5 ★  open data: https://5stardata.info/

Brandos lygio vertę reikia įrašyti į `level` stulpelį.

Brandos lygis yra pakopinis, tai reiškia, kad kiekvienas brandos lygis turi
atitikti ne tik savo kriterijus, bet ir visus žemesnio lygio kriterijus.

Brandos lygio vertinimas turi atitikti duomenų situaciją einamuoju lauku. Kuo
geriau sutvarkyti metaduomenys, tuo labiau kyla duomenų brandos lygis.

Norint pasiekti trečią brandos lygį, dažnai užtenka vien tik automatinių
priemonių, tačiau kiekviena brandos lygio pakopa reikalauja vis daugiau laiko
ir pastangų.

Kiekvieną kartą tvarkant laukų aprašus būtina atnaujinti ir brandos lygio
reikšmę, kad bendroje apskaitoje, realiu laiku būtų galima matyti bendrą
duomenų brandos lygio situaciją.

Nors brandos lygio vertės atitinka 5 ★  open data vertes, tačiau vertinimo
kriterijai yra kiek kitokie, pritaikyti konkrečiai šiam duomenų manifesto
projektui, todėl atidžiai perskaitykite vertinimo kriterijus žemiau ir jais
vadovaukitės.

Kiekvienos vertės vertinimo kriterijai yra tokie:

0
  Ši vertė yra suteikiama tada, kai duomenų nėra, tačiau tokie neegzistuojantys
  duomenys patenka į įstaigos valdomų duomenų sritį.

  Vertinant duomenų brandos lygį svarbu žinoti, ne tik turimus duomenis, bet
  taip pat svarbu žinoti, kokių duomenų trūksta.

  Klausimas, kaip žinoti kokius neegzistuojančius duomenis įtraukti į
  inventorizacijos lentelę?

  Tokius neegzistuojančių duomenų laukų sąrašus turėtų formuoti duomenų
  naudotojai deklaruodami duomenų poreikį. Deklaruojant duomenų poreikį, tam
  kad projektas veiktų, gali neužtekti vien turimų duomenų, projektui gali
  reikėti ir tokių duomenų, kurių valstybė ar verslas dar nekaupia.

  Įstaigos inventorizuojančios savo duomenis, turėtų įvertinti, kurie duomenų
  naudotojams reikalingi duomenys patenka į tos įstaigos valdomų duomenų sritį.
  Ir tokius duomenis, net jei jie neegzistuoja turėtų įsitraukti į savo
  inventorizacijos lenteles.

1
  Ši vertė suteikiama tada, kai neįmanoma nuskaityti duomenų automatiniu būdu
  arba automatinės duomenų nuskaitymo priemonės negali užtikrinti nuskaitytų
  duomenų tikslumo. Šis brandos lygis turėtų būti taikomas paveiksliukams,
  teksto dokumentams ir pan.

  Jei duomenų laukui suteiktas antras brandos lygis, automatinės priemonės net
  nebandys skaityti šio lauko reikšmės.

2
  Ši vertė suteikiama tada, kai duomenis įmanomai tiksliai nuskaityti, tačiau
  turimos priemonės nepalaiko šaltinio duomenų formato arba inventorizacijos
  metaduomenų nepakanka, kad duomenys galėtų būti nuskaityti automatiškai.

  Pavyzdžiui jei pirminis duomenų šaltinis yra CSV failas, kurio stulpelių
  pavadinimai yra ne pirmoje eilutėje arba jei stulpeliai atskirti ne
  kableliais, o kokiu nors kitu simboliu, tada kad toks CSV failas būtų
  nuskaitytas neužtenka metaduomenų pateikiamų inventorizacijos lentelėse,
  reikia papildomus parametrus nurodyti YAML failuose. Kol visi reikalingi
  parametrai nėra pateikti ir kol CSV failas negali būti nuskaitytas
  automatiškai, jam turi būti suteiktas antras brandos lygis.

  Panašiai yra ir su atskirais laukais, pavyzdžiui jei turime datos lauką ir
  šaltinio duomenyse naudojamas koks nors nepalaikomas datos formatas, tada
  tokiam laukui turėtų būti suteiktas antras brandos lygis, iki tol, kol datos
  reikšmės bus sutvarkytos. Laikinai, kad automatinės priemonės nebandytų
  interpretuoti šio lauko, kaip datos, galima lauko tipą pakeisti į `string`.

3
  Ši vertė suteikiama tik tada, kai inventorizacijos metaduomenų pakanka, kad
  duomenys būtų nuskaityti automatiniu būdu.

  Jei paaiškėja, kad tam tikro lauko duomenys yra netvarkingi ir duomenų
  nuskaitymo įrankiai grąžina klaidas, tada tokiam duomenų laukui reikėtų
  suteikti antrą brandos lygį, kol šaltinio duomenys bus sutvarkyti.

4
  Ši vertė suteikiama tada, kai yra sutvarkyti objektų identifikatoriai ir
  ryšiai tarp lentelių, t.y., kai yra aprašyta modelio `_id` savybė, panaudotas
  `ref` duomenų tipas ryšiui tarp lentelių ir šaltinio duomenų užtenka, kad
  būtų galima unikaliai identifikuoti objektus.

  Visiems laukams, kurie nėra `pk` arba `ref` tipo, galima suteikti ketvirtą
  brandos lygį, bet tik su sąlygą, jei to modelio `_id` laukas turi 4 brandos
  lygį. Jei `_id` neturi ketvirto brandos lygio, tada visi kiti laukai taip pat
  negali turėti 4 lygio, kadangi visas objektas, negali būti unikaliai
  identifikuotas.

5
  Ši vertė suteikiam tada, kai modelio ir jo laukų pavadinimai yra išversti į
  vieningą žodyną ir duomenų šaltinis turi reikiamą kiekį laukų, kurie leidžia
  šaltinio objektą identifikuoti globaliai.

  Jei laukas neturi 5 brandos lygio, šio lauko nebus bandoma sieti su žodyno
  modeliu.

  Net ir suteikus laukui 5 brandos lygį, galutiniame skaičiavime, laukas gaust
  4.5 brandos lygį, jei manifesto žodyno laukas nėra susietas su globaliu
  žodyno lauku. Taip daroma todėl, kad manifesto žodyno laukas, kol nėra
  susietas su globaliu žodynu vertinamas 4 brandos lygiu, (5 + 4) / 2 = 4.5.

Tik pilnai sutvarkyti inventorizacijos metaduomenys, kurie leidžia automatiškai
nuskaityti duomenis, patikimai identifikuoti objektus ir visi pavadinimai
išversti į vieningą žodyną, gali būti vertinami aukščiausiu brandos lygiu.

Šio projekto priemonės saugo brandos lygio keitimosi istoriją ir suteikia
galimybę stebėti, kaip keičiasi brandos lygis laike.

Atkreipkite dėmesį į mūsų pirminę, automatiškai generuotą, inventorizacijos
lentelę:

================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref  const  level  title   description  table         column
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     _id       pk      \    \      4      \       \            COUNTRIES     id
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \    \      2      \       \            COUNTRIES     code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     country   string  \    \      2      \       \            COUNTRIES     country
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======

Šiai lentelei `_id` laukui buvo suteiktas 4 brandos lygis, kadangi duomenų
bazės lentelė turi pirminį raktą, kuris leidžia unikaliai identifikuoti
objektą.

Tačiau visi kiti laukai turi 2 brandos lygį, taip yra todėl, kad naudojama
priemonė yra konservatyvi ir pasirenka žemesnį brandos lygį. Kadangi visi kiti
laukai yra `string` tipo, tai nėra iki galo aišku ar tipas yra teisingas, gal
būt duomenų bazę kuriantys žmonės supainiojo tipus, gal būt laukas iš tiesų yra
datos tipo, arba tame lauke yra užkoduoti keli duomenų laukai. Kad tiksliai
nustatyti brandos lygį reikalingas žmogaus įsikišimas.


Nestruktūruoti duomenys
=======================

Dideli kiekiai duomenų slypi įvairiuose nestruktūruoto pavidalo duomenų
šaltiniuose, tokiuose kaip paveiksliukai ar teksto dokumentai.

Atliekant inventorizaciją, svarbu įtraukti ir tokius nesturktūruotus duomenų
šaltinius. Deja, kadangi duomenys nestruktūruoti, tai jokios automatinės
priemonės negali paruošti pradinės inventorizacijos lentelės, šį darbą teks
atlikti rankomis, nuo nulio.

Nestruktūruotų duomenų inventorizacija yra svarbi, kadangi tai leidžia matyti
pilnesnį viso duomenų ūkio vaizdą, leidžia užpildyti trūkstamų duomenų skyles.

Nestruktūruoti duomenys gali turėti didelį poveikio potencialą.

Inventorizuojant nestruktūruotus duomenis, pirmiausia reikia surasti tam tikrą
pasikartojančią struktūrą ir ją aprašyti.

Kaip pavyzdį galima galima imti skaitmenintus RKB metrikus.

.. image:: static/metrikai.png

Konkrečiai šiame pavyzdyje pateikti santuokos metrikų įrašai, tokių
skaitmenintų paveikslėlių yra ištisos knygos ir visose knygose pateikiami
gimimo, santuokos ir mirties įrašai, turintys labai aiškią struktūrą.

================  =========  ======  ===================  ========  ======  =============  =====  =====  ======  ===========  ============  =======
dataset           resource   origin  model                property  type    ref            const  level  title   description  table         column
================  =========  ======  ===================  ========  ======  =============  =====  =====  ======  ===========  ============  =======
gov/rkb/metrikai  epaveldas  \       raw/rkb/page         image     image   \              \      1      \       \            \             \
gov/rkb/metrikai  epaveldas  \       raw/rkb/asmuo        vardas    string  \              \      1      \       \            \             \
gov/rkb/metrikai  epaveldas  \       raw/rkb/asmuo        pavarde   string  \              \      1      \       \            \             \
gov/rkb/metrikai  epaveldas  \       raw/rkb/ivykis       tipas     string  \              \      1      \       \            \             \
gov/rkb/metrikai  epaveldas  \       raw/rkb/ivykis       asmuo     ref     raw/rkb/asmuo  \      1      \       \            \             \
gov/rkb/metrikai  epaveldas  \       raw/rkb/ivykis       data      date    \              \      1      \       \            \             \
gov/rkb/metrikai  epaveldas  \       raw/rkb/ivykis       page      ref     raw/rkb/page   \      1      \       \            \             \
================  =========  ======  ===================  ========  ======  =============  =====  =====  ======  ===========  ============  =======

Turint tokius metaduomenis, galim organizuoti duomenų perrašymą crowdsourcingo_
principu arba bandyti ištraukti duomenis kokiais nors automatizuotais būdais.

.. _crowdsourcingo: https://en.wikipedia.org/wiki/Crowdsourcing

Taip pat, paruošus, kad ir labai primityvų inventorizacijos lentelės variantą,
galima toliau su ja dirbti, sieti su manifesto žodynu, tobulinti duomenų
modelį, dokumentuoti duomenų laukus.

Tai, kad tokie duomenys dalyvauja bendroje apskaitoje, reiškia, kad galima
matyti, kiek potencialių projektų galėtų įdarbinti šiuos duomenis ir kokia
naudą tai galėtų atnešti.


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

================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref  const  level  title   description  table         column
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \    \      2      \       \            COUNTRIES     code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     country   string  \    \      2      \       \            COUNTRIES     country
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======

Tam, kad lentelę būtų galima sieti su kitomis lentelėmis reikia turėti patikimą
identifikatorių ir tai daroma `_id` lauko pagalba.

Jei lentelė neturi pirminio rakto, `_id` lauką reikia pridėti rankomis,
įterpiant naują eilutę ir nurodant vieną ar kelis šaltinio laukus, kurie
patikimai unikaliai identifikuoja objektą:

================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref  const  level  title   description  table         column
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     _id       pk      \    \      4      \       \            COUNTRIES     code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \    \      4      \       \            COUNTRIES     code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     country   string  \    \      4      \       \            COUNTRIES     country
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======

Šiuo atveju, laukas `code` yra šalies kodas, kuris unikaliai identifikuoja
objektą. Todėl galima šį lauką naudoti, kaip unikaliai identifikuojantį šalies
objektą.

Dažnai pasitaiko, kad neužtenka vieno lauko norint unikaliai identifikuoti
objektą, tokiu atveju, galima pateikti kelis laukus `column` stulpelyje,
atskiriant juos kableliu.

Po pertvarkymų taip pat reikėtų nepamiršti atnaujinti `level` stulpelio
reikšmių, nurodant pasikeitusį brandos lygį. Kadangi atsirado galimybė
identifikuoti modelio objektus, `_id` laukui suteikėme 4 brandos lygį.
Atitinkamai, pakeliam ir kitų laukų brandos lygį, kadangi įsitikinome, kad
automatiškai suteiktas `string` tipas yra teisingas, kas leidžia suteikti 3
brandos lygį, tačiau taip pat įsitikinome, kad nei vienas iš laukų nėra ryšio
su kita lentele laukas, todėl galime suteikti 4 brandos lygį.

Nei vienam iš šių laukų negalima suteikti 5 brandos lygio, kadangi `model` ir
`property` pavadinimai nėra iš žodyno.


Objektai be identifikatoriaus
=============================

Duomenų šaltinis ne visada leidžia unikaliai identifikuoti objektą. Pavyzdžiui,
jei turime tokią šaltinio lentelę:

========  =============
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

================  ========  ======  ===================  ==========  ======  ===  =====  =====  ======  ===========  ============  ==========
dataset           resource  origin  model                property    type    ref  const  level  title   description  table         column
================  ========  ======  ===================  ==========  ======  ===  =====  =====  ======  ===========  ============  ==========
gov/dc/villages   sql       \       raw/dc/VILLAGES      _id         pk      \    \      0      \       \            \             \
gov/dc/villages   sql       \       raw/dc/VILLAGES      name        string  \    \      4      \       \            VILLAGES      name
gov/dc/villages   sql       \       raw/dc/VILLAGES      population  string  \    \      4      \       \            VILLAGES      population
================  ========  ======  ===================  ==========  ======  ===  =====  =====  ======  ===========  ============  ==========

Čia papildomai buvo pridėtas `_id` laukas, šiam laukui suteiktas 0 brandos
lygis, kadangi duomenų šiam laukui originaliame šaltinyje nėra.

`name` ir `population` laukams suteikėme 4 brandos lygį, kadangi šie laukai
nėra `ref` tipo. Tačiau bendro modelio brandos lygio skaičiavime, šių laukų
brandos lygis bus nuleistas iki 3, kadangi modelis neturi identifikatoriaus,
todėl nė vienas laukas išskyrus `ref` tipo laukus, negali turėti didesnio
brandos lygio nei 4.

Inventorizacijos lentelėse, kiekvieno lauko brandos lygį galima žymėti
individualiai. Ne jei modelis neturi identifikatoriaus, tačiau tam tikras
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

================  ========  ======  ===================  ========  ======  ================  =====  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref               const  level  title   description  table         column
================  ========  ======  ===================  ========  ======  ================  =====  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     _id       pk      \                 \      4      \       \            COUNTRIES     id
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \                 \      4      \       \            COUNTRIES     code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     country   string  \                 \      4      \       \            COUNTRIES     country
gov/dc/countries  sql       \       raw/dc/CITIES        _id       pk      \                 \      4      \       \            CITIES        id
gov/dc/countries  sql       \       raw/dc/CITIES        country   ref     raw/dc/COUNTRIES  \      4      \       \            CITIES        country
gov/dc/countries  sql       \       raw/dc/CITIES        city      string  \                 \      4      \       \            CITIES        city
================  ========  ======  ===================  ========  ======  ================  =====  =====  ======  ===========  ============  =======

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
Visi identifikatoriai generuojami naujai, kad neatskleisti vidinės duomenų
bazės detalių.

Jei šaltinio lentelės yra susietos naudojant daugiau nei vieną lauką, `column`
stulpelyje galima nurodyti kelis laukus, atskiriant juos kableliu.

Visiems `_id` laukams automatiškai buvo parinktas 4 brandos lygis, tačiau 4
brandos lygis taip pat automatiškai buvo suteiktas ir `CITIES.country` laukui,
kadangi šaltinio duomenų bazėje jau yra pateikti tokie metaduomenys.


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

================  ========  ======  ===================  ========  ======  ================  =====  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref               const  level  title   description  table         column
================  ========  ======  ===================  ========  ======  ================  =====  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/CITIES        _id       pk      \                 \      4      \       \            CITIES        id
gov/dc/countries  sql       \       raw/dc/CITIES        code      string  \                 \      2      \       \            CITIES        code
gov/dc/countries  sql       \       raw/dc/CITIES        country   string  \                 \      2      \       \            CITIES        country
gov/dc/countries  sql       \       raw/dc/CITIES        city      string  \                 \      2      \       \            CITIES        city
================  ========  ======  ===================  ========  ======  ================  =====  =====  ======  ===========  ============  =======

`CITIES` lentelėje yra pateikti du objektai, šalis ir miestas. Todėl
pirmiausiai mums reikia atskirti kur yra šalis, kur miestas, pakeičiant šalies
laukų `model` reikšmes iš `raw/dc/CITIES` į `raw/dc/COUNTRIES`.

Sekantis žingsnis, unikalus šalies identifikatorius. Miesto identifikatorių jau
turime. Šalies objektams, kaip identifikatorių panaudojam `code` lauką.

Paskutinis žingsnis, šalies ir miesto objektų susiejimas pridedant `ref` tipo
lauką, panaudojant tą patį `code` stulpelį, kurį naudojome šalies pirminiam
raktui.

Po pertvarkymų, normalizuota inventorizacijos lentelė turėtų atrodyti taip:

================  ========  ======  ===================  ========  ======  ================  =====  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref               const  level  title   description  table         column
================  ========  ======  ===================  ========  ======  ================  =====  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       raw/dc/COUNTRIES     _id       pk      \                 \      4      \       \            CITIES        code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     code      string  \                 \      4      \       \            CITIES        code
gov/dc/countries  sql       \       raw/dc/COUNTRIES     country   string  \                 \      4      \       \            CITIES        country
gov/dc/countries  sql       \       raw/dc/CITIES        _id       pk      \                 \      4      \       \            CITIES        id
gov/dc/countries  sql       \       raw/dc/CITIES        country   ref     raw/dc/COUNTRIES  \      4      \       \            CITIES        code
gov/dc/countries  sql       \       raw/dc/CITIES        city      string  \                 \      4      \       \            CITIES        city
================  ========  ======  ===================  ========  ======  ================  =====  =====  ======  ===========  ============  =======

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

======================  ========  ======  ===================  ===========  ======  ================  =====  =====  ======  ===========  ============  ===========
dataset                 resource  origin  model                property     type    ref               const  level  title   description  table         column
======================  ========  ======  ===================  ===========  ======  ================  =====  =====  ======  ===========  ============  ===========
gov/dc/administracijos  sql       \       raw/dc/APSKRITYS     _id          pk      \                 \      4      \       \            APSKRITYS     id
gov/dc/administracijos  sql       \       raw/dc/APSKRITYS     pavadinimas  string  \                 \      2      \       \            APSKRITYS     pavadinimas
gov/dc/administracijos  sql       \       raw/dc/SAVIVALDYBES  _id          pk      \                 \      4      \       \            SAVIVALDYBES  id
gov/dc/administracijos  sql       \       raw/dc/SAVIVALDYBES  apskritis    ref     raw/dc/APSKRITYS  \      4      \       \            SAVIVALDYBES  apskritis
gov/dc/administracijos  sql       \       raw/dc/SAVIVALDYBES  pavadinimas  string  \                 \      2      \       \            SAVIVALDYBES  pavadinimas
======================  ========  ======  ===================  ===========  ======  ================  =====  =====  ======  ===========  ============  ===========

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

======================  ========  ============  ======================  ===========  =======  ======================  =====  =====  ======  ===========  ============  ===========
dataset                 resource  origin        model                   property     type     ref                     const  level  title   description  table         column
======================  ========  ============  ======================  ===========  =======  ======================  =====  =====  ======  ===========  ============  ===========
gov/dc/administracijos  sql       APSKRITYS     raw/dc/ADMINISTRACIJOS  _id          pk       \                       \      4      \       \            APSKRITYS     id
gov/dc/administracijos  sql       APSKRITYS     raw/dc/ADMINISTRACIJOS  priklauso    ref      raw/dc/ADMINISTRACIJOS  \      4      \       \                                   
gov/dc/administracijos  sql       APSKRITYS     raw/dc/ADMINISTRACIJOS  lygis        integer  \                       1      4      \       \                                   
gov/dc/administracijos  sql       APSKRITYS     raw/dc/ADMINISTRACIJOS  pavadinimas  string   \                       \      4      \       \            APSKRITYS     pavadinimas
gov/dc/administracijos  sql       SAVIVALDYBES  raw/dc/ADMINISTRACIJOS  _id          pk       \                       \      4      \       \            SAVIVALDYBES  id
gov/dc/administracijos  sql       SAVIVALDYBES  raw/dc/ADMINISTRACIJOS  priklauso    ref      raw/dc/ADMINISTRACIJOS  \      4      \       \            SAVIVALDYBES  apskritis
gov/dc/administracijos  sql       SAVIVALDYBES  raw/dc/ADMINISTRACIJOS  lygis        integer  \                       2      4      \       \                                   
gov/dc/administracijos  sql       SAVIVALDYBES  raw/dc/ADMINISTRACIJOS  pavadinimas  string   \                       \      4      \       \            SAVIVALDYBES  pavadinimas
======================  ========  ============  ======================  ===========  =======  ======================  =====  =====  ======  ===========  ============  ===========


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

======================  ========  ============  ======================  ===========  =======  ======================  =====  =====  ======  ===========  ===============  ===========
dataset                 resource  origin        model                   property     type     ref                     const  level  title   description  table            column
======================  ========  ============  ======================  ===========  =======  ======================  =====  =====  ======  ===========  ===============  ===========
gov/dc/administracijos  sql       \             raw/dc/ADMINISTRACIJOS  _id          pk       \                       \      4      \       \            ADMINISTRACIJOS  id
gov/dc/administracijos  sql       \             raw/dc/ADMINISTRACIJOS  priklauso    ref      raw/dc/ADMINISTRACIJOS  \      4      \       \            ADMINISTRACIJOS  priklauso
gov/dc/administracijos  sql       \             raw/dc/ADMINISTRACIJOS  lygis        integer  \                       \      2      \       \            ADMINISTRACIJOS  lygis
gov/dc/administracijos  sql       \             raw/dc/ADMINISTRACIJOS  pavadinimas  string   \                       \      2      \       \            ADMINISTRACIJOS  pavadinimas
======================  ========  ============  ======================  ===========  =======  ======================  =====  =====  ======  ===========  ===============  ===========

Tam, kad suskaidyti vienos lentelės duomenis į kelis skirtingus modelius, mums
reikia panaudoti filtrus lentelės lygmenyje. Metaduomenys lentelės lygmenyje
taikomi tada, kai `property` reikšmė yra tuščia.

Lentelės metaduomenų lygmenyje `table` stulpelyje galima nurodyti RQL užklausą
duomenims filtruoti.

Šiuo atveju, mums reikia filtruoti duomenis pagal stulpelio `lygis` reikšmes.

Galutinė inventorizacijos lentelė, po pertvarkymų atrodo taip:

======================  ========  ============  ======================  ===========  =======  ======================  =====  =====  ======  ===========  ===============  ===========
dataset                 resource  origin        model                   property     type     ref                     const  level  title   description  table            column
======================  ========  ============  ======================  ===========  =======  ======================  =====  =====  ======  ===========  ===============  ===========
gov/dc/administracijos  sql       \             raw/dc/APSKRITYS        \            \        \                       \      \      \       \            lygis=1          \ 
gov/dc/administracijos  sql       \             raw/dc/APSKRITYS        _id          pk       \                       \      4      \       \            ADMINISTRACIJOS  id
gov/dc/administracijos  sql       \             raw/dc/APSKRITYS        priklauso    ref      raw/dc/APSKRITYS        \      4      \       \            ADMINISTRACIJOS  priklauso
gov/dc/administracijos  sql       \             raw/dc/APSKRITYS        lygis        integer  \                       \      4      \       \            ADMINISTRACIJOS  lygis
gov/dc/administracijos  sql       \             raw/dc/APSKRITYS        pavadinimas  string   \                       \      4      \       \            ADMINISTRACIJOS  pavadinimas
gov/dc/administracijos  sql       \             raw/dc/SAVIVALDYBES     \            \        \                       \      \      \       \            lygis=2          \ 
gov/dc/administracijos  sql       \             raw/dc/SAVIVALDYBES     _id          pk       \                       \      4      \       \            ADMINISTRACIJOS  id
gov/dc/administracijos  sql       \             raw/dc/SAVIVALDYBES     priklauso    ref      raw/dc/SAVIVALDYBES     \      4      \       \            ADMINISTRACIJOS  priklauso
gov/dc/administracijos  sql       \             raw/dc/SAVIVALDYBES     lygis        integer  \                       \      4      \       \            ADMINISTRACIJOS  lygis
gov/dc/administracijos  sql       \             raw/dc/SAVIVALDYBES     pavadinimas  string   \                       \      4      \       \            ADMINISTRACIJOS  pavadinimas
======================  ========  ============  ======================  ===========  =======  ======================  =====  =====  ======  ===========  ===============  ===========


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

=================================  ===========  =======  ====  =====================  ===================  ===========
model                              property     type     ref   uri                    title                description
=================================  ===========  =======  ====  =====================  ===================  ===========
place/country                      \            \        \     schema:Country         Šalis                \
place/country                      _id          pk       code  \                      \                    \
place/country                      code         string   \     esco:isoCountryCodeA2  ISO 3166-1 A2 kodas  \
place/country                      name         string   \     og:country-name        Pavadinimas          \
=================================  ===========  =======  ====  =====================  ===================  ===========

Modelio pavadinimui galima naudoti vardų erdves, kas būtų galima suskirstyti
modelius į tamp tikras kategorijas.

`model`, `property`, `type`, `ref`, `title` ir `description` stulpelių
paskirtis yra tokia pati, kaip ir inventorizacijos lentelėje. Tačiau atsiranda
vienas papildomas laukas `uri`, kurio pagalba, galima susieti vidinį manifesto
žodyną, su pasauliniais žodynais.

Inventorizacijos lentelė, naudojant vieningą žodyną atrodytų taip:

================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
dataset           resource  origin  model                property  type    ref  const  level  title   description  table         column
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
gov/dc/countries  sql       \       place/country        _id       pk      \    \      5      \       \            COUNTRIES     id
gov/dc/countries  sql       \       place/country        code      string  \    \      5      \       \            COUNTRIES     code
gov/dc/countries  sql       \       place/country        name      string  \    \      5      \       \            COUNTRIES     country
================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======

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


Globalūs identifikatoriai
=========================

Dažniausiai nėra didelių problemų su lokaliais, vieno duomenų rinkinio ribose
naudojamai identifikatoriais. Objektus galima jungti tarpusavyje, tačiau tik
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

=================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
dataset            resource  origin  model                property  type    ref  const  level  title   description  table         column
=================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======
gov/dp1/countries  sql       \       place/country        _id       pk      \    \      5      \       \            COUNTRIES     id
gov/dp1/countries  sql       \       place/country        a3code    string  \    \      5      \       \            COUNTRIES     code
gov/dp1/countries  sql       \       place/country        name\@en  string  \    \      5      \       \            COUNTRIES     country
gov/dp2/countries  sql       \       place/country        _id       pk      \    \      5      \       \            SALYS         id
gov/dp2/countries  sql       \       place/country        a2code    string  \    \      5      \       \            SALYS         kodas
gov/dp2/countries  sql       \       place/country        name\@lt  string  \    \      5      \       \            SALYS         salis
gov/dp3/countries  sql       \       place/country        _id       pk      \    \      5      \       \            CODES         A3
gov/dp3/countries  sql       \       place/country        a2code    string  \    \      5      \       \            CODES         A2
gov/dp3/countries  sql       \       place/country        a3code    string  \    \      5      \       \            CODES         A3
=================  ========  ======  ===================  ========  ======  ===  =====  =====  ======  ===========  ============  =======

Žodyno lentelė turėtų atrodyti taip:

=================================  ===========  =======  ======  =====================  ===================  ===========
model                              property     type     ref     uri                    title                description
=================================  ===========  =======  ======  =====================  ===================  ===========
place/country                      _id          pk       a2code  \                      \                    \
place/country                      _id          pk       a3code  \                      \                    \
place/country                      a2code       string   \       \                      \                    \
place/country                      a3code       string   \       \                      \                    \
place/country                      name         string   \       \                      \                    \
=================================  ===========  =======  ======  =====================  ===================  ===========

Svarbus momentas žodyno lentelėje yra dvi `_id` eilutės. Kiekviena eilutė
nurodo, kad `place/country` modelio objektai gali būti identifikuojami vienu iš
dviejų būdų arba `a2code` arba `a3code` laukų pagalba.

Duomenų atvėrimo metu, visi inventorizuoti duomenų rinkiniai bus siejami su
žodyno modeliais pasitelkiant vieną iš galimų identifikatorių `ref` stulpelyje,
`_id` laukams. Jei duomenų rinkinio modelis neturi tokio lauko, tada susiejimas
nebus daromas ir viso modelio brandos lygis nukris iki 4 brandos lygio. Tokie
atvejai duomenų rinkiniuose turėtų būti pažymėti kaip trūkstami laukai.

`ref` reikšmė `_id` laukams, žodyno lentelėje, gali turėti daugiau nei vieną
lauką, jei objekto neįmanoma identifikuoti tik pagal vieną lauką.

Žodynuose reikėtų surašyti visus įmanomus objekto identifikavimo variantus.

Duomenų atvėrimo metu atskirų duomenų rinkinių duomenys bus saugomos pasiekiami
atskirai, kadangi jie gali turėti laukų ne iš manifesto žodyno. Iš visų duomenų
rinkinių bus kuriami ir globalūs, nuo konkretaus duomenų rinkinio nepriklausomi
žodynų objektai.

Konkrečiai šiuo atveju `place/country` žodyno lentelė atvėrus duomenis atrodys
taip:

=======  ======  ======  ===========  ===========
place/country             
-------------------------------------------------
id       a2code  a3code  name\@en     name\@lt
=======  ======  ======  ===========  ===========
1        lt      ltu     Lithuania    Lietuva  
2        lv      lva     Latvia       Latvija
3        ee      est     Estonia      Estija 
=======  ======  ======  ===========  ===========

Kaip matote, iš pirmo žvilgsnio atrodė, kad dviejų duomenų rinkinių neįmanoma
sujungti tarpusavyje, tačiau prijungus dar daugiau duomenų rinkinių, kaip kokia
dėlionė iš mažų detalių susidėliojo pilna ir išsami modelio `place/country`
lentelė.


Nuasmeninimas
=============

Nuasmeninimas sudėtingoka problema ir inventorizacijos metu iš esmės
sprendžiama naudojanti `person` modelį iš manifesto žodyno, tose vietose, kur
duomenys yra apie asmenį.

Vieningo žodyno naudojimas suteikia galimybe jungti skirtingų duomenų rinkinių
lenteles tarpusavyje, ko pasekoje susijungia net iš pirmo žvilgsnio
nesujungiami duomenų rinkiniai. Todėl identifikavus `person` modelius galima
lengviau suprasti ką tiksliai reikia nuasmeninti.

Kol kas nėra sukurta jokių priemonių nuasmeninimo automatizavimui.
