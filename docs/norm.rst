.. default-role:: literal

.. _norm:

Normalizavimas
##############

:term:`Duomenų normalizavimas <normalizavimas>` iš esmės yra duomenų
pasikartojimo mažinimas. Štai pavyzdys, kaip atrodo denormalizuoti duomenys:

===================  ===================
\https://example.com/1/miestai.csv
----------------------------------------
šalis                miestas
===================  ===================
Lietuva              Vilnius            
Lietuva              Kaunas             
Lietuva              Klaipėda          
===================  ===================

Kaip matote, stulpelyje `šalis` daug kartų pakartota reikšmė `Lietuva`. Toks
duomenų pasikartojimas kelia daug problemų, jei duomenys keičiasi arba tas pats
objektas gali būti pavadintas keliais skirtingais pavadinimais. Tarkime, turime
duomenis iš kito tiekėjo, kurie atrodo taip:

===================  ==============
\https://example.com/1/miestai.csv
-----------------------------------
šalis                miestas
===================  ==============
Lietuvos respublika  Šiauliai      
Lietuvos respublika  Panevėžys     
===================  ==============    

Matome, kad šioje vietoje ta pati šalis pavadinta skirtingai.

Tokias besikeičiančių ir pasikartojančių duomenų problemas padeda spręsti
unikalūs identifikatoriai arba pirminiai raktai.

Norint normalizuoti duomenis, mūsų lentelę reikia išskaidyti į dvi atskiras
lenteles:

**Šalys**

==  =======
id  šalis  
==  =======
1   Lietuva
==  =======

**Miestai**

==  =====  =========
id  šalis  miestas
==  =====  =========
1   1      Vilnius
2   1      Kaunas
3   1      Klaipėda
4   1      Šiauliai
5   1      Panevėžys
==  =====  =========

Turinti tokią normalizuotą duomenų bazę, galima nesunkiai keisti šalies
pavadinimą, galima į šalies lentelę įtraukti daugiau atributų ir visa tai
užtenka padaryti vienoje vietoje, kadangi šalies pirminis raktas niekada
nesikeičia.

Pirminius duomenis visada rekomenduojama saugoti normalizuotoje formoje, o
denormalizuotos duomenų bazės kuriamos normalizuotos duomenų bazės pagrindu,
jei norima atlikti duomenų analizę išvengiant skirtingų lentelių jungimo
kainos.

:term:`Duomenų struktūrų <DSA>` aprašai turėtų būti kiek įmanoma normalizuoti.
Jei pirminis duomenų šaltinis yra denormalizuotas, duomenų aprašuose nesunkiai
galima atlikti normalizavimą, su sąlyga, jei įmanoma unikaliai identifikuoti
objektus.

Mūsų aprašytą miestų pavyzdį normalizuoti galima šio duomenų struktūros
aprašo pagalba:

+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
| d | r | b | m | property | source                             | prepare                     | type   | ref       |
+===+===+===+===+==========+====================================+=============================+========+===========+
| datasets/example/norm    |                                    |                             |        |           |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   | miestai/1            | \https://example.com/1/miestai.csv |                             | csv    |           |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   | country          |                                    |                             | proxy  | name      |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   |   | country/1    |                                    |                             |        | name      |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   |   |   | name     | šalis                              |                             | string |           |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   | city             |                                    |                             | proxy  | name      |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   |   | city/1       |                                    |                             |        | name      |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   |   |   | name     | miestas                            |                             | string |           |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   |   |   | country  | šalis                              |                             | ref    | country/1 |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   | miestai/2            | \https://example.com/2/miestai.csv |                             | csv    |           |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   |   |   |          | Lietuvos respublika                | "Lietuva"                   | choice | country   |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   | country          |                                    |                             | proxy  | name      |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   |   | country/2    |                                    |                             |        | name      |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   |   |   | name     | šalis                              | choose(self, self, country) |        |           |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   | city             |                                    |                             | proxy  | name      |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   |   | city/2       |                                    |                             |        | name      |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   |   |   | name     | miestas                            |                             | string |           |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+
|   |   |   |   | country  | šalis                              | choose(self, self, country) | ref    | country/2 |
+---+---+---+---+----------+------------------------------------+-----------------------------+--------+-----------+

Iš šio pavyzdžio matome, kad miestų duomenys iš pirmojo šaltinio `miestai/1`
skaitomi du kartus ir paskirstomi dviejose lentelėse. Pirmą kartą skaitome tik
šalis, generuojant pirminį raktą iš šalies pavadinimo, antrą kartą skaitome tik
miestus ir prijungiame šalį panaudojant šalies pirminį raktą.

Antram duomenų šaltiniui darome tą patį, tik normalizuojame šalies pavadinimus
panaudodami :data:`choice` reikšmių normalizavimo sąrašą.

Abiejų duomenų šaltinių modeliai turi vieną `country` bazę ir vieną `city`
bazę. O kadangi :data:`base.type` yra `proxy`, tai duomenų saugykloje, bus
saugoma tik viena lentelė, bendra abiem šaltiniams. Šaltinių duomenys š
bazines lenteles bus apjungiami sutapatinant objektus, pagal miesto ir šalies
pavadinimus.

Galutiniame rezultate gauname tokias lenteles:

====  =======================
datasets/example/norm/country
-----------------------------
_id   pavadinimas
====  =======================
1     Lietuva
====  =======================


====  =====  =============
datasets/example/norm/city
--------------------------
_id   šalis  miestas
====  =====  =============
1     1      Vilnius
2     1      Kaunas
3     1      Klaipėda
4     1      Šiauliai
5     1      Panevėžys
====  =====  =============
