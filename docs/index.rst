.. manifest documentation master file, created by
   sphinx-quickstart on Sun Jul  7 15:44:01 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. default-role:: literal

Atvirų duomenų manifestas
#########################

Atvirų duomenų manifestas yra visų Lietuvos duomenų rodyklė. Kitais žodžiais
tai yra metaduomenys (duomenys apie duomenis). 

Pavyzdžiui, jei visi Lietuvos duomenys būtų sukrauti į didelę spintą ir
didžioji dalis spintos turinio būtų skolinta iš kitų spintų, tai atvirų duomenų
manifestas būtų lapelis užkabintas ant spintos durų, kuriame surašyta kas, kur,
kada, iš ko pasiskolino, kada grąžinti ir pan.

Metaduomenys leidžia automatizuoti duomenų valdymą įdarbinant robotus, kurie
automatizuotų didelę dalį veiklų susijusių su duomenų valdymu.

.. image:: static/spinta.png

Į šio projekto apimtį įeina ne tik informacija kaip aprašyti metaduomenis, bet
teikiami įrankiai, kurie metaduomenų pagrindu automatizuoja daugelį duomenų
atvėrimo ir pateikimo naudojimui veiklų.

Manifesto (lapelis ant spintos) sudarymo procesas vadinamas duomenų
`inventorizacija <inventorying>`_. Tarkime, kaip pavyzdį, galime panagrinėti
išgalvotos įstaigos „Duomenų centras“ sutrumpintai vadinamos DC duomenis. DC
duomenų bazėje yra lentelė techniniu pavadinimu `COUNTRIES`, lentelės
turinys atrodo taip:

=======  ========  ===========
COUNTRIES
------------------------------
id       code      country
=======  ========  ===========
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ===========

Įstaiga „Duomenų centras“ nori atverti duomenis. Pirmas žingsnis būtų duomenų
inventorizacija. Duomenų inventorizacijos metu sudaromi įstaigoje esančių
duomenų laukų sąrašai, kurie atrodo taip:

================  ============  ========  =====  ===============  ==========
Atvirų duomenų manifestas                        Duomenų centro duomenų bazė
-----------------------------------------------  ---------------------------
dataset           model         property  title  table            column
================  ============  ========  =====  ===============  ==========
gov/dc/countries  COUNTRIES     _id       \      COUNTRIES        id     
gov/dc/countries  COUNTRIES     code      \      COUNTRIES        code   
gov/dc/countries  COUNTRIES     country   \      COUNTRIES        country
================  ============  ========  =====  ===============  ==========

Reali inventorizacijos lentelė yra kiek sudėtingesnė, šiame pavyzdyje yra
mažiau stulpelių dėl paprastumo.

Tokią pirminę inventorizacijos lentelę daugeliu atveju galima sugeneruoti
automatiškai iš duomenų šaltinio.

Deja ne viską galima automatizuoti, toliau prasideda rankinis darbas su
lentele:

- pažymimi laukai, kurie neturi būti atverti

- pateikiami laukų pavadinimai ir aprašymai, kad būtų aišku kaip juos naudoti

- pažymima, kuriuose laukuose pateikta asmeninė informacija

- verčiami lentelių ir laukų pavadinimai, į vieningą manifesto žodyną

Galiausiai gauname lentelę, kuri atrodo taip:

================  =======       ========  =====  ============  =======
dataset           model         property  title  table         column
================  =======       ========  =====  ============  =======
gov/dc/countries  country       _id       ID     COUNTRIES     id     
gov/dc/countries  country       code      Kodas  COUNTRIES     code   
gov/dc/countries  country       name      Šalis  COUNTRIES     country
================  =======       ========  =====  ============  =======

Manifestas
----------

Inventorizacijos lentelė yra tik patogesnė priemonė metaduomenų valdymui.
Tačiau, pagrindinis metaduomenų formatas yra manifesto YAML failai.

