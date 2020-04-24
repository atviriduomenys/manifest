.. default-role:: literal

.. _inventory:

Inventorizacija
###############

Duomenų šaltinio inventorizacija atliekama inventorizacijos lentelės pagalba.
Daugeliu atveju inventorizacijos lentelę nesunkiai galima generuoti
automatiškai iš duomenų šaltinio.

Pavyzdžiui jei duomenų šaltinis yra CSV failas, kuris atrodo taip:

=======  ========  ==============
https://example.com/countries.csv
---------------------------------
id       code      country
=======  ========  ==============
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ==============

Tai tokių duomenų inventorizacijos lentelė atrodys taip:

+----+---+---+---+---+----------+----------------------+---------+---------+---------+-------+--------+-----+-------+-------------+
| id | d | r | b | m | property | source               | prepare | type    | ref     | level | access | uri | title | description |
+====+===+===+===+===+==========+======================+=========+=========+=========+=======+========+=====+=======+=============+
| df | datasets/gov/example     |                      |         |         |         |       |        |     |       |             |
+----+---+---+---+---+----------+----------------------+---------+---------+---------+-------+--------+-----+-------+-------------+
|    |   | http                 | https://example.com/ |         | csv     |         |       |        |     |       |             |
+----+---+---+---+---+----------+----------------------+---------+---------+---------+-------+--------+-----+-------+-------------+
|    |   |   | /country         |                      |         |         | code    |       |        |     |       |             |
+----+---+---+---+---+----------+----------------------+---------+---------+---------+-------+--------+-----+-------+-------------+
| 3a |   |   |   | country      | countries.csv        |         |         | code    |       |        |     |       |             |
+----+---+---+---+---+----------+----------------------+---------+---------+---------+-------+--------+-----+-------+-------------+
|    |   |   |   |   | code     | code                 |         | string  |         | 3     |        |     |       |             |
+----+---+---+---+---+----------+----------------------+---------+---------+---------+-------+--------+-----+-------+-------------+
|    |   |   |   |   | name     | country              |         | string  |         | 3     |        |     |       |             |
+----+---+---+---+---+----------+----------------------+---------+---------+---------+-------+--------+-----+-------+-------------+
|    |   |   | /city            |                      |         |         | name    |       |        |     |       |             |
+----+---+---+---+---+----------+----------------------+---------+---------+---------+-------+--------+-----+-------+-------------+
| 4b |   |   |   | city         | cities.csv           |         |         | name    |       |        |     |       |             |
+----+---+---+---+---+----------+----------------------+---------+---------+---------+-------+--------+-----+-------+-------------+
|    |   |   |   |   | name     | city                 |         | string  |         | 3     |        |     |       |             |
+----+---+---+---+---+----------+----------------------+---------+---------+---------+-------+--------+-----+-------+-------------+
|    |   |   |   |   | country  | country              |         | ref     | country | 3     |        |     |       |             |
+----+---+---+---+---+----------+----------------------+---------+---------+---------+-------+--------+-----+-------+-------------+

Tokia inventorizacijos lentelė, leidžia automatizuoti didelę dalį veiklų
susijusių su duomenimis. Pavyzdžiui yra galimybė patikslinti laukų tipus,
pateikti ryšius tarp lentelių, pateikti aiškesnius laukų pavadinimus ir
aprašymus, susieti su žodynu, konvertuoti duomenis į kitus formatus ir t.t.

Inventorizacijos lentelė yra sudaryta hierarchiniu principu, 5 stulpeliai
einantys po lauko `id` nurodo hierarchijos lygį:

==  ========  ===============================================
d   dataset   Duomenų rinkinio pavadinimas
r   resource  Duomenų šaltinio arba distribucijos pavadinimas
b   base      Modelio bazės pavadinimas
m   model     Modelio arba lentelės pavadinimas
\   property  Modelio savybės pavadinimas
==  ========  ===============================================

