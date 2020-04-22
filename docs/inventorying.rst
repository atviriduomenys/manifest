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
      --dataset=datasets/gov/dc/countries \
      --resource=sql \
      -o inventorizacija.csv

Komanda sukurs `inventorizacija.csv` failą, kuriame bus tokie duomenys:

+---+---+---+---+-----------+-----------+---------+---------+-----+-------+--------+--------+-------------+
| d | r | b | m | property  | source    | prepare | type    | ref | level | access | title  | description |
+===+===+===+===+===========+===========+=========+=========+=====+=======+========+========+=============+
| datasets/gov/dc/countries |           |         |         |     |       |        |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+--------+--------+-------------+
|   | sql                   |           |         |         |     |       |        |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+--------+--------+-------------+
|   |   |                   |           |         |         |     |       |        |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+--------+--------+-------------+
|   |   |   | countries     | COUNTRIES |         |         | id  |       |        |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+--------+--------+-------------+
|   |   |   |   | id        | id        |         | integer |     | 4     |        |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+--------+--------+-------------+
|   |   |   |   | code      | code      |         | string  |     | 2     |        |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+--------+--------+-------------+
|   |   |   |   | country   | country   |         | string  |     | 2     |        |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+--------+--------+-------------+

Inventorizacijos lentelė yra sudaryta hierarchiniu principu, kur pirmųjų
stulpelių raidės reiškia **d**: **dataset**, **r**: **resource**, **b**:
**base**, **m**: **model**.

Kol kas nesigilinsime į visų lentelės stulpelių paskirtį, kadangi tam tikrų
stulpelių panaudojimas bus aptartas atskirai. Kas šiame pavyzdyje yra aktualu:

:dataset:
  Tai yra duomenų rinkinio pavadinimas, kuris atitinka `dcat:Dataset`_.

  Duomenų rinkinio pavadinime galima naudoti vardų erdves. Pavyzdyje, duomenų
  rinkinio `datasets/gov/dc/countries` vardų erdvė yra `gov/dc`. Rekomenduojama
  valstybinėms įstaigoms naudoti `datasets/gov/` vardų erdvę, taip pat nurodant
  įstaigos trumpinį, kuris šiuo atveju yra `dc/`. Paskutinis komponentas yra
  toje įstaigoje esančio duomenų rinkinio pavadinimas. Jei įstaiga turi daug
  duomenų rinkinių, galima pasitelkti daugiau vardų erdvės dalių, pavyzdžiui
  `gov/dc/geo/countries`.

  Duomenų rinkinio pavadinimas naudojamas automatiniam duomenų rinkinių
  sinchronizavimui su atvirų duomenų vitrina `data.gov.lt`_.

.. _`dcat:Dataset`: https://www.w3.org/TR/vocab-dcat-2/#Class:Dataset
.. _data.gov.lt: https://data.gov.lt/

:resource:
  Duomenų rinkinyje esančio resurso pavadinimas, atitinka `dcat:Resource`_.

.. _`dcat:Resource`: https://www.w3.org/TR/vocab-dcat-2/#Class:Distribution

:base:
  Šis stulpelis naudojamas lentelių apjungimui. Lentelės gali būti apjungiamos
  dviem atvejais:

  - Siejant duomenų rinkinių modelius su modeliais naudojančiais žodyno
    pavadinimus.

  - Siejant kelis šaltinio modelius su vienu maziniu modeliu, tokiu būdu
    apjungiant kelis modelius į vieną.

:model:
  Duomenų modelio, pavadinimas. Modelio pavadinime galima naudoti vardų erdves.
  Galutinis modelio pavadinimas bus apjungtas su duomenų rinkinio pavadinimu.
  Pavyzdžiui jei invertorizacijos lentelėje yra nurodytas modelio pavadinimas
  `countries`, galutinios šio modelio pavadinimas bus
  `datasets/gov/dc/countries/countries`.

:property:
  Duomenų lauko pavadinimas. Kaip matote, laukas `id` buvo automatiškai
  įtrauktas į modelio `ref` stulpelį. Taip atsitiko todėl, kad įrankis
  automatiškai atpažino lentelėje esantį pirminį raktą ir įtraukį jį kaip šio
  modelio pirminį raktą.

  Visi laukų pavadinimai, kurie prasideda `_` simboliu yra rezervuoti ir turi
  tam tikrą paskirtį. Įprastiniai laukų pavadinimai negali prasidėti `_`
  simboliu.

:source:
  Priklausomai nuo hierarchijos lygio pateikiamas resurso, modelio ar savybės
  duomenų šaltinis.

:prepare:
  Atliekamas duomenų patikrinimas ir transformacija.

:type:
  Atvirų duomenų saugykla turi turtingą tipų sistemą, todėl svarbu nurodyti
  rinkamus tipus. Įrankis automatiškai bando atpažinti tipus automatiškai,
  tačiau automatinis atpažinimas ne visada suveikia. Pavyzdžiui `date` laukas
  gali būti atpažintas, kaip `string`.

  Galima naudoti šiuos tipus: `pk`, `ref`, `string`, `integer`, `number`,
  `boolean`, `binary`, `date`, `datetime`, `file`.

