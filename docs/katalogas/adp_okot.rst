**Versija: 2021-08-04**

**Paruošė: Aleksandras Urbonas**

**MB DUOMENŲ ALCHEMIKAS**

TURINYS

`1. Įvadas 4 <#įvadas>`__

`1.1. Naudojami terminai ir sąvokos
4 <#naudojami-terminai-ir-sąvokos>`__

`2. Institucijos ir atstovaujančio koordinatoriaus registravimas
5 <#institucijos-ir-atstovaujančio-koordinatoriaus-registravimas>`__

`2.1. Registracija pasirinkus „Gyventojas“
6 <#registracija-pasirinkus-gyventojas>`__

`2.2. Registracija pasirinkus „Viešasis sektorius“
7 <#registracija-pasirinkus-viešasis-sektorius>`__

`2.3. Identifikavus tapatybę 8 <#identifikavus-tapatybę>`__

`3. Prisijungimas prie sistemos 11 <#prisijungimas-prie-sistemos>`__

`4. Pagrindinis meniu 12 <#pagrindinis-meniu>`__

`4.1. Paieška 12 <#_Toc79011215>`__

`5. Pradinis langas 13 <#pradinis-langas>`__

`6. Darbas su organizacijos AD tvarkytojais (Koordinatoriai)
14 <#darbas-su-organizacijos-ad-tvarkytojais-koordinatoriai>`__

`7. Darbas su organizacijos rekvizitais (Koordinatoriai)
16 <#darbas-su-organizacijos-rekvizitais-koordinatoriai>`__

`8. Darbas su poreikiais (Koordinatoriai)
18 <#darbas-su-poreikiais-koordinatoriai>`__

`8.1. Poreikių sąrašo peržiūra 18 <#_Toc79011220>`__

`8.2. Atvėrimo poreikio peržiūra 19 <#atvėrimo-poreikio-peržiūra>`__

`8.3. Atsakymas į pateiktą atvėrimo poreikį
24 <#atsakymas-į-pateiktą-atvėrimo-poreikį>`__

`9. Darbas su duomenų rinkiniais 25 <#darbas-su-duomenų-rinkiniais>`__

`9.1. Duomenų rinkinių sąrašo peržiūra
26 <#duomenų-rinkinių-sąrašo-peržiūra>`__

`9.2. Duomenų šablono atsisiuntimas
27 <#duomenų-šablono-atsisiuntimas>`__

`9.3. Duomenų rinkinio importavimas
27 <#duomenų-rinkinio-importavimas>`__

`9.4. Naujo duomenų rinkinio sukūrimas ir inventorinimas
28 <#naujo-duomenų-rinkinio-sukūrimas-ir-inventorinimas>`__

`1. Inventorinimo duomenys 28 <#inventorinimo-duomenys>`__

`2. Struktūra 29 <#struktūra>`__

`3. Prioritetai 30 <#prioritetai>`__

`4. Finansiniai duomenys 33 <#finansiniai-duomenys>`__

`5. Metaduomenų įvedimas 34 <#metaduomenų-įvedimas>`__

`6. Duomenų distribucijos tvarkymas
37 <#duomenų-distribucijos-tvarkymas>`__

`7. Pateikti poreikiai 40 <#pateikti-poreikiai>`__

`8. Duomenų rinkinio istorijos peržiūra
41 <#duomenų-rinkinio-istorijos-peržiūra>`__

`9. Duomenų rinkinio pastabų peržiūra
42 <#duomenų-rinkinio-pastabų-peržiūra>`__

`10. Darbas su IRS rinkiniais 43 <#darbas-su-irs-rinkiniais>`__

`10. Darbas su metiniais planais 45 <#darbas-su-metiniais-planais>`__

`10.1. Metinio plano sudarymas 46 <#metinio-plano-sudarymas>`__

`10.2. Metinio plano formavimas ir pateikimas
47 <#metinio-plano-formavimas-ir-pateikimas>`__

`10.3. Metinio plano išformavimas 49 <#metinio-plano-išformavimas>`__

`10.4. Plano patvirtinimas organizacijos vardu
50 <#plano-patvirtinimas-organizacijos-vardu>`__

`11. Ataskaitų formavimas 51 <#_Toc79011243>`__

`11.1. Ataskaitų kūrimas 51 <#ataskaitų-kūrimas>`__

`11.2. Paruoštų ataskaitų valdymas 52 <#paruoštų-ataskaitų-valdymas>`__

`11.3. Ataskaita „Atvirų duomenų rinkinių naudojimo intensyvumo detalūs
duomenys“
53 <#ataskaita-atvirų-duomenų-rinkinių-naudojimo-intensyvumo-detalūs-duomenys>`__

`11.4. Ataskaita „Atvirų duomenų rinkinių naudojimo intensyvumo detalūs
duomenys (failams)“
56 <#ataskaita-atvirų-duomenų-rinkinių-naudojimo-intensyvumo-detalūs-duomenys-failams>`__

`12. Partnerių API 58 <#partnerių-api>`__

`13. Slaptažodžio keitimas 59 <#slaptažodžio-keitimas>`__

Įvadas
======

*Organizacijos koordinatorių ir tvarkytojų aplinka yra skirta:*

-  *duomenų rinkinių įkėlimui, įvertinimui ir atvėrimui;*

-  *ataskaitų sudarymui.*

Naudojami terminai ir sąvokos
-----------------------------

=============================================
==============================================================================================================================================================================================================================================================================
Terminas, sąvoka                              Aprašymas
„Laukas“                                      Kabutėmis „  “ žymimas duomenų įvedimo laukas, kur tarp kabučių rašomas lauko pavadinimas, matomas aprašomame lange.
„Tekstinis laukas“                            Vieta, kur sistemos naudotojas gali suvesti duomenis arba duomenys yra vaizduojami.
[Mygtukas]                                    Dialogo lango arba lango mygtukai (taip pat vadinami komandiniais mygtukais) tekste yra žymimi kvadratiniais skliausteliais []. Tarp skliaustelių yra rašomas mygtuko pavadinimas. Sistemoje atvaizduoti kaip keturkampiai mygtukai ir aktyvios nuorodos (pabrauktas tekstas).
API (angl. Application Programming Interface) Programos valdymo sąsaja įgalina automatizuotai atlikti duomenų rinkinių kėlimą ir valdymą naudojant organizacijos programinę įrangą.
Lango mygtukas                                Mygtukas, kurio veiksmas įtakoja visus lango duomenis.
Įrašo mygtukas                                Mygtukas, kurio veiksmas įtakoja vieno įrašo duomenis.
IRS                                           Rinkiniai iš Informacinių Rinkinių Sistemos (IRS)
„Meniu punktas”                               Kabutėmis „  ” yra žymimas meniu punktas.
                                             
                                              Tarp kabučių rašomas meniu punkto pavadinimas.