Lentelėje šie pavadinimai yra sutrumpinti, dėl aiškumo, tačiau šie pavadinimai
inventorizacijos lentelėse turi būti pilni.

Hierarchijos principas veikia taip, kad jei yra pateikta `dataset` reikšmė, tai
visi kiti gileniame hierarchijos lygmenyje esantys įrašai, priklauso nurodytam
`dataset`.

Stulpeliai einantys por `property` gali turėti skirtingą prasmę, priklausomai
nuo hierarchijos lygmens.

Dalis laukų turi vienodą prasmę, nepriklausomai nuo hierarchijos lygio:

:id:
  Automatiškai generuotas UUID, kad užtikrinti unikalų objektų identifikavimą,
  net jei keičiasi pavadinimai.

  Šis laukas turėtų būti naudojamas tik kartu su `datast` ir `model`.

:level:
  :ref:`brandos-lygis`. Visi žmenesni hierarchijos lygiai paveldės tai, kas
  nurodyta aukštesniame lygyje, nebent žemesnis lygis turi kitą reikšmę.

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

  Šis stulpelis taip pat paveldimas žemesniuose hierarchijos lygiuose.

:uri:
  Sąsaja su išoriniu žodynu naudojant `sutartinius prefiksus`__.

  .. __: https://gitlab.com/atviriduomenys/manifest/-/blob/master/prefixes.yml

:title:
  Duomenų rinkinio, resurso, modelio ar savybės pavadinimas skirtas žmonėms.

:description:
  Duomenų rinkinio, resurso, modelio ar savybės aprašymas.


Duomenų rinkinys
================

Duomenų rinkinys atitinka `dcat:Dataset`_ prasmę.

Duomenų rinkinio pavadinime galima naudoti vardų erdves. Pavyzdyje, duomenų
rinkinio `datasets/gov/example` vardų erdvė yra `datasets/gov`. Rekomenduojama
valstybinėms įstaigoms naudoti `datasets/gov/` vardų erdvę, taip pat nurodant
įstaigos trumpinį, kuris šiuo atveju yra `example/`. Jei įstaiga turi didesnį
kiekį duomenų rinkinių, galima pasitelkti daugiau vardų erdvės dalių,
pavyzdžiui `datasets/gov/example/geo`, kad suskirstyti rinkinius į kategorijas.

Duomenų rinkinio pavadinimas naudojamas automatiniam duomenų rinkinių
sinchronizavimui su atvirų duomenų vitrina `data.gov.lt`_.

.. _`dcat:Dataset`: https://www.w3.org/TR/vocab-dcat-2/#Class:Dataset
.. _data.gov.lt: https://data.gov.lt/


:source:
  Konkretaus duomenų rinkinio URL, kur galima rasti daugiau informacijos apie
  šį duomenų rinkinį.


Resursas
========

Tiksli resurso prasmė priklauso nuo :ref:`duomenų šaltinio <sources>`. Tai gali
būti duomenų bazė, katalogas, kuriame laikomi CSV ar TSV failai, skaičiuoklės
failas, ZIP archyvas, JSON ar XML dokumentas ir pan.

Pats resurso pavadinimas gali būti duomenų bazės pavadinimas, failo
pavadinimas, katalogo pavadinimas ir pan. Vienas duomenų rinkinys gali turėti
kelis resursus, todėl pavadinimas turi unikaliai identifikuoti kiekvieną
resursą.

:source:
  Duomenų šaltinio pavadininimas, gali būti duomenų bazės prisijungimo eilutė
  arba URL iki duomenų katalogo ar konkretaus failo.

:type:
  Resurso tipas. Galimi variantai:

  :sql:
    Reliacinė duomenų bazė.

  :csv:
    CSV failas.

  :json:
    JSON dokumentas.

  :xml:
    XML dokumentas.

  :xlsx:
    XLSX dokumentas.

  Daugiau apie tai skyriuje :ref:`sources`.