:ref:
  Šis stulpelis skirtas ryšiams tarp lentelių ir stulpelio prasmė priklauso nuo
  to kokioje eilutėje pateikta reikšmė. Jei `ref` nurodytas modeliui arba
  `base` eilutei, tafa `ref` yra vienas ar daugiau modelio savybių nurodytų
  `property` stulpelyje, tokiu atveju `ref` padeda susieti duomenų rinkinio
  identifikatorius su vidiniais manifesto identifikatoriais.

  Jei `ref` pateiktas `property` eilutei, tada tai yra modelio pavadinimas su
  kuriuo tam tikra savybė turi ryšį.

:level:
  Duomenų brandos lygis.

:access:
  Nurodo ar duomenys gali būti atverti ar ne. Galimos reikšmės yra:

  :private:
    Duomenų laukas yra uždaras ir negali būti atvertas ar matomas per API. Šis
    pasirinkimas turi būti naudojamas tik tokiems laukams, kurie yra tik
    vidiniam tam tikros vienos sistemos naudojimui.

  :protected:
    Duomenų laukas nėra viešas, tačiau gali būti naudojamas vidinėje
    komunikacijoje per API, turint atitinkamas teises.

  :public:
    Duomenų laukas gali būti atvertas, tačiau duomenų naudojimas yra apribotas,
    duomenų naudotojai turi susipažinti ir laikytis tam tikrų duomenų
    naudojimosi sąlygų.

  :open:
    Duomenų laukas gali būti atveras ir naudojamas be jokių apribojimų.

:title:
  Modelio ar duomenų lauko pavadinimas skirtas žmonėms. Norint nurodyti modelio
  pavadinimą, `property` stulpelis turi būti tuščias.

:description:
  Modelio ar duomenų lauko aprašymas. Norint pateikti modelio aprašymą
  `property` stulpelis turi būti tuščias. Iš šio aprašymo generuojama
  dokumentacija, todėl aprašyme reikėtų pateikti informaciją, kuri padėtų
  suprasti kaip naudoti duomenis.

Jei yra poreikis, galima pridėti daugiau stulpelių, savo nuožiūra, visi kiti
stulpeliai einantys po `description` bus ignoruojami. Stulpelių pavadinimai
turi būti tiksliai tokie, kokie pateikti pavyzdyje.

Tokia automatiškai parengta inventorizacijos lentelė gali būti naudojama
atveriant duomenis.

Inventorizacijos lentelė yra tik pagalbinė priemonė atveriamų duomenų laukų
sąrašams. Šios lentelės pagrindu yra kuriama manifesto YAML failai, tai galima
padaryti taip:

.. code-block:: sh

    scripts/csv-to-manifest inventorizacija.csv

Ši komanda sukurs `manifest/datasets/gov/dc/countries.dataset.yml` ir
`manifest/datasets/gov/dc/countries/countries.yml` failus. Šiuos YAML failus
naudoja praktiškai visos priemonės, kadangi inventorizacijos lentelėje yra
pateikiama tik pati svarbiausia metaduomenų dalis, o YAML failuose, galima
pateikti žymiai daugiau metaduomenų.

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
duomenų laukų atranką. Duomenų laukų atrankai naudojamas `access` stulpelis,
kurio reikšmės gali būti `open`, `public`, `protected` arba `private`.

`access` reikšmę galima nurodyti tiek prie vienos iš hierarchinių eilučių, tiek
prie kiekvieno lauko atskirai.

+---+---+---+---+-----------+-----------+---------+---------+-----+-------+-----------+--------+-------------+
| d | r | b | m | property  | source    | preapre | type    | ref | level | access    | title  | description |
+===+===+===+===+===========+===========+=========+=========+=====+=======+===========+========+=============+
| datasets/gov/dc/countries |           |         |         |     |       |           |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+-----------+--------+-------------+
|   | sql                   |           |         |         |     |       |           |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+-----------+--------+-------------+
|   |   |                   |           |         |         |     |       |           |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+-----------+--------+-------------+
|   |   |   | countries     | COUNTRIES |         |         | id  |       | open      |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+-----------+--------+-------------+
|   |   |   |   | id        | id        |         | pk      |     | 4     | private   |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+-----------+--------+-------------+
|   |   |   |   | code      | code      |         | string  |     | 2     |           |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+-----------+--------+-------------+
|   |   |   |   | country   | country   |         | string  |     | 2     | protected |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+-----------+--------+-------------+

Šiame pavyzdyje, visas modelis `countries` buvo pažymėtas atvėrimui, tačiau
laukas `country` nebus atvertas, nes jo `access` reikšmė yra `protected`, tai
reiškia, kad šiuos duomenis galima pasiekti tik per vidinį API.

