.. default-role:: literal

.. _norm:

Normalizavimas
##############

:term:`Duomenų normalizavimas <normalizavimas>` iš esmės yra duomenų
pasikartojimo mažinimas. Štai pavyzdys, kaip atrodo denormalizuoti duomenys:

===================  ===================
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


Manifestas
==========

Manifesto duomenų struktūrų aprašai turėtų būti kiek įmanoma normalizuoti. Jei
pirminis duomenų šaltinis yra denormalizuotas, duomenų aprašuose nesunkiai
galima atlikti normalizavimą, su sąlyga, jei įmanoma unikaliai identifikuoti
objektus. Kaip pavyzdį imkime tą pačią denormalizuotą miestų lentelę:

===================  ===================
šalis                miestas            
===================  ===================
Lietuva              Vilnius            
Lietuva              Kaunas             
Lietuva              Klaipėda          
===================  ===================

Tarkime ši lentelė yra pateikta CSV formatu adresu
`https://example.com/miestai.csv`.

Šiuo lentelės duomenų aprašas turėtų atrodyti taip:

.. code-block:: yaml

   name: pavyzdziai/normalizavimas
   type: dataset
   resources:
     miestai:
       type: csv
       objects:
         geografija/salis:
           source: https://example.com/miestai.csv
           properties:
             id:
               type: pk
               source: šalis
             pavadinimas:
               type: string
               source: šalis
         geografija/miestas:
           source: https://example.com/miestai.csv
           properties:
             id:
               type: pk
               source: šalis
             salis:
               type: ref
               object: geografija/salis
               source: šalis
             pavadinimas:
               type: string
               source: miestas

Iš šio pavyzdžio matome, kad miestų duomenys skaitomi du kartus ir paskirstomi
dviejose lentelėse. Pirmą kartą skaitome tik šalys, generuojant pirminį raktą
iš šalies pavadinimo, antrą kartą skaitome tik miestus ir prijungiame šalį
panaudojant šalies pirminį raktą. Galutiniame rezultate gauname tokias
lenteles:


**geografija/salis**

==========  ===========
id          pavadinimas
==========  ===========
`098b634e`  Lietuva
==========  ===========

**geografija/miestas**

==========  ==========  ===========
id          salis       pavadinimas
==========  ==========  ===========
`8e65fec0`  `098b634e`  Vilnius
`4fe80490`  `098b634e`  Kaunas
`cad19c34`  `098b634e`  Klaipėda
==========  ==========  ===========


Sinonimai
=========

Klausimas, ką daryti, jei duomenų šaltinis tą patį objektą vadina skirtingais
pavadinimais, jei ta pati šalis turi du sinonimus `Lietuva` arba `Lietuvos
respublika`?

Deja, tokiais atvejais automatinių priemonių nėra ir duomenys turi būti
tvarkomi pirminiame šaltinyje, arba transformuojant rankiniu būdu pasitelkiant
sinonimų lenteles ar kitas priemones. Duomenų normalizavimas veikia tik turint
unikaliai objektą identifikuojančias reikšmes.