Modelio bazė
============

Modelio bazė naudojama modelių apjungimui. Vienas modelis gali būti kito
bazinio modelo dalimi.

Kai modelis turi nurodyta bazinį modelį, tai tas modelis tampa bazinio modelio
dalimi, gauna tuos pačius identifikatorius, paveldi laukus su sutampančiais
pavadinimais ir pan.

:type:
  Baziniai modeliai gali būti įvairių rūšių. Jei `type` nenurodytas, tada
  bazinis modelis ir modelis saugomi atskirai, tik siejami naudojanti vienodus
  identifikatorius per :ref:.

  :proxy:
    Saugomas tik bazinis modelis, visi kiti šiam baziniam modeliui priskirti
    modeliai atskirai nesaugomi.

:ref:
  Vienas ar keli laukai atskirti kableliais iš kiekvieno modelio laukų sąrašo
  susieto su baziniu modeliu. Šie laukai naudojami, tam kad unikaliai
  identifikuoti objektą, tada visiems modeliams priskiriamas bazinio modelio
  objekto identifikatorius.

:prepare:
  Modelių apjungimui dažniausiai užtenka nurodyti tik laukų sąrašą `ref`
  stulpelyje. Tačiau yra galimybė nurodyti formulę, kurios pagalba galima
  suprogramuoti kokį nors kitą, nestandartinis modelių apjungimo būdą.

  Plačiau apie formules skaitykite skyriuje :ref:`formulas`.


Modelis
=======

Modelis yra viena duomenų lentelė.

Duomenų modelio, pavadinimas. Modelio pavadinime galima naudoti vardų erdves.
Galutinis modelio pavadinimas bus apjungtas su duomenų rinkinio pavadinimu.
Pavyzdžiui jei invertorizacijos lentelėje yra nurodytas modelio pavadinimas
`country`, galutinios šio modelio pavadinimas bus
`datasets/gov/example/country`.


:source:
  Duomenų šaltinyje esantis modelio pavadinimas.

  Daugiau apie tai skaitykite skyriuje :ref:`sources`.

:prepare:
  Jei reikia atverti ne visus, o tik dalį konkrečios lentelės duomenų, galima
  nurodyti filtrą duomenų atrankai.

  Plačiau apie formules skaitykite skyriuje :ref:`formulas`.

:ref:
  Modelio pirminis raktas.

  Pateikiamas vienas ar daugiau kableliais atskirtų laukų iš `property`
  stulpelio, kurie unikaliai identifikuoja kiekvieną modelio objektą.



Modelio savybė
==============

Modelio savybė arba duomenų laukas.

:source:
  Duomenų šaltinyje esantis duomenų lauko pavadinimas.

  Daugiau apie tai skaitykite skyriuje :ref:`sources`.

:prepare:
  Jei lauko reikšmę reikia transformuoti ar patikrinti, galima naudoti
  formules.

  Plačiau apie formules skaitykite skyriuje :ref:`formulas`.

:type:
  Duomenų lauko tipas. Galimi tokie tipai:

  =========  ========================================================
  Tipas      Aprašymas
  =========  ========================================================
  boolean    Loginė reikšmė taip/ne.
  integer    Sveikas skaičius
  number     Realus skaičius
  string     Simbolių eilutė
  text       Tam tikra kalba (Lietuvių, Anglų, ..) parašytas tekstas.
  binary     Dvejetainiai duomenys.
  date       Data.
  datetime   Data ir laikas.
  file       Failas.
  image      Paveiksliukas.
  ref        Ryšys su kitu modeliu.
  backref    Atgalinis ryšys su modeliu.
  generic    Dinaminis ryšys su modeliu.
  =========  ========================================================

:ref:
  Jei lauko tipas yra `ref`, `backref` arba `generic`, stulpelyje `ref`
  nurodomas modelis, su kuriuo siejamas konretus laukas.