Taip pat `id` laukui suteikta `private` reikšmė, kadangi šis laukas turi prasmę
tik konkretaus duomenų rinkinio resurso ribose.


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
  ryšiai tarp lentelių, t.y., kai yra užpildyta `ref` reikšmė `base`,
  `model` arba `ref` tipo `property` laukams.

  Visiems laukams, kurie nėra `ref` tipo, galima suteikti ketvirtą brandos
  lygį, bet tik su sąlygą, jei to modelio `ref` laukas yra užpildytas. Jei
  modelio `ref` stulpelis tuščias, tada visi kiti laukai taip pat negali turėti
  4 lygio, kadangi visas modelis, negali būti unikaliai identifikuotas.

5
  Ši vertė suteikiam tada, kai modelio ir jo laukų pavadinimai yra išversti į
  vieningą žodyną ir duomenų rinkinio modelis gali būti identifikuojamas
  globaliai.

  Modelis yra „išvertas“ tada, kai jo `base` eilutės `ref` stulpelis yra
  užpildytas.

  Net ir suteikus laukui 5 brandos lygį, galutiniame skaičiavime, laukas gaust
  4.5 brandos lygį, jei manifesto žodyno laukas nėra susietas su globaliu
  žodynu, t.y. kai žodyno modelio `uri` reikšmė yra tuščia. Taip daroma todėl,
  kad manifesto žodyno laukas, kol nėra susietas su globaliu žodynu vertinamas
  4 brandos lygiu, (5 + 4) / 2 = 4.5.

Tik pilnai sutvarkyti inventorizacijos metaduomenys, kurie leidžia automatiškai
nuskaityti duomenis, patikimai identifikuoti objektus ir visi pavadinimai
išversti į vieningą žodyną, gali būti vertinami aukščiausiu brandos lygiu.

Šio projekto priemonės saugo brandos lygio keitimosi istoriją ir suteikia
galimybę stebėti, kaip keičiasi brandos lygis laike.

Atkreipkite dėmesį į mūsų pirminę, automatiškai generuotą, inventorizacijos
lentelę:

+---+---+---+---+-----------+-----------+---------+---------+-----+-------+---------+--------+-------------+
| d | r | b | m | property  | source    | prepare | type    | ref | level | access  | title  | description |
+===+===+===+===+===========+===========+=========+=========+=====+=======+=========+========+=============+
| datasets/gov/dc/countries |           |         |         |     |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+---------+--------+-------------+
|   | sql                   |           |         |         |     |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+---------+--------+-------------+
|   |   |                   |           |         |         |     |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+---------+--------+-------------+
|   |   |   | countries     | COUNTRIES |         |         | id  |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+---------+--------+-------------+
|   |   |   |   | id        | id        |         | integer |     | 4     |         |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+---------+--------+-------------+
|   |   |   |   | code      | code      |         | string  |     | 2     |         |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+---------+--------+-------------+
|   |   |   |   | country   | country   |         | string  |     | 2     |         |        |             |
+---+---+---+---+-----------+-----------+---------+---------+-----+-------+---------+--------+-------------+

Šiai lentelei `id` laukui buvo suteiktas 4 brandos lygis, kadangi duomenų bazės
lentelė turi pirminį raktą, kuris leidžia unikaliai identifikuoti objektą.

Tačiau visi kiti laukai turi 2 brandos lygį, taip yra todėl, kad naudojama
priemonė yra konservatyvi ir pasirenka žemesnį brandos lygį. Kadangi visi kiti
laukai yra `string` tipo, tai nėra iki galo aišku ar tipas yra teisingas, gal
būt laukas yra datos tipo, arba tame lauke yra užkoduoti keli duomenų laukai.
Kad tiksliai nustatyti brandos lygį reikalingas žmogaus įsikišimas.

Brandos lygis nurodomas tik prie duomenų laukų. Modelio, resurso ir viso
duomenų rinkionio brandos lygis yra paskaičiuojamas automatiškai imant visų
duomenų laukų vidurkį, kuris šiuo atveju yra 2.7.


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

+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
| d | r | b | m | property   | source | prepare | type   | ref   | level | access  | title  | description |
+===+===+===+===+============+========+=========+========+=======+=======+=========+========+=============+
| datasets/gov/rkb/metrikai  |        |         |        |       |       |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   | epaveldas              |        |         |        |       |       |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |                    |        |         |        |       |       |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |   | lapas          |        |         |        |       |       |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |   |   | paveikslas |        |         | image  |       | 1     |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |                    |        |         |        |       |       |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |   | asmuo          |        |         |        |       |       |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |   |   | vardas     |        |         | string |       | 1     |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |   |   | pavarde    |        |         | string |       | 1     |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |                    |        |         |        |       |       |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |   | ivykis         |        |         |        |       |       |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |   |   | tipas      |        |         | string |       | 1     |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |   |   | asmuo      |        |         | ref    | asmuo | 1     |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |   |   | data       |        |         | date   |       | 1     |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+
|   |   |   |   | lapas      |        |         | ref    | lapas | 1     |         |        |             |
+---+---+---+---+------------+--------+---------+--------+-------+-------+---------+--------+-------------+