Darbas su inventorizacijos lentele yra patogus ir paprastas, tačiau deja kai
kurios sudėtingesnės automatizavimo veiklos reikalauja žymiai daugiau
metaduomenų. O turėti didelį kiekį metaduomenų vienoje lentelėje yra tiesiog
nepraktiška.  Todėl paprasti dalykai ir pirminė inventorizacija daroma
lentelėse, sudėtingesni dalykai ir pilnas duomenų aprašas yra YAML failuose.

Visi įrankiai dirba su YAML failais. YAML failus galima nuskaityti mašininiu
būdu, tačiau YAML sintaksė yra lengvai suprantama ir žmonėms. Štai kaip
atrodytų mūsų inventorizacijos lentelė YAML formatu:

.. code-block:: yaml

   type: dataset
   name: gov/dc/countries
   resources:
     countries:
       type: sql
       source: postgresql://user:password@host/dbname
       objects:
         country:
           source: COUNTRIES
           properties:
             _id:
               type: pk
               source: id
             code:
               type: string
               source: code
             name:
               type: string
               source: country

Tokie duomenų aprašai leidžia pateikti daug daugiau informacijos apie duomenų
šaltinį, tačiau failo formatas yra kiek sudėtingesnis, nei inventorizacijos
lentelės. Todėl pirminė inventorizacija atliekama lentelės pagalba, o
išplėstinė, YAML failų pagalba.

Tarpinė duomenų saugykla
------------------------

Pasidarius tokią inventorizaciją, automatinėmis priemonėmis, duomenys
kopijuojami iš pirminio duomenų šaltinio į tarpinę duomenų saugyklą. Tarpinė
duomenų saugykla nėra prieinama iš išorės ir turėtų veikti įstaigos
atveriančios duomenis infrastruktūroje.

Tarpinėje duomenų saugykloje atliekami visi nuasmeninimo, transformacijos,
vertimo į manifesto žodyną ir kiti darbai. Kad neatskleisti jautrios
informacijos, visi šie darbai turi būti atliekami tarpinėje saugykloje, kad
duomenys, kol dar nėra iki galo paruošti, nepaliktų įstaigos infrastruktūros
ribų.

Galiausiai ištestuoti ir patvirtinti atvėrimui duomenų rinkiniai keliauja į
viešąją duomenų saugyklą, kuri yra pasiekiama adresu https://atviriduomenys.lt.

Viešoji duomenų saugykla leidžia duomenis atsisiųsti įvairiais formatais,
suteikia vieningą API duomenų integracijai ir suteikia įvairias priemones
darbui su duomenimis. Duomenų naudotojai gali rašyti užklausas, jungti duomenis
tarpusavyje, sekti pasikeitimus duomenyse, matyti kokios klaidos įvyko
apdorojant duomenis ir pan.

Tiek vidinėje saugykloje, tiek viešojoje saugykloje, pagrindinis integracijos
taškas yra manifesto YAML failai. Atvėrus duomenis iš tarpinės duomenų
saugyklos, vidiniai YAML failai transformuojami į viešai prieigai tinkantį
pavidalą, kur yra paslėpti vidinių duomenų bazių pavadinimai, transformacijų
aprašai ir pan. Šis viešasis manifesto variantas skelbiamas
`atviriduomenys/manifest`_ kodo repozitorijoje.

.. _atviriduomenys/manifest: https://gitlab.com/atviriduomenys/manifest

Duomenų naudotojai, pastebėję klaidas, gali užregistruoti pranešimą `užduočių
valdymo sistemoje`__. Užduočių valdymo sistema yra atvira ir integruota su kodo
repozitorija. Viešoji manifesto dalis yra atviro kodo, todėl visi gali
įsitraukti ir tiksliai matyti kas vyksta.

.. __: https://gitlab.com/atviriduomenys/manifest/issues

Paskutinis žingsnis - suformuotas duomenų rinkinys užregistruojamas atvirų
duomenų vitrinoje adresu https://data.gov.lt, kad duomenų naudotojai galėtų
rasti duomenis.


Turinys
=======

.. toctree::
   :maxdepth: 2

   inventorying
   sources
   pk
   norm
   dependencies
   vocabulary
   api
   glossary
   contributing