Žymimasis langelis                            Kvadrato formos figūra, kurios dešinėje rašomas tekstas. Aprašymas atspindi galimą veiksmą. Figūra parodo, ar yra pasirinkta nurodyta reikšmė, ar ne. Naudotojas gali keisti pasirinkimo langelio reikšmę pele pažymint arba panaikinant požymį langelyje.
Pagrindinis meniu                             Pagrindiniame meniu yra pristatomos pagrindinės sistemos funkcijos. Pagrindinio meniu punktai yra pasirenkami pelės kairiojo klavišo spustelėjimu pažymint juos.
Pasirinktas meniu punktas                     Norėdamas pasirinkti meniu punktą, sistemos naudotojas turi spragtelti ant jo kairiu pelės klavišu.
Saugus slaptažodis                            Bent aštuonių simbolių ilgio; sudarytas iš raidžių, skaičių ir specialių simbolių (tokių kaip „@“, „#“ ar pan.).; skiriasi nuo ankstesnio.
VIISP                                         Valstybės Informacinių Išteklių Sąveikumo Platforma, prieiname per Elektroninius Valdžios Vartus
E-Vartai                                      Elektroninių valdžios vartų puslapis
Įstaiga                                       Organizacija / institucija, vykdanti nustatytas veiklas
|image0| Sąrašo rūšiavimas                    Sąrašą galima rikiuoti pagal bet kurį iš stulpelių: spauskite pasirinkto stulpelio pavadinimą arba [|image1|].
=============================================
==============================================================================================================================================================================================================================================================================

Institucijos ir atstovaujančio koordinatoriaus registravimas
============================================================

*Portale reikia registruoti savo instituciją ir vieną atstovaujantį
koordinatorių.*

*Koordinatorius paskiria atvirų duomenų rinkinių tvarkytojus.*

*Prieš pradedant registraciją, siūlome turėti vadovo parašu patvirtintą
koordinatoriaus skyrimo raštą.*

1. Naršyklėje atsidarykite Portalo puslapį https://data.gov.lt.

2. Pagrindiniame lange spauskite [**Užpildyti naujo duomenų teikėjo
   formą**]:

| |Graphical user interface Description automatically generated|
| 1 pav. Portalo pagrindinio lango viršutinis fragmentas

*Būsite nukreipti į E-Vartų puslapį.* *Čia pateikiami prisijungimo
būdai:*

| |image3|
| 2 pav. E-vartų prisijungimo puslapio fragmentas

Jeigu koordinatoriumi yra skiriamas:

-  Valstybės tarnautojas: Registruokitės pasirinkę „Gyventojas“ (3) arba
   „Viešasis sektorius“ (5)

-  Darbuotojas, dirbantis pagal darbo sutartį: Registruokitės pasirinkę
   „Gyventojas“ (3).

Siūlome registruotis pasirinkus „Gyventojas“ (3).

Registracija pasirinkus „Gyventojas“
------------------------------------

E-Vartų puslapyje:

1. Paspauskite „Gyventojas ar rezidentas“ (3).

| |image4|
| 3 pav. E-Vartų puslapio viršutinis fragmentas

2. Atsidariusiame lange pasirinkite registraciją „Per banką“ (6) arba
   „Su elektroninės atpažinties priemone“ (7). Siūlome rinktis variantą
   „Per banką“.

| |Graphical user interface, application Description automatically
  generated|
| 4 pav. Prisijungimo prie E-Vartų langas

3. Pasirinkite registraciją „Per banką“ (6), paspauskite savo banko
   ikoną, suvesti el. bankininkystės prisijungimo duomenis.

Registracija pasirinkus „Viešasis sektorius“
--------------------------------------------

1. Paspauskite „Viešasis sektorius“ (5).

| |image6|
| 5 pav. E-Vartų prisijungimo tapatybės nustatymo langas

2. Atsidariusiame lange paspauskite „Valstybės tarnautojo pažymėjimas ir
   skaitytuvas“ (8).

| |Graphical user interface, text, application, chat or text message
  Description automatically generated|
| 6 pav. Prisijungimo priemonės nustatymo langas

3. Suveskite reikiamus identifikavimo duomenis (9):

| |Graphical user interface, text, application, chat or text message,
  website Description automatically generated| |Graphical user
  interface, website Description automatically generated|
| 7 pav. Kairėje – identifikavimo lango pirmas fragmentas. Dešinėje –
  pasirašymo su PIN lango fragmentas.

**
**

Identifikavus tapatybę
----------------------

*Tiek registruojantis kaip „Gyventojas“, tiek kaip „Viešasis sektorius“,
po tapatybės nustatymo būsite nukreipti į puslapį „E. paslaugos“ arba į
langą „Duomenų teikimas į Atvirų duomenų portalą“.*

*Priklausomai pagal atpažinimo pobūdį, atlikite veiksmus:*

-  *Nuo žingsnio (10), jeigu buvote nukreipti į puslapį „E-paslaugos“,*

-  *Nuo žingsnio (13), jeigu buvote nukreipti „Duomenų teikimas į Atvirų
   duomenų portalą“.*

1. Jeigu buvote nukreipti į E. paslaugos puslapį, spauskite
   „Prisijungti“ (10).

   *Būsite nukreipti į E-Vartų puslapį.*

| |Graphical user interface, website Description automatically
  generated|
| 8 pav. Prisijungimo per elektroninį banką langas

Atsidarius langui (11):

| |Graphical user interface, website Description automatically
  generated|
| 9 pav. E-Vartų puslapio prisijungimo būdo pasirinkimo langas

2. Naujame naršyklės lange atsidarykite Portalo puslapį
   https://data.gov.lt.

3. Pakartotinai spauskite [**Užpildyti naujo duomenų teikėjo formą**]:

| |Graphical user interface Description automatically generated|
| 10 pav. Portalo pradinio lango fragmentas

*Atsidariusiame E-vartų lange „Duomenų teikimas į Atvirų duomenų
portalą“ (13) automatiškai surenkami ir atvaizduojami registruojamo
koordinatoriaus duomenys: vardas, pavardė, kontaktai.*

| |Graphical user interface Description automatically generated|
| 11 pav. E-vartų langas „Duomenų teikimas į Atvirų duomenų portalą“

-  **Atsisakyti patvirtini duomenis:** spauskite [**Atšaukti**].

-  **Patvirtinti informaciją:** spauskite [**Patvirtinti**] (14).

4. Atsidarys „Duomenų teikėjo registracijos“ (15) forma, kurioje
   pateikite informaciją (\* – privaloma):

| |Graphical user interface, text, application, email Description
  automatically generated|
| 12 pav. Duomenų teikėjo registracijos lango fragmentas

5. Pasirinkite organizaciją iš sąrašo \* (16).

   -  Jeigu organizacijos nėra sąraše, spauskite „Pridėti organizaciją“
      (17).

6. Nurodykite atvirų duomenų koordinatoriaus el. pašto adresą \* (18).

7. Nurodykite organizacijos atvirų duomenų koordinatoriaus telefoną \*
   (19).

8. Įkelkite institucijos vadovo (ar įgalioto darbuotojo) pasirašytą
   koordinatoriaus paskyrimo raštą \* (20).

   Rašto formatas:

-  skaitmeninė kopija (pdf)

-  el. parašu pasirašytas (.adoc)

-  e-parašu pasirašyto dokumento nuorašas (pdf).

   *Rašto pavyzdį rasite po nuoroda
   „orgKoordinatoriausPaskyrimoRastas.doc“*

9. Spauskite „Registruoti duomenų teikėją“ (21).

*Atsakymo žinutę gausite per keletą dienų nurodytu el. paštu.*

*Jei registracija – patvirtinta:*

-  *Žinutėje nurodomi koordinatorius prisijungimo duomenys – el. paštas
   ir slaptažodis*

-  *Dabar prie portalo galite prisijungti kaip koordinatorius!*

*Jei registracija – atmesta:*

-  *Žinutėje nurodoma atmetimo priežastis, pvz., „raštas nėra tinkamai
   užpildytas“ ar „trūksta parašo“.*

**
**

Prisijungimas prie sistemos
===========================

| |Graphical user interface, application Description automatically
  generated|
| 13 pav. Prisijungimo langas

1. Naršyklėje atidarykite puslapį adresu:
      https://staging.data.gov.lt/admin/login.

2. Užpildykite laukus **„El. paštas“** ir **„Slaptažodis“**.

3. Spauskite **[Prisijungti]**.

Jei naršyklėje jau esate atsidarę nuorodą, galite tikėtis tokio
pranešimo:

|Text Description automatically generated with low confidence|

Pagrindinis meniu
=================

============================================================================================
=============================================================================================
=========================================
|Graphical user interface, application Description automatically generated|                  *Pagrindinis meniu matomas prisijungus prie sistemos ir leidžia pasiekti aplinkos atributus:* |image18|
14 pav. Pagrindinis                                                                                                                                                                        15 pav. Pagrindinis meniu Koordinatoriams
meniu Tvarkytojams                                                                           -  **Pagrindinis:** pirmasis puslapis rodomas po prisijungimo;                               
                                                                                                                                                                                          
                                                                                             -  **Atvėrimo poreikiai:** atvėrimo poreikių sąrašas;                                        
                                                                                                                                                                                          
                                                                                             -  **Atvėrimo planai:** metiniai duomenų rinkinių atvėrimo planai;                           
                                                                                                                                                                                          
                                                                                             -  **Organizacijos rekvizitai:** duomenys apie pačią organizaciją;                           
                                                                                                                                                                                          
                                                                                             -  **Organizacijos tvarkytojai:** priskirtus tvarkytojų duomenys;                            
                                                                                                                                                                                          
                                                                                             -  **Duomenų rinkiniai:** duomenų rinkinių informacija [Meniu];                              
                                                                                                                                                                                          
                                                                                             -  **Ataskaitos:** ataskaitų ruošimo langas [Meniu];                                         
                                                                                                                                                                                          
                                                                                             -  Kiti skyriai, reikalingi Koordinatorių arba Tvarkytojų darbui.                            
============================================================================================
=============================================================================================
=========================================
-  **Išskleisti meniu**\ *: Pelyte užveskite ant meniu juostos, o tada*\ **[> Išskleisti].**                                                                                              
                                                                                                                                                                                          
-  **Suskleisti meniu**\ *: Spauskite*\ **[< Suskleisti]**\ *meniu apačioje.*                                                                                                             
                                                                                                                                                                                          
-  **Išskleisti meniu lauką**\ *: Spauskite*\ **[**\ |Screenshot (254)|\ **]**                                                                                                            
                                                                                                                                                                                          
-  **Suskleisti meniu lauką**\ *: Spauskite*\ **[**\ |image20|\ **]**\ *.*                                                                                                                
============================================================================================
=============================================================================================
=========================================

Paieška
-------

Kairėje ekrano pusėje, meniu viršuje – tekstinis laukas skirtas meniu
laukų paieškai.

=================================================================================
===============================================================================
|Graphical user interface, text, application Description automatically generated| 1. Į tekstinį lauką įveskite pavadinimą, pilną arba fragmentą;
16 pav. Pagrindinio meniu laukų paieškos rezultatų pavyzdys                      
                                                                                  2. Spauskite **[Enter]**.
                                                                                 
                                                                                  3. Paiešką atitinkantys variantai bus atvaizduoti meniu lauke.
                                                                                 
                                                                                  4. Vėl norėdami matyti pilną meniu, spauskite **[**\ |Screenshot (256)|\ **].**
=================================================================================
===============================================================================

Pradinis langas
===============

*Pradinis langas matomas:*

-  *prisijungus prie paskyros,*

-  *pagrindiniame meniu paspaudus punktą*\ **„Pradinis“**\ *.*

| |image23|
| 17 pav. Organizacijos koordinatoriaus aplinkos pradinio lango
  fragmentas

Lange pateikiama lentelė, kurioje pateikta informacija apie
organizacijos statistiką:

-  **Organizacijos:**– skaičius organizacijų, portale pateikusių duomenų
   rinkinius;

-  **Organizacijos duomenų rinkiniai** – skaičius rinkinių portale,
   priskirtų organizacijai;

-  **Distribucijos**: į portalą įkeltų duomenų rinkinių pateikimo
   distribucijos failų skaičius;

-  **Portalo naudotojai:** portalo registruotų naudotojų paskyrų
   skaičius

| |image24|
| 18 pav. Organizacijos tvarkytojo aplinkos pradinio lango fragmentas

Darbas su organizacijos AD tvarkytojais (Koordinatoriai)
========================================================

*Šis skyrius skirtas tik Koordinatoriams.*

1. Pagrindiniame meniu išskleiskite „Naudotojai“ ir pasirinkite
   **„Organizacijų tvarkytojai“**:

|image25|

19 pav. Organizacijos tvarkytojų paskyrų sąrašo lango meniu

Sąrašo duomenys:

-  **ID** – unikalus paskyros identifikatorius sistemoje. Galite
   tekstiniame lauke jį įvesti arba rikiuoti didėjimo arba mažėjimo
   tvarka spausdami rodykles **[**\ |image26|\ **]** prie stulpelio
   pavadinimo.

-  **El. paštas** – el. paštas, kuriuo registruotos paskyros. Galima
   suvesti jį arba jo fragmentą tekstiniame lauke stulpelio viršuje,
   arba rikiuoti abėcėlės arba atvirkštine tvarka spaudžiant
   **[**\ |image27|\ **]** prie stulpelio pavadinimo.

-  **Organizacija** – teikia duomenis

-  **Vardas**, **Pavardė** – paskyrų naudotojų vardų ir pavardžių
   stulpeliai. Galima suvesti pilną vardą arba pavardę, arba kurio nors
   fragmentą į atitinkamą tekstinį lauką sąrašo viršuje, arba filtruoti
   pagal kurį nors iš laukų abėcėlės arba atvirkštine tvarka spaudžiant
   **[**\ |image28|\ **]** prie kurio nors stulpelio pavadinimo.

-  **Paskutinis prisijungimas** – Data ir laikas, kada naudotojas buvo
   paskutinį kartą prisijungęs prie savo paskyros. Galima rikiuoti nuo
   naujausios arba nuo seniausios datos spaudžiant
   **[**\ |image29|\ **]** prie stulpelio pavadinimo.

-  **Sukurtas** – paskyros sukūrimo data ir laikas. Galima rikiuoti nuo
   naujausios arba nuo seniausios datos spaudžiant
   **[**\ |image30|\ **]** prie stulpelio pavadinimo.

**Sukurti naują savo organizacijos AD tvarkytojo paskyrą:**

-  Spauskite **[+ Pridėti]** ir užpildykite registracijos langą ir
   išsaugokite pakeitimus\ **:**

|image31|

20 pav. Langas pridėti naują organizacijos tvarkytoją

**Redaguoti paskyras:**

-  Sąraše pažymėkite reikiamą paskyrą ir lango meniu spauskite
   **[Redaguoti]**:

|image32|

21 pav. Langas pridėti naują organizacijos tvarkytoją

**Panaikinti paskyrą:**

-  Sąraše pažymėkite paskyrą ir spauskite **[Suspenduoti]**.

   Atsidaro papildomas langas, kuriame pasirinkite naudotoją, kuriam bus
   priskirti duomenys:

|image33|

22 pav. Langas pašalinti pasirinktą paskyrą

**Filtruoti naudotojų sąrašą:**

1. Pasirinkite lauką iš sąrašo;

2. Filtruoti galima pagal kelis laukus vienu metu;

3. Rikiuoti galima vienu metu tik pagal vieną kurį nors stulpelį.

Darbas su organizacijos rekvizitais (Koordinatoriai)
====================================================

*Šis skyrius skirtas tik Koordinatoriams.*

**Redaguoti savo organizacijos pateikiamus aplinkoje duomenis:**

1. Pagrindiniame meniu pasirinkite **„Organizacijos“**.

2. Pasirinkite organizaciją, kurios informaciją norėsite redaguoti.
   Spauskite [**Redaguoti**].

3. Rekvizitų lange redaguokite reikiamus duomenis.

4. Įsitikinę, kad tinkamai užpildėte/redagavote laukus, spauskite
   **[**\ |image34|\ **]** lango apačioje.

5. Norėdami ištrinti pasirinktą organizaciją, spauskite [|image35|]
   lango apačioje.

===================================
=========================================================================================================================================================
|image36|                           Skiltyje **„1. Bendra informacija“** galima redaguoti laukus:
23 pav. Rekvizitų redagavimo langas
                                    -  **Pavadinimas:** pilnas organizacijos pavadinimas;
                                   
                                    -  **Įmonės kodas:** juridinio asmens kodas;
                                   
                                    -  **El. pašto adresas:** kontaktinis organizacijos el. pašto adresas;
                                   
                                    -  **Adresas:** registruotas organizacijos adresas;
                                   
                                    -  **Telefono numeris:** kontaktinis organizacijos telefono numeris;
                                   
                                    -  **Tinklalapis:** nuoroda į organizacijos oficialią svetainę;
                                   
                                    -  **Regionas:** iš sąrašo pasirenkamas apskrities, kurioje registruota organizacija, pavadinimas;
                                   
                                    -  **Savivaldybė:** iš sąrašo pasirenkamas savivaldybės, kuriai priklauso organizacija, pilnas pavadinimas;
                                   
                                    -  **Ministrų valdymo sritis:** ministerija, su kuria susijusi organizacija. Spauskite **[**\ |image37|\ **]** lauko dešinėje pusėje ir išplėsite sąrašą.
===================================
=========================================================================================================================================================
\                                  
===================================
=========================================================================================================================================================

Skiltyje **„2. Logotipas“** galite įkelti naują arba pakeisti įkeltą
organizacijos logotipą:

|image38|

24 pav. Rekvizitų redagavimo langas

Darbas su poreikiais (Koordinatoriai)
=====================================

*Šis skyrius skirtas tik Koordinatoriams.*

*Portalo naudotojams pateikus arba vyr. koordinatoriui priskyrus poreikį
Jūsų organizacijai, gausite pranešimą apie naują poreikį į Jūsų paskyrai
užregistruotą el. paštą.*

Poreikių sąrašo peržiūra
------------------------

1. Pagrindiniame menu pasirinkite **„Atvėrimo poreikiai“**.

| |image39|
| 25 pav. Poreikių sąrašo langas

Bendrame organizacijai pateiktų duomenų atvėrimo poreikių sąraše –
pagrindinė poreikių informacija:

-  **Būsena** – organizacijai pateikto poreikio atvėrimo būsena. Galimos
   reikšmės:

   -  „Pateiktas“, jei organizacijos vardu dar nebuvo atsakyta į
         poreikį,

   -  „Planuojama atverti“, jei poreikis patvirtintas,

   -  „Nenumatytas atverti“, jei poreikis atmestas;

-  **Organizacija** – kuriai pateiktas duomenų atvėrimo poreikis;

-  **Pavadinimas** – duomenų rinkinio, kuriam pateiktas poreikis
   atverti, pavadinimas;

-  **Aprašymas** – trumpas duomenų rinkinio, kuriam pateiktas poreikis
   atverti, aprašymas;

-  **Duomenų rinkinio ID** – duomenų rinkinio unikalus identifikatorius
   sistemoje.

..

   Pateikiamas, jei poreikis skirtas jau atvertą rinkinį atnaujinti;

-  **Formatas** – pageidaujamas duomenų pateikimo formatas;

-  **Sukurtas** – Data ir laikas, kada poreikis buvo sukurtas viešame
   portale;

-  **Komentaras** – koordinatoriaus/ tvarkytojo atsakymas su atvėrimo
   poreikio priežastimi.

*Įsijungus puslapį, sąrašas pateikiamas automatiškai surikiuotas pagal
sukūrimo datą, pateikiant naujausios datos poreikius viršuje.*

Atvėrimo poreikio peržiūra
--------------------------

*Su sąraše pateiktais poreikiais galite:*

-  *Peržiūrėti išsamesnę informaciją;*

-  *Redaguoti kai kuriuos poreikių duomenis;*

-  *Atsakyti į poreikį.*

**Peržiūrėti išsamesnę pateikto poreikio informaciją:**

1. Sąraše pasirinkite poreikį ir du kartus paspauskite ant poreikio.

2. Atverto lango viršuje pateiktas meniu, kuriuo naudojantis pasiekiamos
   atvėrimo poreikio skiltys. Melsvai paryškinta ta skiltis, kurioje tuo
   metu esate. Numatytoji atidaryti skiltis yra **„Įrašo informacija“**:

| |image40|\ |image41|
| 26 pav. Atvėrimo poreikio lango meniu

Šiame lange pateikta pagrindinė poreikio informacija, pateikta poreikio
teikėjo:

-  **Autorius**: poreikio teikėjo vardas, pavardė ir el. paštas;

-  **Registravimo data**: data ir laikas, kada poreikis buvo pateiktas;

-  **Norimas atlikti pakeitimas** – įvardinama, koks konkrečiai
      pakeitimas turėtų būti įvykdytas esamam duomenų rinkiniui.
      Poreikio teikėjas gali pasirinkti nuo vieno iki trijų pakeitimų iš
      pateikto sąrašo;

-  **Pasiūlymas organizacijai** – poreikio teikėjas gali pateikti
      pasiūlymą organizacijai;

-  **Duomenų atnaujinimo periodiškumas:** nurodomas periodas, kas kiek
      laiko turi būti atnaujinti rinkinyje pateikti duomenys;

-  **Patinka paspaudimai:** neredaguotinas laukas, kuriame nurodyta,
      kiek viešos aplinkos naudotojų paspaudė „Patinka“ prie poreikio. Į
      „Patinka“ paspaudimų skaičių atsižvelgiama vertinant poreikio
      prioritetą;

-  **Norimas keisti duomenų rinkinys:** pavadinimas jau esamo duomenų
      rinkinio, kuriam atnaujinti teikiamas poreikis;

-  **Aprašymas:** duomenų rinkinio ir poreikio aprašymas. Pildo
      *poreikio teikėjas*;

-  **Formatas:** kokias formatais atveriamas duomenų rinkinys. Laukas
      neredaguotinas. Pildo *poreikio teikėjas*;

-  **Papildoma informacija:** papildoma informacija apie duomenų rinkinį
      ar poreikį. Pildo *poreikio teikėjas*.

**
**

**Peržiūrėti poreikio teikėjo pateiktą struktūrą:**

1. Pagrindiniame meniu pasirinkite **„Atvėrimo poreikiai“;** du kartus
   paspauskite ant pasirinkto poreikio, kad atsidarytų papildomas meniu
   „Atvėrimo poreikis“, kur pasirinkite „\ **Pageidaujama duomenų
   struktūra**\ “.

| |image42|
| 27 pav. Pageidaujamos duomenų rinkinio struktūros fragmentas

2. Pageidaujama duomenų struktūra aprašoma šiuose laukuose (*: privalomi
   laukai):

-  **Duomenų pavadinimas \*** – Lauko, kuriame pateikiamas tam tikro
      tipo duomuo, pavadinimas;

-  **Duomenų pavadinimas standartiniame žodyne** – duomens pavadinimas,
      atitinkantis lietuvių kalbos taisykles.

-  **Duomenų tipas \***– duomenų tipas, įrašomas anglų kalba.

-  **Pastabos** – laisvai įvedamos pastabos apie duomenis.

3. Duomenų teikėjas duomenų rinkinio struktūrą gali įkelti kaip Excel
   failą: atveju lango viršuje patiekiama nuoroda parsisiųsti failą.

| |struk|
| 28 pav. Reikiamos duomenų struktūros failo atsisiuntimo nuoroda
  poreikio lange

*SVARBU: Tik poreikio teikėjas gali pakeisti pageidaujamą duomenų
struktūrą.*

**Peržiūrėti atvėrimo poreikio būsenų pasikeitimus**

1. Pagrindiniame meniu pasirinkite **„Atvėrimo poreikiai“;** du kartus
   paspauskite ant pasirinkto poreikio, kad atsidarytų papildomas meniu
   „Atvėrimo poreikis“, kur pasirinkite „\ **Būsenų istorija**\ “.

| |poreikist|
| 29 pav. Atvėrimo poreikio lango skiltis „Būsenų istorija“

2. Sąraše atvaizduojami duomenys:

-  **Sukurtas** – Data ir laikas, kada buvo atliktas veiksmas

-  **Būsena** – Veiksmo, kuris buvo atliktas, pavadinimas. Galimos
      reikšmės

   -  „Sukurtas“

   -  „Redaguotas“

   -  „Patvirtintas“

   -  „Atmestas“.

-  **Autorius** – paskyros savininko, atlikusio veiksmus, vardas ir
      pavardė.

-  **Komentaras** – Komentaras, kuris gali būti paliekamas atsakant į
      poreikį.

Atsakymas į pateiktą atvėrimo poreikį
-------------------------------------

1. Pagrindiniame meniu pasirinkite **„Atvėrimo poreikiai“;** du kartus
   paspauskite ant pasirinkto poreikio, kad atsidarytų papildomas meniu
   „Atvėrimo poreikis“, kur pasirinkite „\ **Organizacijos
   atsakymas**\ “.

| |poreik|
| 30 pav. Atvėrimo poreikio lango skilties „Organizacijos atsakymas“
  pavyzdys

2. Užpildykite atsakymo formos laukus:

-  Pasirinkite atsakymą pažymint vieną iš atsakymo laukų:

   -  „Planuojamas atverti“, jei poreikis priimamas ir rinkinys
         planuojamas atverti.

   -  „Nenumatytas atverti“, jei tuo metu duomenų rinkinys nenumatytas
         atverti.

-  Jei rinkinys planuojamas atverti, lauke **„Planuojama atvėrimo
      data“** įveskite numatytą rinkinio atvėrimo datą formatu
      „mm/dd/mmmm“ arba pasirinkę kalendoriuje, spausdami
      **[**\ |sn10|\ **]** dešinėje.

-  Tekstiniame lauke **„Komentaras dėl atvėrimo numatymo arba
      atmetimo“** įrašykite komentarą dėl atsakymo. Ši informacija bus
      pateikta viešame portale bei matoma atvėrimo poreikių sąrašo
      lange.

-  Tekstiniame lauke **„Galutinis organizacijos atsakymas“** įrašykite
      atsakymą dėl atvėrimo ir priežastį. Ši informacija bus pateikta
      poreikio teikėjui.

Spauskite mygtuką **[Saugoti]**, norėdami išsaugoti atsakymą: atsakymas
į poreikį ir jo priežastis bus automatiškai nusiųsta poreikio teikėjui.

Poreikio patvirtinimo būsena po atsakymo gali būti pakeista pagal
poreikį.

Darbas su duomenų rinkiniais
============================

Duomenys į Portalą keliami dviem būdais:

1. Kuriant naują duomenų rinkinį;

..

   *Plačiau:*\ `Naujo duomenų rinkinio sukūrimas ir
   inventorinimas <#_Naujo_duomenų_rinkinio>`__;

2. Importuoti pagal šabloną užpildytą Excel failą;

..

   *Plačiau:*\ `Duomenų šablono
   atsisiuntimas <#duomenų-šablono-atsisiuntimas>`__.

**Importavus duomenų rinkinį:**

1. Koreguokite informaciją.

   *Plačiau:*\ `Duomenų distribucijos
   tvarkymas <#_Duomenų_distribucijos_tvarkymas>`__\ *;*

2. Pereikite prie veiksmų su rinkiniu.

   *Plačiau*: `Duomenų rinkinio struktūros
   sukūrimas <#_Duomenų_rinkinio_struktūros>`__.

   **Išsaugoti įvestą informaciją:**

1. Atitinkamoje kortelėje spauskite **[Saugoti]**.

   **Atšaukti įvestų pakeitimų saugojimą:**

1. Jei pakeitimų atsisakote, spauskite **[Grįžti į sąrašą]**.

Duomenų rinkinių sąrašo peržiūra
--------------------------------

*Organizacijos pačios kuria ir pildo joms priklausančius duomenų
rinkinius. Jei duomenų rinkinys perkeliamas iš vienos organizacijos
kitai, pirmoji netenka prieigos prie jo. Duomenų rinkinių sąrašo lange:*

-  *kurti naujus duomenų rinkinius,*

-  *atsisiųsti duomenų pateikimo šabloną*

-  *importuoti duomenis*

-  *peržiūrėti sukurtų duomenų rinkinių informaciją.*

1. Pagrindiniame meniu spauskite **[Duomenų rinkiniai]**

| |image47|
| 31 pav. Duomenų rinkinių sąrašo langas

2. Sąraše pateikiama pagrindinė duomenų rinkinių informacija:

-  **Eil. Nr.**: duomenų rinkinio eilės numeris duomenų rinkinių sąraše;

-  **ID:** duomenų rinkinio unikalus identifikatorius sistemoje. Pagal
   šį stulpelį taip pat galima ir filtruoti rinkinių sąrašą, įvedus
   skaitinę reikšmę į tekstinį lauką stulpelio pavadinime;

-  **Viešas:** duomenų rinkinio vaizdavimo viešoje aplinkoje būsena. Jei
   pateiktas varnelė **[**\ |image48|\ **]**, rinkinys – pateiktas
   viešoje aplinkoje. Jei lauke pateiktas tuščias apskritimas
   [|image49|], rinkinys matomas tik administracinėje aplinkoje;

-  **Pavadinimas:** duomenų rinkinio pavadinimas; galite filtruoti;

-  **Kategorija:** duomenų rinkiniui priskirta kategorija. galite
   filtruoti ;

-  **Atvėrimo planas:** metai, į kurių planą įtrauktas rinkinys;

-  **Būsena:** duomenų rinkinio kūrimo ir pildymo būsena;

-  **Atvėrimo kaštai:** Suma eurais, reikalinga atverti duomenų rinkinį;

-  **Prioritetas:** duomenų rinkinio prioriteto skaitinė reikšmė;

-  **Sukurtas:** data ir laikas, kada duomenų rinkinys buvo sukurtas.

   **Filtruoti rinkinių sąrašą**\ *:*

1. Įveskite lauko vertę arba jo fragmentą į lauką pasirinkto stulpelio
   pavadinime;

   **Rikiuoti sąrašą pagal stulpelį**\ *:*

1. Spauskite prie pasirinkto stulpelio pavadinimo esantį [|sn2|].

   **Keisti stulpelius vietomis:**

1. Pasirinkite stulpelį ir pelyte jį nutempkite iki reikiamos pozicijos.

Duomenų šablono atsisiuntimas
-----------------------------

*Duomenų rinkinys, įkeliamas kaip failas, privalo atitikti šabloną.*

1. Pagrindiniame meniu spauskite **[Duomenų rinkiniai]**.

2. Duomenų rinkinių lange spauskite mygtuką **[**\ `Atsisiųsti XLSX
      šabloną <https://staging.data.gov.lt/admin/VAADIN/dynamic/resource/4/345e087f-2108-44da-baad-58e0a99757a0/Excel_import_%C5%A1ablonas_v1.1.xlsx>`__\ **]**.

3. Į kompiuterį taip parsisiųsite Excel failą.

4. Pagal gautą šabloną sudarykite (arba užpildykite gautą) duomenų
      failą, kurį galėsite įkelti į ADP.

Duomenų rinkinio importavimas
-----------------------------

1. Pagrindiniame meniu pasirinkite **„Duomenų rinkiniai“**;

2. Duomenų rinkinių sąrašo lange paspauskite **[Importuoti XLSX]**;

*Importuojant XLSX failą, įkeliamas tik aprašas.*

*Inventorinimo, prioritetų, finansiniai ir meta- duomenys nėra
įkeliami.*

*Rinkinio metaduomenys įkeliami atskirai, po aprašymo failo įkėlimo.*

3. Įkelkite failą iš kompiuterio sekdami įkėlimo lango nuorodas.

Naujo duomenų rinkinio sukūrimas ir inventorinimas 
---------------------------------------------------

Inventorinimo duomenys
~~~~~~~~~~~~~~~~~~~~~~

1. Pagrindiniame meniu pasirinkite **[Duomenų rinkiniai]**.

2. Duomenų rinkinių sąrašo lange spauskite **[+ Naujas duomenų
      rinkinys]**.

..

   *Pasirinkus duomenų rinkinį, atidaroma kortelė
   „1. Inventorinimo duomenys“.*

| |Graphical user interface Description automatically generated|
| 32 pav. Duomenų rinkinio inventorinimo duomenų langas.

3. Užpildykite kortelę (*: privalomi laukai):

-  **Pavadinimas*:** pilnas duomenų rinkinio pavadinimas lietuvių kalba;
      žymimas raudonai tol, kol užpildomas;

-  **Aprašymas*:** duomenų rinkinio aprašymas lietuvių kalba; žymimas
      raudonai, kol neužpildomas;

-  **Pavadinimas (anglų k.):** pateikiamas pilnas duomenų rinkinio
      pavadinimas anglų kalba.;

..

   *Jei pirma užpildysite lietuvišką lauką, sistema anglišką pavadinimą
   paruoš automatiškai;*

-  **Aprašymas (anglų k.):** pilnas duomenų rinkinio aprašymas anglų
      kalba;

-  **Pastabos:** skirtas pastaboms apie atveriamų duomenų rinkinius,
      atsakingus asmenis, reikiamas sukurti paskyras rinkiniui tvarkyti.
      Vaizduojamas tik administracinėje aplinkoje;

-  Šiame lange įkelti struktūros ir spausti **[Įkelti struktūros
      failą]** neprivalote: struktūros failus siūlome pateikiami
      skiltyje **„2. Struktūra“** (daugiau: `Duomenų rinkinio struktūros
      sukūrimas <#_Duomenų_rinkinio_struktūros>`__)

4. Įsitikinkite, kad įvedėte teisingus duomenis ir spauskite
      [**Saugoti**].

5. | |Graphical user interface Description automatically generated|
   | 33 pav. Išsaugotos kortelės *1. Inventorinimo duomenys“* sistemos
     pranešimo fragmentas.

*Išsaugojus užpildytą kortelę „1. Inventorinimo duomenys“, atveriamos
sekančios kortelės.*

5. Tęskite kitų kortelių suvedimą. Siūlome kuriant naują rinkinį
   informaciją įvesti nuosekliai.

Struktūra
~~~~~~~~~

*Duomenų naudotojams bus aiškiau, kaip publikuojami duomenys, jei
įkelsite ir struktūrą:*

| |Table Description automatically generated|
| 34 pav. Struktūros failo Excel dokumente pavyzdys

*Kiekvienai struktūrai galite sukurti atskirą failą, kuriame aprašyta,
kokie duomenys atvaizduojami, įvardinant stulpelių pavadinimus bei
antraštes priklausomai nuo to:*

-  *Kiek duomenų rinkinyje yra pateikta failų;*

-  *Kiek iš pateiktų failų turi skirtingas duomenų vaizdavimo
   struktūras.*

1. Duomenų rinkinio lange spauskite lango meniu punktą **„Struktūra“**.

| |Graphical user interface, text, application, email, website
  Description automatically generated|
| 35 pav. Duomenų rinkinio struktūros langas

Duomenų rinkinio struktūros lange pateikiama pagrindinė informacija:

-  **Pridėtas**: data ir laikas, kada struktūros failas buvo pridėtas;

-  **Pavadinimas**: struktūros pavadinimas sistemoje, sukuriamas
      įkeliant struktūros failą;

-  **Failo pavadinimas**: pilnas įkelto struktūros failo pavadinimas;

-  **Standartinis:** požymis, kad duomenų rinkinys yra bendrinės
      struktūros;

-  **Aktualus:** požymis, kad duomenų rinkinys yra naujausios versijos.

Prioritetai
~~~~~~~~~~~

*Pastaba: šiuo metu pildyti šios skilties laukų nėra privaloma.*

   *Prioritetai naudojami sudarant organizacijos metų planus.*

   *Atsižvelgus į suteikiamą finansavimą, apskaičiuojama, kuriems
   rinkiniams suteikiama pirmenybė.*

-  *prioritetus galima įvesti tik suinventorintiems rinkiniams.*

-  *prioritetus galima redaguoti tol, kol rinkinys nėra įtrauktas į
   metinį rinkinių atvėrimo planą.*

1. Pasirinkto suinventorinto duomenų rinkinio lango viršuje meniu
      spauskite **[3. Prioritetai]**

2. Pažymėkite visus tinkamus laukus:

| |Graphical user interface, text, application, email Description
  automatically generated|
| 36 pav. Prioritetų kortelės pirmasis fragmentas

3. Jei galioja: pažymėkite lauką **„Duomenų rinkinys yra atvertas
      mašininiu būdu ...“**.

*Pasirinkimas suteikia maksimalų prioritetą, 100 balų.*

*Pasirinkus daugiau laukų pasirinkti nebegalima.*

4. Kitais atvejais, atskirai pažymėkite tinkamus laukus iš sąrašo.

| |Graphical user interface, text, application, email Description
  automatically generated|
| 37 pav. Prioritetų kortelės fragmentas „Duomenų vertė“

   Laukas **Duomenų vertė (20 balų)**

-  **Duomenų vertė (iki 20 balų) -** Duomenų poreikis pagal duomenų
   tvarkytojo vertinimą. Pažymima, kokiems tikslams duomenys gali būti
   panaudojami.

... rinkinyje yra naudojami duomenys priskirti prioritetiniam
rekomenduojamam atvertinų duomenų sąrašui.

   *Poreikių pasirinkimai suskirstyti trimis laukais.*

   *Kiekvienas iš jų turi po maksimalią prioritetų taškų sumą.*

   Laukai **Duomenų atvėrimo poreikis (50 balų)**

-  Pažymima, kokiems poreikiams buvo pateiktos naudotojų užklausos:.
   kokiems pasirinkimams iš sąrašo portalo naudotojai pateikė poreikį
   atverti duomenų rinkinį.

| |Graphical user interface, text, application, email Description
  automatically generated|
| 38 pav. Prioritetų kortelės fragmentas: „Duomenų poreikis“

Sužymėkite atitinkamus pasirinkimus:

-  Moksliniams tyrimams, studijoms

-  Naujų paslaugų, produktų sukūrimui;

-  Pilietinės visuomenės, demokratinių procesų skatinimu;

-  Visuomenės informavimui;

-  Socialinių ar aplinkosauginių problemų sprendimui;

Lauke **„Duomenų atvėrimo sudėtingumas“** taip pat galima pažymėti šiuos
pasirinkimus:

Duomenų rinkinyje yra asmens duomenų

Duomenų rinkinyje esantys duomenys turės būti transformuojami arba
papildomi susijusiais duomenimis.

| |Graphical user interface, text, application Description automatically
  generated|
| 39 pav. Prioritetų kortelės antras fragmentas

Į tekstinį lauką pagal poreikį įveskite duomenų rinkinyje naudojamų
duomenų bazės laukų skaičių.

Lauko numatyta reikšmė „0“ (jei prioritetų pasirinkimai pildomi
kiekviename lauke atskirai).

-  pasirinkite, ar duomenys bus publikuoti automatizuotai nuskaitomu
   formatu, jei taip, kokiu formatu(-ais):

CSVXMLHDF5JSONRDF

Kiekvienas iš formatų taip pat suteikia reitingą duomenų rinkiniui,
remiantis Tim Berners-Lee modeliu:

-  1 - priskiriama PDF ir analogiškiems formatams;

-  2 - priskiriamos XLSX ir analogiškiems formatams;

-  3 - priskiriamos CSV ir analogiškiems formatams;

-  4 - priskiriamos RDF ir analogiškiems formatams;

-  5 - priskiriamos RDF ir analogiškiems formatams, kai duomenys yra
      susieti su kitais duomenų rinkiniais.

| |Graphical user interface, text, application Description automatically
  generated|
| 40 pav. Prioritetų kortelės paskutinis fragmentas

5. Pasirinkite visus reikiamus laukus

6. Spauskite mygtuką **[Saugoti]** ir sistema išsaugos kortelės laukų
      informaciją.

7. Tęskite kitų kortelių suvedimą.

Finansiniai duomenys
~~~~~~~~~~~~~~~~~~~~

*Pastaba: šiuo metu pildyti šios skilties laukų nėra privaloma.*

*Duomenų rinkinių finansiniai duomenys įvedami siekiant apskaičiuoti
reikalingą atverti sumą visiems metų plano rinkiniams.
Daugiau:*\ `Darbas su metiniais planais <#_Darbas_su_metiniais>`__\ *.*

*Finansinius duomenis galima įvesti tik suinventorintiems rinkiniams su
nustatytais prioritetais.*

*Duomenų rinkinio finansinius duomenis galima redaguoti tol, kol
rinkinys nėra įtrauktas į metinį planą.*

*Įvertinus rinkinio finansavimą, jį galima įtraukti į metinį planą.*

2. Pasirinkto duomenų rinkinio lango meniu spauskite **[4. Finansiniai
   duomenys]**.

| |Graphical user interface, text, application, email Description
  automatically generated|
| 41 pav. Finansinių duomenų kortelės langas

3. Lauke **„Reikalingi finansiniai ištekliai duomenų atvėrimui (EUR)“**
   įveskite sumą, reikalingą atverti duomenis. Rašykite natūraliaisiais
   skaičiais, be kablelių ir taškų.

..

   *Įvesta suma – viena iš sąlygų, pagal kurias vertinamas bendras
   rinkinio prioritetas metinių planų sąraše. Pirmenybė teikiama
   pigesniems rinkiniams.*

4. Jei norite, išsaugokite pakeitimus ir tęskite kitų kortelių suvedimą.

Metaduomenų įvedimas
~~~~~~~~~~~~~~~~~~~~

*Rinkinys jau turi būti suinventorintas, turėti įvestus prioritetus ir
finansinius duomenis.*

1. Spauskite **[5. Metaduomenys]**.

| |Graphical user interface, text, application, email, Teams Description
  automatically generated|
| 42 pav. Duomenų rinkinio metaduomenų įvedimo/redagavimo lango pirmas
  fragmentas

| |Graphical user interface, text, application Description automatically
  generated|
| 43 pav. Duomenų rinkinio metaduomenų įvedimo/redagavimo lango antras
  fragmentas

2. Užpildykite laukus pagal poreikį (\* – privalomi; A – automatiniai):

-  **Kategorija*:** iš sąrašo pasirenkama, kokiai kategorijai priklauso
      duomenų rinkinys;

-  **Licencija:** iš sąrašo pasirenkama duomenų rinkiniui taikoma
      licencija.

..

   *Pasirinkus kurią nors licenciją, pateikiama nuoroda į ją, kad
   galėtumėte patikrinti, ar pasirinkta licencija tinkama;*

-  **AD koordinatorius (A):** iš sąrašo pasirenkamas organizacijos
      koordinatorius;

-  **Sukurtas (A):** data ir laikas, kada duomenų rinkinys buvo
      sukurtas;

-  **Duomenų šaltinis (A):** duomenų rinkinio distribucijos šaltinio
      failo pavadinimas;

-  **Prieigos teisės:** lauke įvardinama, kas turi prieigos teises prie
      duomenų rinkinio, jei prieiga yra ribota;

-  **Periodo pradžia**: rinkinyje pateiktų duomenų periodo pradžia.
      Neredaguotina, nustatoma automatiškai, nurodant anksčiausią
      visuose įkeltuose rinkinio failuose periodo pradžios datą
      (nurodoma keliant duomenų failą). Neįkėlus nei vieno duomenų
      failo, laukas rodomas tuščias; nustatoma automatiškai. Jei
      nežinoma, rašoma reikšmė „Nežinoma“;

-  **Raktiniai žodžiai*:** suvedami raktiniai žodžiai, tinkami duomenų
      rinkiniui, naudojami portalo naudotojų viešoje aplinkoje atliekant
      išplėstinę paiešką. Visus raktinius žodžius rašykite mažosiomis
      raidėmis, tarpusavyje atskirkite kableliais. Rekomenduojama
      nurodyti iki 6 raktinių žodžių;

-  **Įvertinimas:** viešoje aplinkoje registruotų naudotojų pateiktas
      bendras duomenų rinkinio įvertinimas 5 balų skalėje;

-  **Kalba:** iš sąrašo pasirenkama kalba, kuria bus atveriamas duomenų
      rinkinys. Kalbų skaičius neribojamas;

-  **Katalogas:** iš sąrašo pasirinkite „Lietuva“;

-  **Duomenų atnaujinimo periodiškumas:** iš sąrašo pasirenkama, kokiu
      dažnumu atnaujinami rinkinio duomenys;

-  **AD Tvarkytojas*:** iš sąrašo pasirenkamas organizacijos AD
      tvarkytojas. Laukas užpildomas automatiškai, tačiau gali būti
      redaguotas. Laukas privalomas;

-  **Atnaujintas (A):** paskutinio rinkinio atnaujinimo data ir laikas;

-  **Vidinis ID:** rinkinio identifikatorius Portalo sistemoje;

-  **Formatas (A):** formatas(-ai), kuriuo(-iais) atveriamas rinkinys;

-  **Periodo pabaiga:** rinkinyje jau pateiktų duomenų periodo pabaiga.
      Nustatoma automatiškai, priklausomai nuo to, kokia periodo pabaiga
      visuose įkeltuose failuose nurodyta vėliausia. Neįkėlus nei vieno
      duomenų failo, laukas rodomas tuščias;

-  **Portalo duomenų rinkinio ID (A):** duomenų rinkinio unikalus
      identifikatorius sistemoje;

-  **Atvirumas:** duomenų rinkinio atvirumo lygis skalėje nuo 1 iki 5.

-  **Platinimo sąlygos:** įvedamos sąlygos platinti duomenų rinkinį.

..

   Lango apačioje pateikta prioriteto balų suma.

| |Graphical user interface, text, application, chat or text message
  Description automatically generated|
| 44 pav. Duomenų rinkinio metaduomenų įvedimo/redagavimo lango apatinis
  fragmentas

3. Užpildžius reikiamus laukus, galite spauskite mygtuką **[Saugoti]**
      arba pereikit prie kitų kortelių pildymo.

..

   *Išsaugojus rinkinio būsena bus pakeista į*\ **„Užpildyti
   metaduomenys“**

*
*

   *Jei spaudžiate*\ **[Saugoti]**\ *neužpildę kai kurių privalomų
   laukų, net jei jie buvo neužpildyti ir išsaugoti prieš Jums
   atsidarant metaduomenų langą, sistema parodys papildomą langą,
   kuriame pateikiami privalomi neužpildyti DCAT laukai.*

   *Paaiškinimo lange galite tik įvesti lauko neužpildymo priežastį. Jei
   norite lauką užpildyti, paaiškinimo lange
   spauskite*\ **[Atšaukti]**\ *ir grįšite prie pildymo.*

-  Tekstiniuose laukuose įveskite priežastį kiekvienam DCAT laukui,
   kurio neužpildėte.

| |image64|
| 45 pav. Duomenų rinkinio metaduomenų neužpildymo paaiškinimo lango
  pavyzdys

Nurodyta priežastis bus matoma poreikio peržiūros lango skiltyje
**„Įvykių istorija“**, komentaro lauke.

| |01|
| 46 pav. DCAT lauko neužpildymo priežasties peržiūros pavyzdys

Įvedę priežastis neužpildyti privalomiems laukams, spauskite
**[Saugoti]**.

4. Spauskite **[Saugoti]** metaduomenų įvedimo lange, kad išsaugotumėte
      įvestus duomenis arba pakeitimus.

Duomenų distribucijos tvarkymas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Rinkinio duomenys gali būti įkeliami, kai užpildyta kortelė*\ **„1.
Inventorinimo duomenys“**

1. Duomenų rinkinio lango meniu spauskite mygtuką **[6. Duomenys]**.

2. Sistema parodys duomenų įkėlimui skirtą langą.

| |Graphical user interface, text, application, chat or text message
  Description automatically generated|
| 47 pav. Duomenų rinkinio duomenų distribucijos langas

Lange pateiktas sąrašas įkeltų nuorodų ir failų, kuriuose pateikti
duomenys, nurodant šią informaciją:

-  **ID** – unikalus failo arba nuorodos ID sistemoje, sugeneruojamas
      automatiškai įkeliant;

-  **Pavadinimas** – failo arba nuorodos pavadinimas sistemoje;

-  **Aprašymas** – trumpas failo arba nuorodos aprašymas;

-  **Tipas** – nurodoma „FILE“, jei tai yra failas, arba „URL“, jei tai
      nuoroda;

-  **Dokumentas** – įkelto failo pilnas pavadinimas. Jei tai nuoroda,
      laukas paliekamas tuščias;

-  **Nuoroda** – įkelta pilna nuoroda (su pradžia http:// arba
      https://). Jei tai failas, laukas paliekamas tuščias;

-  **Versija** – skaičiumi nurodoma, kelinta tai įkelta to failo arba
      nuorodos versija;

-  **Įkelta** – data ir laikas, kada nuoroda arba failas buvo įkeltas;

-  **Atnaujinta** – data ir laikas, kada nuoroda arba failas buvo
      paskutinį kartą atnaujintas.

3. Įkelkite naują distribuciją:

-  kaip failą: spauskite **[+ Įkelti duomenų rinkinio distribucijos
      failą]**.

-  kaip nuorodą, spauskite mygtuką **[+Įkelti duomenų distribucijos
      nuorodą]**.

   *Sistema parodys naujos distribucijos langą.*

| |Screenshot (235)|
| 48 pav. Naujos distribucijos kaip failo įkėlimo langas

4. Užpildykite reikiamus laukus:

-  **Pavadinimas** – Įkeliamo duomenų failo pavadinimas. Privalomas
      laukas;

-  **Savivaldybė** – Savivaldybė, kuriai priklauso įkeliamas duomenų
      rinkinio failas. Neprivalomas laukas;

-  **Laikotarpio pradžia** – Įkeliamo failo laikotarpio pradžia.
      Privalomas laukas;

-  **Aprašymas** – Įkeliamo duomenų failo aprašymas. Privalomas laukas;

-  **Regionas** – Regionas, kuriam priklauso įkeliamas failas.
      Neprivalomas laukas;

-  **Laikotarpio pabaiga** – Įkeliamo failo laikotarpio pabaiga.
      Privalomas laukas.

..

   *Failo įkėlimas privalomas pridedant distribuciją.*

5. Spauskite mygtuką **[Upload files]** arba nutempkite failą iki lauko
   **{Drop files here}**.

6. Jei distribuciją keliate kaip nuorodą, nuorodos įkėlimo lange vietoje
   suveskite privalomus laukus:

-  **Formatas*:**\ *iš sąrašo pasirinkite vieną duomenų distribucijos
      formatą;*

-  **Nuoroda*:**\ *nuoroda į distribuciją.*

| |image68|
| 49 pav. Distribucijos nuorodos įkėlimo langas

7. Užpildę laukus, spauskite **[Saugoti]**.

*Naujai įkeltas failas ar nuoroda bus iškart matomi distribucijų lange
esančiame sąraše:*

| |Graphical user interface, text, application Description automatically
  generated|
| 50 pav. Duomenų distribucijų sąrašo pavyzdys

**Redaguoti distribuciją:**

-  Įkeltų distribuciją atnaujinimai atliekami tik per API.

   **Pašalinti distribuciją iš sąrašo:**

-  pažymėkite ją sąraše ir spauskite **[Šalinti distribuciją]** ekrano
   viršuje.

2. Struktūros kūrimo lange paspauskite mygtuką **[Įkelti failą]**.

| |image70|
| 51 pav. Struktūros failo įkėlimo langas

3. Struktūros įkėlimo lange užpildykite privalomą tekstinį lauką
      **„Pavadinimas“**

4. Spauskite **[Upload File]** ir įkelkite failą iš kompiuterio.

5. Norėdami išsaugoti įkeltus failus, spauskite **[Saugoti]** lango
      apačioje.

*Įkelti failai bus pateikti viešoje aplinkoje, duomenų rinkinio
peržiūroje.*

*Įkeltų struktūros failų redaguoti nebegalima, tik įkelti iš naujo.*

   **Pašalinti kurį nors įkeltą failą:**

-  pažymėkite jį sąraše

-  paspauskite **[Šalinti failą]** sąrašo viršuje.

Pateikti poreikiai
~~~~~~~~~~~~~~~~~~

1. Rinkinio peržiūros lango meniu pasirinkite skiltį **„Pateikti
   poreikiai“**.

| |image71|
| 52 pav. Duomenų rinkiniui pateiktų poreikių peržiūros langas

Poreikių peržiūros lange galite tik peržiūrėti pateiktų poreikių
informaciją:

-  **Pateiktas** – data ir laikas, kada poreikis buvo pateiktas;

-  **Aprašymas** – poreikio teikėjo pateiktas poreikio aprašymas;

-  **Pastabos** – pastabos tekstas.

Duomenų rinkinio istorijos peržiūra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Duomenų rinkinio lango** viršuje esančiame meniu pasirinkite skiltį
   **„Įvykių istorija“**.

| |image72|
| 53 pav. Duomenų rinkinio istorijos langas

Lange pateikti rinkinio istorijos duomenys, automatiškai kaupiami nuo
duomenų rinkinio sukūrimo:

-  **Data:** data ir laikas, kai buvo atliktas veiksmas su duomenų
      rinkiniu (sukūrimas, redagavimas);

-  **Autorius:** vardas ir pavardė paskyros, kuria atitinkamas veiksmas
      buvo atliktas, savininko;

-  **Įvykis:** įvardinama, kas buvo atlikta: redaguotas rinkinys,
      pakeistas jo statusas (būsena) ir t.t.;

-  **Komentaras:** koordinatoriaus paliktas komentaras redaguojant
      rinkinį (pvz., priežastys, kodėl tam tikri metaduomenų lango
      laukai palikti neužpildyti). Jei atliktas veiksmas nereikalavo
      paliekamo komentaro, laukas paliekamas tuščias.

Duomenų rinkinio pastabų peržiūra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Tvarkant duomenų rinkinių atvėrimo planus, gali būti pateiktos
pastabos.*

*Pastabos peržiūrimos per duomenų rinkinį arba metinį planą.*

*Peržiūrėti pastabas per metinį planą: sąraše pasirinkite metinio planą,
stulpelyje*\ **„Pastaba“**\ *.*

1. Pagrindiniame meniu pasirinkite **„Duomenų rinkiniai“**, rinkinių
      sąrašo lange pasirinkite reikiamą rinkinį;

2. Duomenų rinkinio lango viršuje esančiame meniu pasirinkite
      **„Pastabos“**.

| |image73|
| 54 pav. Duomenų rinkinio pastabų sąrašo lango fragmentas

Lange pateikiama pagrindinė pastabų informacija:

-  **Data** – data ir laikas, kada pastaba buvo pateikta;

-  **Autorius** – vardas ir pavardė pastabą parašiusios paskyros
      savininko;

-  **Pastaba** – pateiktas pastabos tekstas.

Sąraše galite pasirinkti reikiamą pastabą, kad atvertumėte jos peržiūros
langą ir galėtumėte perskaityti pilną pastabos tekstą.

| |past01|
| 55 pav. Duomenų rinkiniui pateiktos pastabos peržiūros langas

*Pateiktų pastabų redaguoti negalima, tik peržiūrėti.*

*Naujos pastabos pateikiamos, kai vyr. koordinatorius atmeta iš naujo
nacionaliniam planui pateiktą organizacijos duomenų rinkinį.*

Darbas su IRS rinkiniais
~~~~~~~~~~~~~~~~~~~~~~~~

| |image75|
| 56 pav. IRS rinkinių sąrašo langas

IRS rinkinių sąraše galima peržiūrėti tokią bendrą informaciją:

-  **Eil. nr.** – rinkinio numeris sąraše, sugeneruotas portale
      automatiškai;

-  **ID** – unikalus rinkinio identifikatorius sistemoje, sugeneruotas
      automatiškai importuojant rinkinį. Pagal stulpelį taip pat galima
      filtruoti sąrašą, įvedus skaitinę reikšmę į tekstinį lauką
      stulpelio pavadinime;

-  **Viešas** – rinkinio viešumo portalo viešoje aplinkoje būsena.
      Laukas žymimas varnele **[**\ |image76|\ **]**, jei rinkinys –
      viešas;

-  **Pavadinimas** – pilnas duomenų rinkinio pavadinimas. Pagal stulpelį
      taip pat galima filtruoti sąrašą, įvedant rinkinio pavadinimą arba
      jo fragmentą į tekstinį lauką stulpelio pavadinime;

-  **Tvarkytojas** – Organizacijos tvarkytojo, atsakingo už rinkinį,
      vardas ir pavardė. Pagal stulpelį taip pat galima filtruoti
      sąrašą, įvedant vardą ir pavardę, arba kurio nors iš jį fragmentą
      į tekstinį lauką stulpelio pavadinime. Laukas gali būti
      pateikiamas tuščias;

-  **Atnaujintas** – data ir laikas, kada rinkinys buvo paskutinį kartą
      atnaujintas.

**Redaguoti IRS rinkinį:**

paspausti ant IRS rinkinio, kurį norite peržiūrėti/ tikslinti/
sutvarkyti eilutės (40).

|Graphical user interface, email Description automatically generated|

==================================================================================================================================
SVARBU. IRS rinkinį reikia pašalinti, jeigu duomenų rinkinys nebėra aktualus, arba jau yra įvesta naujas panašus duomenų rinkinys.
==================================================================================================================================

IRS rinkinius galima redaguoti. Tikslinant IRS rinkinius galioja tos
pačios taisyklės, kaip ir naujo duomenų rinkinio įvedimo atveju.

Pagal bet kurį pasirinktą stulpelį (vieną stulpelį vienu metu) sąrašas
gali būti rikiuojamas spaudžiant stulpelio pavadinimą, arba mygtuką
**[**\ |image78|\ **]**. Stulpelis, pagal kurį sąrašas tuo metu
rikiuojamas, paryškinamas mėlynai.

Sąrašas pildomas automatiškai, importuojant rinkinius iš atitinkamų
portalų.

Darbas su metiniais planais
===========================

*Metiniai planai sudaromi ruošiantis duomenų rinkinių atvėrimui.*

*Ruošiant metinius planus atsižvelgiama į duomenų prioritetą bei
finansavimą.*

*Organizacijos koordinatorius atsako už organizacijos atveriamų duomenų
rinkinių metinio plano:*

-  *Sudarymą;*

-  *pateikimą vyr. koordinatoriui,*

-  *plano redagavimą, jei vyr. koordinatorius planą atmeta,*

-  *patvirtinimą organizacijos vardu, jei vyr. koordinatorius planą
   patvirtina.*

Metinio plano sudarymas
-----------------------

1. Pagrindiniame meniu pasirinkite **„Atvėrimo planai“**.

2. Atsivėrusiame metinių atvėrimų plane spauskite **[+ Naujas duomenų
      atvėrimo planas]**.

| |image79|
| 57 pav. Atvėrimo planų sąrašo langas

Lange pateikiama pagrindinė atvėrimo planų informacija:

-  **Eil. nr. –** atvėrimo plano eilės vieta sąraše;

-  **Metai –** metai, kuriems skirtas atvėrimo planas;

-  **Planuojami kaštai (EUR) –** suma eurais, reikalinga pilnai
      finansuoti duomenų rinkinį;

-  **Planuojami duomenų rinkiniai –** skaičius duomenų rinkinių, kurie
      įtraukti į atvėrimo planą;

-  **Numatytas finansavimas (EUR) –** suma eurais, skirta finansuoti
      metų planą;

-  **Finansuoti duomenų rinkiniai –** duomenų rinkinių, kuriems buvo
      vyr. koordinatoriaus skirtas finansavimas, skaičius;

-  **Būsena –** atvėrimo plano būsena. Galimos reikšmės:

   -  Formuojamas: organizacija dar kuria/redaguoja planą,

   -  Pateiktas: planas pateiktas vyr. koordinatoriui, bet į jį dar
         nebuvo atsakyta;

   -  Patvirtintas koordinatoriaus: vyr. koordinatorius patvirtino
         planą;

   -  Patvirtintas organizacijos: po vyr. koordinatoriaus patvirtinimo
         planas buvo vėl patvirtintas organizacijos.

3. Naujo metinio plano lange įveskite, kuriems metams norite sukurti
      atvėrimo planą ir spauskite mygtuką **[Sukurti]**.

| |image80|
| Metinio plano metų pasirinkimo langas

Metinio plano formavimas ir pateikimas
--------------------------------------

1. Pagrindiniame meniu spauskite pasirinkite **„Atvėrimo planai“**.

2. Atvėrimo planų lange pasirinkite planą, kurį norite formuoti.

| |image81|
| 58 pav. Metinio duomenų atvėrimo plano langas

Metinio duomenų atvėrimo plano lango viršuje – plano būsena ir
reikalingas finansavimas, suma EUR.

| |image82|
| 59 pav. Metinio duomenų atvėrimo plano lango poskyrių meniu

Numatyta lango įjungimo skiltis **„Duomenų rinkiniai“**. Skiltis
**„Istorija“** tampa prieinama (tapusi prieinama patamsėja) atlikus
kokius nors veiksmus su planu.

3. Pasirinkto metinio plano lange spauskite mygtuką **[Formuoti <Jūsų
      pasirinkti metai> metų planą]**, esantį virš metinio duomenų
      atvėrimo plano lango poskyrių meniu.

4. Atvertame rinkinių įtraukimo lange, pasirinkite, kurie rinkinių
      poreikiai turi būti įtraukti į metinį planą, pažymėdami žymimąjį
      laukelį rinkinio kairėje pusėje.

| |image83|
| 60 pav. Pasirinkto metinio duomenų atvėrimo plano langas

   Sąraše pateikti tik tie rinkiniai, kurie priskirti Jūsų
   organizacijai, yra nepriskirti kitam metiniam planui, neturi įkeltų
   duomenų ir kurių būsena yra **„Įvertintas finansavimas“** arba
   **„Užpildyti metaduomenys“**.

5. Įsitikinę, jog pasirinkote visus reikiamus rinkinius, spauskite
      mygtuką **[Patvirtinti]**.

..

   **Pastaba**\ *: į metinį planą įtrauktų duomenų rinkinių prioritetų
   ir finansinių duomenų nebegalima redaguoti. Juos bus galima redaguoti
   tik pašalinus rinkinį iš plano. Daugiau:*\ `Metinio plano
   išformavimas <#_Metinio_plano_išformavimas>`__

6. Metinio plano lange spauskite mygtuką **[Pateikti planą vyr.
      koordinatoriui]**.

..

   Pateikto plano nebebus galima redaguoti, išformuoti ar pateikti iš
   naujo. Tokie veiksmai atlikti su planu bus galimi tik vyr.
   koordinatoriui jį atmetus. Vyr. koordinatorius, atmesdamas planą,
   pateikia pastabas atitinkamiems į planą įtrauktiems duomenų
   rinkiniams, nurodydamas ką konkrečiai reikia redaguoti.

Metinio plano išformavimas
--------------------------

*Į metinį planą įtraukti duomenų rinkiniai negali būti įtraukti į kitus
rinkinius bei negali būti redaguoti jų prioritetai ir finansiniai
duomenys, net jei pateiktas planas buvo atmestas.*

*Dabartinį planą turite išformuoti, kad duomenų rinkinys nebebūtų jam
priskirtas:*

-  *Kai rinkinys turi būti paliktas kitų metų planui;*

-  *Kai reikia pakeisti prioritetus ir/arba finansinius duomenis.*

..

   **Pastaba**\ *: išformuoti negalite planų, kurie yra patvirtinti vyr.
   koordinatoriaus arba organizacijos, arba įtraukti į jau patvirtintą
   nacionalinį duomenų rinkinių atvėrimo planą.*

**išformuoti metinį planą:**

-  pasirinkite reikiamą planą sąraše

-  jo lange spauskite **[Formuoti <metai> metų planą]**.

-  Rinkinių įtraukimo lango apačioje spauskite mygtuką **[Išformuoti
   planą]**.

| |image84|
| 61 pav. Metinio plano išformavimo mygtukas

-  Spauskite **[Patvirtinti]**, jei tikrai norite išformuoti planą.

| |image85|
| 62 pav. Metinio plano išformavimo patvirtinimo langas

   Planas tebeliks matomas planų sąraše ir jį bus galima formuoti iš
   naujo įtraukiant rinkinius, tačiau jis bus tuščias, o jam buvę
   priskirti rinkiniai nebebus jam priskirti ir juos bus galima
   priskirti kitiems metiniams planams.

Plano patvirtinimas organizacijos vardu
---------------------------------------

*Kai metinis planas yra patvirtintas vyr. koordinatoriaus (plano būsena
pasikeičia į*\ **“Patvirtintas koordinatoriaus”**\ *, organizacijos
koordinatorius gali jį patvirtinti vyr. koordinatoriui).*

1. Pagrindiniame meniu spauskite pasirinkite **„Atvėrimo planai“**.

2. Atvėrimo planų lange pasirinkite planą, kurį norite patvirtinti (jo
      būsena turi būti **„Patvirtintas koordinatoriaus“**).

3. Plano lange spauskite mygtuką **[Patvirtinti planą organizacijos
      vardu]**.

| |image86|
| 63 pav. Metinio plano patvirtinimo organizacijos vardu pavyzdys

4. Pasirinkimo patvirtinimo lange spauskite **[Taip]**, kad
   patvirtintumėte planą organizacijos vardu.

   Patvirtinus, plano būsena pasikeis į „Patvirtintas organizacijos“ ir
   bus matomas vyr. koordinatoriui.

| |image87|
| 64 pav. Plano patvirtinimo organizacijos vardu langas

Ataskaitų formavimas
====================

-  Ataskaitoje **Atvirų duomenų rinkinių naudojimo intensyvumo detalūs
      duomenys** pateikiami duomenys apie *duomenų rinkinių* panaudojimą
      nurodytu laikotarpiu;

-  Ataskaitoje **Atvirų duomenų rinkinių naudojimo intensyvumo detalūs
      duomenys (failams)** pateikiami duomenys apie *duomenų rinkinių
      rinkmenų* panaudojimą nurodytu laikotarpiu.

Ataskaitų kūrimas
-----------------

**Suformuoti ataskaitą:**

1. Pagrindiniame meniu išskleiskite punktą **„Ataskaitos“** ir
      paspauskite ant norimo ataskaitos tipo.

2. Pasirinktos ataskaitos lange spauskite **[Formuoti]**.

| |sn41|
| 65 pav. Ataskaitos formavimo langas

3. Užpildykite reikiamus laukus

4. Formos apačioje spauskite **[Formuoti].**

*Suformuota ataskaita bus pateikta ekrane.*

**Atsisiųsti suformuotą rezultatą kaip Excel dokumentą:**

-  suformuotos ataskaitos lango viršuje spauskite **[Atsisiųsti XLSX]**.

**Performuoti tokio paties tipo ataskaitą:**

-  spauskite mygtuką **[Formuoti]**.

   *Formuojant ataskaitą nurodyti kriterijai yra pateikiami lango
   viršuje.*

Paruoštų ataskaitų valdymas
---------------------------

**Rikiuoti stulpelį abėcėlės arba atvirkštine tvarka:**

-  Spauskite stulpelio pavadinimą.

   **Filtruoti stulpelį:**

-  *Tekstiniams* laukams įveskite savo paiešką į tekstinį lauką po
   stulpelio pavadinimu.

-  *Skaitiniams* laukams įveskite skaitines reikšmes į laukus „Nuo“
   ir/arba „Iki“ po stulpelio pavadinimu.

-  *Datoms* įveskite arba pasirinkite datas kalendoriuose arba įveskite
   jas laukuose „Nuo“ ir/arba „Iki“ po stulpelio pavadinimu.

   **Tvarkyti ataskaitos stulpelių eiliškumą:**

-  Nutempkite pasirinktą stulpelį iki reikiamos pozicijos.

   **Keisti suformuotos ataskaitos stulpelius vietomis:**

-  Pasirinktą stulpelį nutempkite iki reikiamos pozicijos.

Ataskaita „Atvirų duomenų rinkinių naudojimo intensyvumo detalūs duomenys“
--------------------------------------------------------------------------

| |image89|
| 66 pav. Ataskaitos „Atvirų duomenų rinkinių naudojimo intensyvumo
  detalūs duomenys“ formavimo forma

Ataskaitos laukai ( \* – privalomi ):

-  **Ministrų valdymo sritys**: iš sąrašo pasirinkite ministerijų
   pavadinimus, galite pasirinkti daugiau nei vieną.

-  **Organizacijos:** pasirinkite iš sąrašo arba įveskite pavadinimus
   organizacijų, kurių duomenų rinkinius norima įtraukti į ataskaitą.

-  **Savivaldybė:** pasirinkite iš sąrašo visas savivaldybes, su
   kuriomis susiję duomenų rinkiniai.

-  **Kategorijos:** pasirinkite iš sąrašo arba įveskite (jei įvestis
   atitinka kurį nors sąrašo elementą) visas kategorijas sričių, su
   kuriomis susiję duomenų rinkiniai turi būti įtraukti į ataskaitą.

-  **Data nuo:** pasirinkite iš kalendoriaus arba įveskite
   **laikotarpio, kuris įtraukiamas į ataskaitą,** pradžios data.

-  **Data iki \*:** pasirinkite iš kalendoriaus arba įveskite
   **laikotarpio, kuris įtraukiamas į ataskaitą, pabaigos data.**

-  **Būsena: pasirenkite iš sąrašo visas duomenų rinkinių, įtraukiamų į
   ataskaitą, būsenas.**

*
*

*Suformavus ataskaitą, duomenys pateikiami ataskaitos lange.*

| |image90|
| 67 pav. Ataskaitos „Atvirų duomenų rinkinių naudojimo intensyvumo
  detalūs duomenys“ langas

Suformuotos ataskaitos lange pateikiami šie įtraukto duomenų rinkinio
laukai:

-  **Eil. nr.**: eilės numeris ataskaitoje.

-  **Organizacijos pavadinimas:** savininkės organizacijos pavadinimas.

-  **Duomenų rinkinio pavadinimas:** įtraukto duomenų rinkinio
   pavadinimas.

-  **Savivaldybė:** priskirtos savivaldybės pavadinimas.

-  **Ministrų valdymo sritys:** priskirtos ministerijos pavadinimas.

-  **Kategorijos:** priskirtos kategorijos.

-  **Peržiūrų skaičius:** duomenų rinkinio peržiūrų skaičius.
   (Skaitinis)

-  **Parsisiuntimų skaičius per portalą:** duomenų rinkinio
   parsisiuntimų per portalą skaičius. (Skaitinis)

-  **Parsisiuntimų skaičius per API:** duomenų rinkinio parsisiuntimų
   per API skaičius. (Skaitinis)

-  **Duomenų rinkinio failai:** duomenų rinkinio failų skaičius.
   (Skaitinis)

-  **Įkėlimo data:** duomenų rinkinio įkėlimo į Portalą data. (Data)

-  **Atnaujinimo data:** duomenų rinkinio atnaujinimo data. (Data)

-  **Brandos lygis:** brandos lygio skaitmuo.

-  **Būsena:** „Inventorintas“, „Suvesti duomenys“, „Užpildyti
   metaduomenys“, „Įvertintas finansavimas“, arba „Įvertinti
   prioritetai“.

**Atidaryti ataskaitos šablono keitimo langą:**

-  *Paspauskite ant bet kurio stulpelio pavadinimo dešiniuoju pelės
   klavišu.*

| |image91|
| 68 pav. Ataskaitos „Atvirų duomenų rinkinių naudojimo intensyvumo
  detalūs duomenys“ šablono keitimo lango fragmentas

Lange pateikti stulpelių pavadinimai bei jų rodymo ataskaitoje būsena.

-  Jei stulpelio būsenos reikšmė yra pažymėta varnele
   **„**\ |image92|\ **“**, stulpelis rodomas ataskaitoje.

-  Jei stulpelio būsenos reikšmė yra tuščia (**„**\ |image93|\ **“**).

   **Keisti stulpelio būseną:**

-  Paspauskite būsenos ikoną: varnelę „\ |image94|\ “ arba tuščią lauką
   „\ |image95|\ “.

   **Uždaryti šablono keitimo langą:**

-  Spauskite **[Uždaryti]**.

*Uždarant langą bus išsaugotos naujausios reikšmės.*

**Atstatyti pradines visų būsenų reikšmes:**

-  Spauskite **[Atstatyti]**.

*Šablono keitimo langas bus uždarytas ir reikšmės bus atstatytos į
pradines.*

Ataskaita „Atvirų duomenų rinkinių naudojimo intensyvumo detalūs duomenys (failams)“
------------------------------------------------------------------------------------

| |image96|
| 69 pav. Ataskaitos „Atvirų duomenų rinkinių naudojimo intensyvumo
  detalūs duomenys (failams)“ sudarymo forma

Ataskaitos laukai (\* – privalomi):

-  **Ministrų valdymo sritys**: iš sąrašo pasirinkite kelias
   ministerijas, su kuriomis susiję rinkiniai;

-  **Organizacijos:** iš sąrašo pasirinkite arba įveskite organizacijas,
   kurių rinkinius norima įtraukti į ataskaitą.

-  **Savivaldybė**: įveskite arba pasirinkti iš sąrašo savivaldybes, su
   kuriomis susiję duomenų rinkiniai. galima parenkamų savivaldybių
   skaičius neribojamas.

-  **Kategorijos:** pasirinkti iš sąrašo, arba įvesti (jei įvestis
   atitinka kurį nors sąrašo elementą) kategorijas sričių, su kuriomis
   susiję duomenų rinkiniai turi būti įtraukti į ataskaitą. Kategorijų
   skaičius neribojamas, laukas neprivalomas.

-  **Data nuo \***: pasirinkite iš kalendoriaus arba įveskite ataskaitos
   laikotarpio pradžios datą.

-  **Data iki \*: periodo, kurio laikotarpis turi būti įtraukiamas į
   ataskaitą, pabaigos data. Galima pasirinkti iš kalendoriaus arba
   įvesti**

-  **Formatas – failų, įtraukiamų į ataskaitą, formatas, pasirenkamas iš
   sąrašo. Pasirenkamų formatų skaičius neribojamas. Laukas
   neprivalomas.**

*
*

*Suformavus ataskaitą, duomenys pateikiami ataskaitos lange:*

| |image97|
| 70 pav. Ataskaitos „Atvirų duomenų rinkinių naudojimo intensyvumo
  detalūs duomenys (failams)“ langas

Žemiau pateikiami į ataskaitą įtraukto duomenų rinkinio laukai:

-  **Eil. nr.:** duomenų rinkinio eilės numeris ataskaitoje.

-  **Organizacijos pavadinimas:** savininkės organizacijos pavadinimas.

-  **Duomenų rinkinio pavadinimas:** duomenų rinkinio pavadinimas.

-  **Savivaldybė:** duomenų rinkinio pilnas savivaldybės pavadinimas.
   Jei nėra priskirta, laukas tuščias.

-  **Ministrų valdymo sritys:** priskirtos ministerijos pavadinimas. Jei
   nėra priskirta, laukas tuščias.

-  **Kategorijos: priskirtos kategorijos pavadinimas.**

-  **Peržiūrų skaičius: duomenų rinkinio peržiūrų skaičius.**

-  **Parsisiuntimų skaičius per portalą: įtraukto duomenų rinkinio
   parsisiuntimų skaičius per portalą.**

-  **Parsisiuntimų skaičius per API: įtraukto duomenų rinkinio
   parsisiuntimų skaičius per API.**

-  **Įkėlimo data: įtraukto duomenų rinkinio įkėlimo į Portalą data.**

-  **Atnaujinimo data: įtraukto duomenų rinkinio atnaujinimo data.**

-  **Formatai: duomenų rinkinio formatas arba formatai. Jei formatas
   nepriskirtas, laukas tuščias.**

| |image98|
| 71 pav. Ataskaitos „Atvirų duomenų rinkinių naudojimo intensyvumo
  detalūs duomenys“ šablono keitimo lango fragmentas

Partnerių API
=============

Partnerių API operacijas galima vykdyti tik su organizacijai suteiktu
API raktu. Dėl organizacijai skirto rakto suteikimo kreipkitės į Portalo
vyr. koordinatorių.

Norėdami pasiekti Partnerių API, naršyklėje įveskite nuorodą
https://data.gov.lt/partner/api/1.

| |image99|
| 72 pav. API aplinkos fragmentas

Slaptažodžio keitimas
=====================

1. Prisijunkite prie sistemos.

2. Spustelėkite savo paskyros ikoną **[**\ |image100|\ **]** dešiniame
      ekrano kampe viršuje.

3. Po ikona išskleidžiamame kontekstiniame meniu spustelėkite
      **[Nustatymai]**.

| |Graphical user interface, text, application Description automatically
  generated|
| 73 pav. Paskyros kontekstinis meniu

4. Paskyros lange spustelėkite **[Keisti slaptažodį]**.

5. Slaptažodžio keitimo lange užpildykite visus privalomus laukus:

-  dabartinį slaptažodį;

-  naują slaptažodį;

-  pakartokite naują slaptažodį.

Slaptažodis privalo būti saugus. (Daugiau:
`Sąvokos <#naudojami-terminai-ir-sąvokos>`__, „Saugus slaptažodis“)

| |Graphical user interface, text, application Description automatically
  generated|
| 74 pav. Slaptažodžio keitimo langas

6. Spauskite **[Keisti]**, kad išsaugotumėte naują slaptažodį.

7. Sekantį kartą jungiantis prie sistemos, prisijunkite naudodami
      naująjį slaptažodį.

.. |image0| image:: /static/katalogas/okot/image2.png
   :width: 0.10417in
   :height: 0.12222in
.. |image1| image:: /static/katalogas/okot/image2.png
   :width: 0.10417in
   :height: 0.12222in
.. |Graphical user interface Description automatically generated| image:: /static/katalogas/okot/image3.png
   :width: 5.54178in
   :height: 3in
.. |image3| image:: /static/katalogas/okot/image4.png
   :width: 4.49056in
   :height: 2in
.. |image4| image:: /static/katalogas/okot/image5.png
   :width: 4.49557in
   :height: 2in
.. |Graphical user interface, application Description automatically generated| image:: /static/katalogas/okot/image6.png
   :width: 4.7875in
   :height: 2.12611in
.. |image6| image:: /static/katalogas/okot/image7.png
   :width: 4.49557in
   :height: 2in
.. |Graphical user interface, text, application, chat or text message Description automatically generated| image:: /static/katalogas/okot/image8.png
   :width: 1.64494in
   :height: 1.62798in
.. |Graphical user interface, text, application, chat or text message, website Description automatically generated| image:: /static/katalogas/okot/image9.png
   :width: 3.14498in
   :height: 1.5in
.. |Graphical user interface, website Description automatically generated| image:: /static/katalogas/okot/image10.png
   :width: 2.55663in
   :height: 1.5in
.. |Graphical user interface, website Description automatically generated| image:: /static/katalogas/okot/image11.png
   :width: 5.34663in
   :height: 3.12311in
.. |Graphical user interface, website Description automatically generated| image:: /static/katalogas/okot/image12.jpeg
   :width: 5.06181in
   :height: 1.70417in
.. |Graphical user interface Description automatically generated| image:: /static/katalogas/okot/image3.png
   :width: 5.54178in
   :height: 3in
.. |Graphical user interface Description automatically generated| image:: /static/katalogas/okot/image13.png
   :width: 4.66964in
   :height: 2.71347in
.. |Graphical user interface, text, application, email Description automatically generated| image:: /static/katalogas/okot/image14.png
   :width: 5in
   :height: 2.41303in
.. |Graphical user interface, application Description automatically generated| image:: /static/katalogas/okot/image15.png
   :width: 1.6393in
   :height: 1.75609in
.. |Text Description automatically generated with low confidence| image:: /static/katalogas/okot/image16.png
   :width: 2.98611in
   :height: 0.53997in
.. |Graphical user interface, application Description automatically generated| image:: /static/katalogas/okot/image17.png
   :width: 1.3in
   :height: 2.43671in
.. |image18| image:: /static/katalogas/okot/image18.png
   :width: 1.30486in
   :height: 4.43783in
.. |Screenshot (254)| image:: /static/katalogas/okot/image19.png
   :height: 0.10556in
.. |image20| image:: /static/katalogas/okot/image20.png
.. |Graphical user interface, text, application Description automatically generated| image:: /static/katalogas/okot/image21.png
   :width: 1.2318in
   :height: 1.26515in
.. |Screenshot (256)| image:: /static/katalogas/okot/image22.png
   :width: 0.2in
   :height: 0.1913in
.. |image23| image:: /static/katalogas/okot/image23.png
   :width: 6.69375in
   :height: 2.26319in
.. |image24| image:: /static/katalogas/okot/image24.png
   :width: 6.68542in
   :height: 2.36111in
.. |image25| image:: /static/katalogas/okot/image25.png
   :width: 6.69375in
   :height: 0.94583in
.. |image26| image:: /static/katalogas/okot/image26.png
   :width: 0.14375in
   :height: 0.14375in
.. |image27| image:: /static/katalogas/okot/image26.png
   :width: 0.14375in
   :height: 0.14375in
.. |image28| image:: /static/katalogas/okot/image26.png
   :width: 0.14375in
   :height: 0.14375in
.. |image29| image:: /static/katalogas/okot/image26.png
   :width: 0.14375in
   :height: 0.14375in
.. |image30| image:: /static/katalogas/okot/image26.png
   :width: 0.14375in
   :height: 0.14375in
.. |image31| image:: /static/katalogas/okot/image27.png
   :width: 6.69375in
   :height: 1.77153in
.. |image32| image:: /static/katalogas/okot/image28.png
   :width: 6.69375in
   :height: 1.76319in
.. |image33| image:: /static/katalogas/okot/image29.png
   :width: 3.5in
   :height: 2.22917in
.. |image34| image:: /static/katalogas/okot/image30.png
   :width: 0.58333in
   :height: 0.17431in
.. |image35| image:: /static/katalogas/okot/image31.png
   :width: 0.51183in
   :height: 0.16389in
.. |image36| image:: /static/katalogas/okot/image32.png
   :width: 2.83333in
   :height: 5.94792in
.. |image37| image:: /static/katalogas/okot/image33.png
   :width: 0.17431in
   :height: 0.13611in
.. |image38| image:: /static/katalogas/okot/image34.png
   :width: 2.57292in
   :height: 2.15625in
.. |image39| image:: /static/katalogas/okot/image35.png
   :width: 6.69375in
   :height: 0.65278in
.. |image40| image:: /static/katalogas/okot/image36.png
   :width: 6.6875in
   :height: 2.9375in
.. |image41| image:: /static/katalogas/okot/image37.png
   :width: 6.6875in
   :height: 3.26042in
.. |image42| image:: /static/katalogas/okot/image38.png
   :width: 6.29167in
   :height: 1.02083in
.. |struk| image:: /static/katalogas/okot/image39.png
   :width: 6.6875in
   :height: 1.03125in
.. |poreikist| image:: /static/katalogas/okot/image40.png
   :width: 4.21911in
   :height: 1.7913in
.. |poreik| image:: /static/katalogas/okot/image41.png
   :width: 4.84375in
   :height: 3.125in
.. |sn10| image:: /static/katalogas/okot/image42.png
   :width: 0.1875in
   :height: 0.1875in
.. |image47| image:: /static/katalogas/okot/image43.png
   :width: 6in
   :height: 0.8389in
.. |image48| image:: /static/katalogas/okot/image44.png
   :width: 0.15627in
   :height: 0.15in
.. |image49| image:: /static/katalogas/okot/image45.png
   :width: 0.15in
   :height: 0.15in
.. |sn2| image:: /static/katalogas/okot/image26.png
   :width: 0.14583in
   :height: 0.14583in
.. |Graphical user interface Description automatically generated| image:: /static/katalogas/okot/image46.png
   :width: 5.5631in
   :height: 3in
.. |Graphical user interface Description automatically generated| image:: /static/katalogas/okot/image47.png
   :width: 1.26562in
   :height: 0.43229in
.. |Table Description automatically generated| image:: /static/katalogas/okot/image48.png
   :width: 5.84416in
   :height: 1.40298in
.. |Graphical user interface, text, application, email, website Description automatically generated| image:: /static/katalogas/okot/image49.png
   :width: 6.12738in
   :height: 1.28472in
.. |Graphical user interface, text, application, email Description automatically generated| image:: /static/katalogas/okot/image50.png
   :width: 5.3705in
   :height: 0.67424in
.. |Graphical user interface, text, application, email Description automatically generated| image:: /static/katalogas/okot/image50.png
   :width: 5.3693in
   :height: 0.56061in
.. |Graphical user interface, text, application, email Description automatically generated| image:: /static/katalogas/okot/image50.png
   :width: 5.36725in
   :height: 1.63681in
.. |Graphical user interface, text, application Description automatically generated| image:: /static/katalogas/okot/image52.png
   :width: 4.62879in
   :height: 1.54917in
.. |Graphical user interface, text, application Description automatically generated| image:: /static/katalogas/okot/image53.png
   :width: 6in
   :height: 1.99191in
.. |Graphical user interface, text, application, email Description automatically generated| image:: /static/katalogas/okot/image54.png
   :width: 4.02177in
   :height: 2.70455in
.. |Graphical user interface, text, application, email, Teams Description automatically generated| image:: /static/katalogas/okot/image55.png
   :width: 6in
   :height: 2.81793in
.. |Graphical user interface, text, application Description automatically generated| image:: /static/katalogas/okot/image56.png
   :width: 6in
   :height: 1.61616in
.. |Graphical user interface, text, application, chat or text message Description automatically generated| image:: /static/katalogas/okot/image57.png
   :width: 0.81884in
   :height: 0.5in
.. |image64| image:: /static/katalogas/okot/image58.png
   :width: 2.78823in
   :height: 1.90278in
.. |01| image:: /static/katalogas/okot/image59.png
   :width: 6in
   :height: 0.38317in
.. |Graphical user interface, text, application, chat or text message Description automatically generated| image:: /static/katalogas/okot/image60.png
   :width: 6.04463in
   :height: 0.80833in
.. |Screenshot (235)| image:: /static/katalogas/okot/image61.png
   :width: 6in
   :height: 2.3245in
.. |image68| image:: /static/katalogas/okot/image62.png
   :width: 6in
   :height: 1.82243in
.. |Graphical user interface, text, application Description automatically generated| image:: /static/katalogas/okot/image63.png
   :width: 6in
   :height: 0.86026in
.. |image70| image:: /static/katalogas/okot/image64.png
   :width: 2.34912in
   :height: 1.56436in
.. |image71| image:: /static/katalogas/okot/image65.png
   :width: 6.69375in
   :height: 0.72431in
.. |image72| image:: /static/katalogas/okot/image66.png
   :width: 6.69375in
   :height: 1.09306in
.. |image73| image:: /static/katalogas/okot/image67.png
   :width: 6.69375in
   :height: 0.60833in
.. |past01| image:: /static/katalogas/okot/image68.png
   :width: 4.95049in
   :height: 2.17358in
.. |image75| image:: /static/katalogas/okot/image69.png
   :width: 4.12376in
   :height: 0.62422in
.. |image76| image:: /static/katalogas/okot/image70.png
   :width: 0.16752in
   :height: 0.15in
.. |Graphical user interface, email Description automatically generated| image:: /static/katalogas/okot/image71.png
   :width: 6.19491in
   :height: 2.84583in
.. |image78| image:: /static/katalogas/okot/image72.png
   :width: 0.11389in
   :height: 0.16667in
.. |image79| image:: /static/katalogas/okot/image73.png
   :width: 6.68958in
   :height: 1in
.. |image80| image:: /static/katalogas/okot/image74.png
   :width: 3.03333in
   :height: 1.25369in
.. |image81| image:: /static/katalogas/okot/image75.png
   :width: 6.68194in
   :height: 1.98261in
.. |image82| image:: /static/katalogas/okot/image76.png
   :width: 2.04514in
   :height: 0.65139in
.. |image83| image:: /static/katalogas/okot/image77.png
   :width: 6.46944in
   :height: 2.79514in
.. |image84| image:: /static/katalogas/okot/image78.png
   :width: 5.47059in
   :height: 2.76908in
.. |image85| image:: /static/katalogas/okot/image79.png
   :width: 3.13225in
   :height: 0.69565in
.. |image86| image:: /static/katalogas/okot/image80.png
   :width: 6.19722in
   :height: 2.82569in
.. |image87| image:: /static/katalogas/okot/image81.png
   :width: 6.69351in
   :height: 0.64171in
.. |sn41| image:: /static/katalogas/okot/image82.png
   :width: 0.85417in
   :height: 0.4375in
.. |image89| image:: /static/katalogas/okot/image83.png
   :width: 2.92361in
   :height: 3.16784in
.. |image90| image:: /static/katalogas/okot/image84.png
   :width: 6.30208in
   :height: 0.90625in
.. |image91| image:: /static/katalogas/okot/image85.png
   :width: 2.82386in
   :height: 2.18603in
.. |image92| image:: /static/katalogas/okot/image86.png
   :width: 0.16667in
   :height: 0.14583in
.. |image93| image:: /static/katalogas/okot/image87.png
   :width: 0.14495in
   :height: 0.15in
.. |image94| image:: /static/katalogas/okot/image86.png
   :width: 0.16667in
   :height: 0.14583in
.. |image95| image:: /static/katalogas/okot/image87.png
   :width: 0.14495in
   :height: 0.15in
.. |image96| image:: /static/katalogas/okot/image88.png
   :width: 3.85208in
   :height: 2.00792in
.. |image97| image:: /static/katalogas/okot/image89.png
   :width: 6in
   :height: 0.57944in
.. |image98| image:: /static/katalogas/okot/image85.png
   :width: 2.55952in
   :height: 1.98694in
.. |image99| image:: /static/katalogas/okot/image90.png
   :width: 6.29514in
   :height: 3.02041in
.. |image100| image:: /static/katalogas/okot/image91.png
   :width: 0.12984in
   :height: 0.15in
.. |Graphical user interface, text, application Description automatically generated| image:: /static/katalogas/okot/image92.png
   :width: 0.79167in
   :height: 0.66076in
.. |Graphical user interface, text, application Description automatically generated| image:: /static/katalogas/okot/image93.png
   :width: 1.27822in
   :height: 1.97396in