Turint tokius metaduomenis, galim organizuoti duomenų perrašymą talkos_
principu arba bandyti ištraukti duomenis kokiais nors automatizuotais būdais.

.. _talkos: https://en.wikipedia.org/wiki/Crowdsourcing

Taip pat, paruošus, kad ir labai primityvų inventorizacijos lentelės variantą,
galima toliau su ja dirbti, sieti su manifesto žodynu, tobulinti duomenų
modelį, dokumentuoti duomenų laukus.

Tai, kad tokie duomenys dalyvauja bendroje apskaitoje, reiškia, kad galima
matyti, kiek potencialių projektų galėtų įdarbinti šiuos duomenis ir kokią
naudą tai galėtų atnešti.


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

+---+---+---+---+-----------+-----------+---------+--------+-----+-------+---------+--------+-------------+
| d | r | b | m | property  | source    | perpare | type   | ref | level | access  | title  | description |
+===+===+===+===+===========+===========+=========+========+=====+=======+=========+========+=============+
| datasets/gov/dc/countries |           |         |        |     |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+-----+-------+---------+--------+-------------+
|   | sql                   |           |         |        |     |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+-----+-------+---------+--------+-------------+
|   |   |                   |           |         |        |     |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+-----+-------+---------+--------+-------------+
|   |   |   | countries     | COUNTRIES |         |        |     |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+-----+-------+---------+--------+-------------+
|   |   |   |   | code      | code      |         | string |     | 2     |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+-----+-------+---------+--------+-------------+
|   |   |   |   | country   | country   |         | string |     | 2     |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+-----+-------+---------+--------+-------------+

Tam, kad lentelę būtų galima sieti su kitomis lentelėmis reikia turėti patikimą
identifikatorių. Šiuo atveju, galima daryti prielaidą, kad laukas `code`
unikaliai identifikuoja `countries` modelio įrašus, todėl `model` ielutės `ref`
stulpeliui galima priskirti `code` reikšmę taip pakeliand modelio brandos lygį
iki 4.

+---+---+---+---+-----------+-----------+---------+--------+------+-------+---------+--------+-------------+
| d | r | b | m | property  | source    | prepare | type   | ref  | level | access  | title  | description |
+===+===+===+===+===========+===========+=========+========+======+=======+=========+========+=============+
| datasets/gov/dc/countries |           |         |        |      |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+------+-------+---------+--------+-------------+
|   | sql                   |           |         |        |      |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+------+-------+---------+--------+-------------+
|   |   |                   |           |         |        |      |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+------+-------+---------+--------+-------------+
|   |   |   | countries     | COUNTRIES |         |        | code |       |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+------+-------+---------+--------+-------------+
|   |   |   |   | code      | code      |         | string |      | 4     |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+------+-------+---------+--------+-------------+
|   |   |   |   | country   | country   |         | string |      | 4     |         |        |             |
+---+---+---+---+-----------+-----------+---------+--------+------+-------+---------+--------+-------------+

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

+---+---+---+---+------------+------------+---------+--------+-----+-------+---------+--------+-------------+
| d | r | b | m | property   | source     | prepare | type   | ref | level | access  | title  | description |
+===+===+===+===+============+============+=========+========+=====+=======+=========+========+=============+
| datasets/gov/dc/villages   |            |         |        |     |       |         |        |             |
+---+---+---+---+------------+------------+---------+--------+-----+-------+---------+--------+-------------+
|   | sql                    |            |         |        |     |       |         |        |             |
+---+---+---+---+------------+------------+---------+--------+-----+-------+---------+--------+-------------+
|   |   |                    |            |         |        |     |       |         |        |             |
+---+---+---+---+------------+------------+---------+--------+-----+-------+---------+--------+-------------+
|   |   |   | villages       | VILLAGES   |         |        |     |       |         |        |             |
+---+---+---+---+------------+------------+---------+--------+-----+-------+---------+--------+-------------+
|   |   |   |   | name       | name       |         | string |     | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+--------+-----+-------+---------+--------+-------------+
|   |   |   |   | population | population |         | string |     | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+--------+-----+-------+---------+--------+-------------+


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

+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
| d | r | b | m | property   | source     | prepare | type    | ref       | level | access  | title  | description |
+===+===+===+===+============+============+=========+=========+===========+=======+=========+========+=============+
| datasets/gov/dc/countries  |            |         |         |           |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   | sql                    |            |         |         |           |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |                    |            |         |         |           |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | countries      | COUNTRIES  |         |         | id        |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | id         | id         |         | integer |           | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | code       | code       |         | string  |           | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | country    | country    |         | string  |           | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |                    |            |         |         |           |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | cities         | CITIES     |         |         | id        |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | id         | id         |         | integer |           | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | country    | country    |         | ref     | countries | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | city       | city       |         | string  |           | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+

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

+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
| d | r | b | m | property   | source     | prepare | type    | ref       | level | access  | title  | description |
+===+===+===+===+============+============+=========+=========+===========+=======+=========+========+=============+
| datasets/gov/dc/countries  |            |         |         |           |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   | sql                    |            |         |         |           |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |                    |            |         |         |           |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | countries      | CITIES     |         |         | id        |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | id         | id         |         | integer |           | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | code       | code       |         | string  |           | 2     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | country    | country    |         | string  |           | 2     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | city       | city       |         | string  |           | 2     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+

`CITIES` lentelėje yra pateikti du objektai, šalis ir miestas. Todėl
pirmiausiai mums reikia atskirti kur yra šalis, kur miestas, pakeičiant šalies
laukų `model` reikšmes iš `raw/dc/CITIES` į `raw/dc/COUNTRIES`.

Sekantis žingsnis, unikalus šalies identifikatorius. Miesto identifikatorių jau
turime. Šalies objektams, kaip identifikatorių panaudojam `code` lauką.

Paskutinis žingsnis, šalies ir miesto objektų susiejimas pridedant `ref` tipo
lauką, panaudojant tą patį `code` stulpelį, kurį naudojome šalies pirminiam
raktui.

Po pertvarkymų, normalizuota inventorizacijos lentelė turėtų atrodyti taip:

+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
| d | r | b | m | property   | source     | prepare | type    | ref       | level | access  | title  | description |
+===+===+===+===+============+============+=========+=========+===========+=======+=========+========+=============+
| datasets/gov/dc/countries  |            |         |         |           |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   | sql                    |            |         |         |           |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |                    |            |         |         |           |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | countries      | CITIES     |         |         | code      |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | code       | code       |         | string  |           | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | country    | country    |         | string  |           | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |                    |            |         |         |           |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | cities         | CITIES     |         |         | id        |       |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | id         | id         |         | integer |           | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | country    | code       |         | ref     | countries | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | city       | city       |         | string  |           | 4     |         |        |             |
+---+---+---+---+------------+------------+---------+---------+-----------+-------+---------+--------+-------------+

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

+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+
| d | r | b | m | property        | source       | prepare | type    | ref       | level | access  | title  | description |
+===+===+===+===+=================+==============+=========+=========+===========+=======+=========+========+=============+
| datasets/gov/dc/administracijos |              |         |         |           |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+
|   | sql                         |              |         |         |           |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |                         |              |         |         |           |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | apskritys           | APSKRITYS    |         |         | id        |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | id              | id           |         | integer |           | 4     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | pavadinimas     | pavadinimas  |         | string  |           | 2     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |                         |              |         |         |           |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | savivaldybes        | SAVIVALDYBES |         |         | id        |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | id              | id           |         | integer |           | 4     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | apskritis       | apskritis    |         | ref     | apskritys | 4     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | pavadinimas     | pavadinimas  |         | string  |           | 2     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------+-------+---------+--------+-------------+

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

- Primiausiai, apsirašome naują modelį `administracijos`, kadangi galutiniame
  rezultate norime turėti viską vienoje lentelėje.

- Tada nurodome, kad `apskritys` ir `savivaldybes` yra modelio
  `administracijos` dalis. Tai reiškia, kad galiausiai duomenys iš `apskritys`
  ir `savivaldybes` bus apjungti į vieną modelį `administracijos`.

- Keičiame lauko `savivaldybes.apskritis` pavadinimą į `priklauso`, kad  lauko
  pavadinimas sutaptu su `administracijos.priklauso`.

  Kai du modeliai siejamie per `base` lauką, apjungtieji modeliai tampa
  vieno modelio dalimi ir turi tokias pačias savybes, kaip ir bazinis modelis.
  Šiuo atveju bazinis modelis yra `administracijos`.

- Paskutinis pakeitimas, tiek apskritims, tiek savivaldybėms pridėti `lygis`
  savybę nurodant konstantas `1` ir `2`.

Po pertvarkymų, mūsų inventorizacijos lentelė turėtų atrodyti taip:

+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
| d | r | b | m | property        | source       | prepare | type    | ref             | level | access  | title  | description |
+===+===+===+===+=================+==============+=========+=========+=================+=======+=========+========+=============+
| datasets/gov/dc/administracijos |              |         |         |                 |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |                         |              |         |         |                 |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   | administracijos     |              |         |         |                 |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | priklauso       |              |         | ref     | administracijos |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | lygis           |              |         | integer |                 |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | pavadinimas     |              |         | string  |                 |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   | sql                         |              |         |         |                 |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   | administracijos         |              |         | proxy   |                 |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   | apskritys           | APSKRITYS    |         |         | id              |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | id              | id           |         | integer |                 | 4     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | lygis           |              | 1       | integer |                 | 4     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | pavadinimas     | pavadinimas  |         | string  |                 | 4     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   | savivaldybes        | SAVIVALDYBES |         |         | id              |       |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | id              | id           |         | integer |                 | 4     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | priklauso       | apskritis    |         | ref     | apskritys       | 4     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | lygis           |              | 2       | integer |                 | 4     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | pavadinimas     | pavadinimas  |         | string  |                 | 4     |         |        |             |
+---+---+---+---+-----------------+--------------+---------+---------+-----------------+-------+---------+--------+-------------+

`administracijos`  modelis neturi `level` reikšmių, taip yra todėl, kad
`administracijos` modelis yra išvestinis ir neturi tiesioginio šaltinio, o
duomenų brandos lygis nurodomas duomenų laukams kurie tiesiogiai gaunami iš tam
tikro duomenų šaltinio.

Kadangi `base` `administracijos` eilutėje `ref` stulpelio yra reikšmė, tai
susiejimas bus daromas pagal vidinį modelio identifikatorių. Tai reiškia, kad
modeliai `apskritys` ir `savivaldybes` nepersidengs.

`base` `administracijos` eilutėje `type` sulpelio reikšmė `proxy` reiškia,
kad modeliai `apskritys` ir `savivaldybes` jokių duomenų nesaugos, o veiks kaip
perlaidos režimu ir duomenis rašys tik į `administracijos` modelį.


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

+---+---+---+---+-----------------+-----------------+---------+---------+-----------------+-------+---------+--------+-------------+
| d | r | b | m | property        | source          | prepare | type    | ref             | level | access  | title  | description |
+===+===+===+===+=================+=================+=========+=========+=================+=======+=========+========+=============+
| datasets/gov/dc/administracijos |                 |         |         |                 |       |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   | sql                         |                 |         |         |                 |       |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |                         |                 |         |         |                 |       |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   | administracijos     | ADMINISTRACIJOS |         |         | id              |       |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | id              | id              |         | integer |                 | 4     |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | priklauso       | priklauso       |         | ref     | administracijos | 4     |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | lygis           | lygis           |         | integer |                 | 2     |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------------+-------+---------+--------+-------------+
|   |   |   |   | pavadinimas     | pavadinimas     |         | string  |                 | 2     |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------------+-------+---------+--------+-------------+

Tam, kad suskaidyti vienos lentelės duomenis į kelis skirtingus modelius, mums
reikia panaudoti filtrus lentelės lygmenyje. Metaduomenys lentelės lygmenyje
taikomi tada, kai `property` reikšmė yra tuščia.

`source` stulpelyje galima nurodyti užklausą duomenims filtruoti. Duomenų
filtras pateikiamas tarp `[]` skliaustelių.

Šiuo atveju, mums reikia filtruoti duomenis pagal stulpelio `lygis` reikšmes.

Galutinė inventorizacijos lentelė, po pertvarkymų atrodo taip:

+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
| d | r | b | m | property        | source          | prepare | type    | ref       | level | access  | title  | description |
+===+===+===+===+=================+=================+=========+=========+===========+=======+=========+========+=============+
| datasets/gov/dc/administracijos |                 |         |         |           |       |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   | sql                         |                 |         |         |           |       |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |                         |                 |         |         |           |       |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | apskritys           | ADMINISTRACIJOS | lygis=1 |         | id        |       |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | id              | id              |         | integer |           | 4     |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | pavadinimas     | pavadinimas     |         | string  |           | 4     |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | lygis           | lygis           |         | integer |           | 4     | private |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |                         |                 |         |         |           |       |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | savivaldybes        | ADMINISTRACIJOS | lygis=2 |         | id        |       |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | id              | id              |         | integer |           | 4     |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | apskritis       | priklauso       |         | ref     | apskritys | 4     |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | pavadinimas     | pavadinimas     |         | string  |           | 4     |         |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | lygis           | lygis           |         | integer |           | 4     | private |        |             |
+---+---+---+---+-----------------+-----------------+---------+---------+-----------+-------+---------+--------+-------------+

Atkreipkite dėmesį, kad `lygis=1` filtre, pavadinimas `lygis` ateina iš
`property` stulpelio, todėl visi filtre naudojami pavadinimai turi būti
aprašyti `property` stulpelyje. Kadangi `lygis` naudojamas tik filtravimui,
`access` stulpelyje pažymime, kad šis laukas yra `private`, tokiu būdu jis
nebus niekur kitur naudojamas.


Šaltinių apjungimas į vieną modelį
==================================

Dažnai pasitaiko, kad atviri duomenys pateikiame kriuose duomenų šaltiniuose,
kur duomenys yra sugrūpuoti pagal metus ar kitus kriterijus.

Tarkime jei turime miestų duomenis suskirstytus pagal šalis.

=======  ========================
https://example.com/cities/lt.csv
---------------------------------
id       city
=======  ========================
1        Vilnius
=======  ========================

=======  ========================
https://example.com/cities/lv.csv
---------------------------------
id       city
=======  ========================
2        Ryga
=======  ========================


Norint apjungti visus šiuos šaltinius į vieną modelį, reikia atskirai aprašyti
modelį, kuris lentelėje žemiau pavadintas `cities`, o tada kiekvienam resursui
nurodyti š `cities` modelį `base` stulpelyje. Taip pat `base` eilutėje, `type`
stulplyje reikia nurodyti apjungimo tipą `proxy`, tai reiškia, kad duomenys į
modelius nebus rašomi, o perleidžiami į `base` stulpelyje nurodytą modelį.

+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
| d | r | b | m | property        | source                            | prepare | type    | ref       | level | access  | title  | description |
+===+===+===+===+=================+===================================+=========+=========+===========+=======+=========+========+=============+
| datasets/gov/dc/cities          |                                   |         |         |           |       |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | cities              |                                   |         |         | id        |       |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | id              | id                                |         | integer |           | 4     |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | city            | city                              |         | string  |           | 4     |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
|   | lt                          | https://example.com/cities/lt.csv |         | csv     |           |       |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   | cities                  |                                   |         | proxy   |           |       |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | cities/lt           |                                   |         |         |           |       |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | country         |                                   | 'lt'    | string  |           | 4     |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
|   | lv                          | https://example.com/cities/lv.csv |         | csv     |           |       |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   | cities                  |                                   |         | proxy   |           |       |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | cities/lv           |                                   |         |         |           |       |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | country         |                                   | 'lv'    | string  |           | 4     |         |        |             |
+---+---+---+---+-----------------+-----------------------------------+---------+---------+-----------+-------+---------+--------+-------------+


API duomenų inventorizavimas
============================

Dažnai duomenys teikiame per tamk tikrą API. Dažniausiai API neleidžia
parsisiųsti visų duomenų vienu kartu, reikia susirinkti duomenis nedideliais
gabaliukais.

Pavyzdžiui API gali leisti atsisiųsti miestų identifikatorių sąrašą, tačiau
norint gauti informaciją apie kiekvieną miestą reikėtų daryti po užklausą
kiekvienam miestui atskirai.


=======  ========================
https://example.com/cities/
---------------------------------
id       name
=======  ========================
1        Vilnius
2        Kaunas
3        Klaipėda
=======  ========================

=======  ======  ================
https://example.com/cities/1/
---------------------------------
id       name      population
=======  ========  ==============
1        Vilnius   536692 
=======  ========  ==============


+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
| d | r | b | m | property        | source                                 | prepare     | type    | ref       | level | access  | title  | description |
+===+===+===+===+=================+========================================+=============+=========+===========+=======+=========+========+=============+
| datasets/gov/dc/cities          |                                        |             |         |           |       |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   | cities                      | https://example.com/cities/            |             | json    |           |       |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   |   |                         |                                        |             |         |           |       |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | cities              |                                        |             |         | id        |       |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | id              |                                        |             | integer |           | 4     |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | name            |                                        |             | string  |           | 4     |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | population      |                                        |             | integer |           |       |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   | city                        | https://example.com/cities/{city._id}  |             | csv     |           |       |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   |   | cities                  |                                        |             | proxy   |           |       |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   |   |   | cities/details      |                                        |             |         | id        |       |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | $city           | cities                                 | select(_id) |         |           |       |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | id              |                                        |             | integer |           | 4     |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | name            |                                        |             | string  |           | 4     |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+
|   |   |   |   | population      |                                        |             | integer |           | 4     |         |        |             |
+---+---+---+---+-----------------+----------------------------------------+-------------+---------+-----------+-------+---------+--------+-------------+

Šiame pavyzdyje matome, kad buvo panaudotas `$city` kintamasis, kurio pagalba
formuojamas API užklausos adresas. `$city` kintamasis ima duomenis iš `cities`
modelio, kuriame jau yra sąrašas visų miestų `id`, kurio reikia API adresui
formuoti.


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

+---+-----------------+--------+-----+-----------------------+---------------------+-------------+
| m | property        | type   | ref | uri                   | title               | description |
+===+=================+========+=====+=======================+=====================+=============+
| place/country       |        |     | schema:Country        | Šalis               |             |
+---+-----------------+--------+-----+-----------------------+---------------------+-------------+
|   | code            | string |     | esco:isoCountryCodeA2 | ISO 3166-1 A2 kodas |             |
+---+-----------------+--------+-----+-----------------------+---------------------+-------------+
|   | name            | string |     | og:country-name       | Pavadinimas         |             |
+---+-----------------+--------+-----+-----------------------+---------------------+-------------+

Modelio pavadinimui galima naudoti vardų erdves, kas būtų galima suskirstyti
modelius į tamp tikras kategorijas.

`model`, `property`, `type`, `ref`, `title` ir `description` stulpelių
paskirtis yra tokia pati, kaip ir inventorizacijos lentelėje. Tačiau atsiranda
vienas papildomas laukas `uri`, kurio pagalba, galima susieti vidinį manifesto
žodyną, su pasauliniais žodynais.

Inventorizacijos lentelė, naudojant vieningą žodyną atrodytų taip:

+---+---+---+---+-----------------+-----------+---------+---------+------+-------+---------+--------+-------------+
| d | r | b | m | property        | source    | prepare | type    | ref  | level | access  | title  | description |
+===+===+===+===+=================+===========+=========+=========+======+=======+=========+========+=============+
| datasets/gov/dc/countries       |           |         |         |      |       |         |        |             |
+---+---+---+---+-----------------+-----------+---------+---------+------+-------+---------+--------+-------------+
|   | sql                         |           |         |         |      |       |         |        |             |
+---+---+---+---+-----------------+-----------+---------+---------+------+-------+---------+--------+-------------+
|   |   | /place/country          |           |         |         | code |       |         |        |             |
+---+---+---+---+-----------------+-----------+---------+---------+------+-------+---------+--------+-------------+
|   |   |   | countries           | COUNTRIES |         |         | id   |       |         |        |             |
+---+---+---+---+-----------------+-----------+---------+---------+------+-------+---------+--------+-------------+
|   |   |   |   | id              | id        |         | integer |      | 5     |         |        |             |
+---+---+---+---+-----------------+-----------+---------+---------+------+-------+---------+--------+-------------+
|   |   |   |   | code            | code      |         | string  |      | 5     |         |        |             |
+---+---+---+---+-----------------+-----------+---------+---------+------+-------+---------+--------+-------------+
|   |   |   |   | name            | country   |         | string  |      | 5     |         |        |             |
+---+---+---+---+-----------------+-----------+---------+---------+------+-------+---------+--------+-------------+

Duomenų rinkinių modeliai siejami su žodynu nurodant `base` reikšmę, kuri
atitinka žodyno modelį. Tada atitinkamai reikia pakeisti `property` reikšmes,
kad jos atitiktų `base` stulpelyje nurodyto modelio pavadinimus.

Dar vienas svabus momentas yra `code` reikšmė `source` stulpelyje, ties
`place/country` eilute. Ši reikšmė nurodo kaip
`datasets/gov/dc/countries/countries` modelio objektai turi būti
identifikuojami `place/country` lentelėje. Šiuo atveju nurodyta, kad objektų
siejimas turi būti daromas per `code` lauką. Toks objektų susiejimas leidžia
turėti vienodus identifikatorius visiems duomenų rinkiniams kurie yra
`place/country` modelio dalis.


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

+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
| d | r | b | m | property   | source    | prepare | type    | ref    | level | access  | title  | description |
+===+===+===+===+============+===========+=========+=========+========+=======+=========+========+=============+
| datasets/gov/dp1/countries |           |         |         |        |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   | sql                    |           |         |         |        |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   | /place/country     |           |         |         | a3code |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   |   | countries      | COUNTRIES |         |         | id     |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   |   |   | id         | id        |         | integer |        | 5     |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   |   |   | a3code     | code      |         | string  |        | 5     |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   |   |   | name.en    | country   |         | text    |        | 5     |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
| datasets/gov/dp2/countries |           |         |         |        |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   | sql                    |           |         |         |        |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   | /place/country     |           |         |         | a2code |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   |   | salys          | SALYS     |         |         | id     |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   |   |   | id         | id        |         | integer |        | 5     |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   |   |   | a2code     | kodas     |         | string  |        | 5     |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   |   |   | name.lt    | salis     |         | text    |        | 5     |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
| datasets/gov/dp3/countries |           |         |         |        |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   | sql                    |           |         |         |        |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   | /place/country     |           |         |         | a3code |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   |   | codes          | CODES     |         |         | a3code |       |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   |   |   | a2code     | A2        |         | string  |        | 5     |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+
|   |   |   |   | a3code     | A3        |         | string  |        | 5     |         |        |             |
+---+---+---+---+------------+-----------+---------+---------+--------+-------+---------+--------+-------------+


Žodyno lentelė turėtų atrodyti taip:

+---+-----------+--------+-----+-----+-------+-------------+
| m | property  | type   | ref | uri | title | description |
+===+===========+========+=====+=====+=======+=============+
| place/country |        |     |     |       |             |
+---+-----------+--------+-----+-----+-------+-------------+
|   | a2code    | string |     |     |       |             |
+---+-----------+--------+-----+-----+-------+-------------+
|   | a3code    | string |     |     |       |             |
+---+-----------+--------+-----+-----+-------+-------------+
|   | name      | text   |     |     |       |             |
+---+-----------+--------+-----+-----+-------+-------------+

Duomenų atvėrimo metu, visi inventorizuoti duomenų rinkiniai bus siejami su
žodyno modeliais pasitelkiant identifikatorių nurodytą `ref` stulpelyje ties
`base` eilute. Jei duomenų rinkinio modelis neturi tokio lauko, tada
susiejimas nebus daromas ir viso modelio brandos lygis nukris iki 4 brandos
lygio.

Duomenų atvėrimo metu atskirų duomenų rinkinių duomenys bus saugomi atskirai,
kadangi jie gali turėti laukų ne iš manifesto žodyno. Iš visų duomenų rinkinių
bus kuriami ir globalūs, nuo konkretaus duomenų rinkinio nepriklausomi žodynų
objektai.

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
