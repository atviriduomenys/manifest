.. default-role:: literal

.. _asmens-duomenys:


Asmens duomenys
###############

.. _nuasmeninimas:

Nuasmeninimas
=============

Duomenų laukų reikšmių nuasmeninimas atliekamas :data:`property.prepare`
stulpelio pagalba.

.. function:: randomize(model, n)

    Reikšmės keičiamos parenkant atsitiktinę vertę ±\ `n` intervale nuo
    tikrosios vertės.

.. function:: permutate(model)

    Atsitiktine tvarka sumaišomos duomenų reikšmės.

.. function:: hash(model)

    Taikyti numatytą maišos funkciją.

.. function:: hash(model, name)

    Taikyti konkrečią `name` maišos funkciją.

.. function:: sample(model, n)

    Atsitiktine tvarka atrenkama `n` procentų žodžių naudojamų tekste.

.. function:: group(model, n)

    Pakeičia originalias reikšmes į intervalų grupes taip, kad į vieną intervalą
    patektų ne mažiau nei `n` reikšmių. Jei viena konkreti reikšmė pasikartoja
    daugiau nei `n` kartų, tada intervalas nekuriamas, reikšmė paliekama tokia
    kokia yra šaltinyje.


.. _pii:

Asmenį identifikuojantys duomenys
=================================

Asmenį identifikuojančios savybės turi būti pažymėtos :data:`property.ref`
stulpelyje. Rekomenduojame naudoti tokius reikšmes, kadangi jos gali būti
naudojamos nuasmeninimo procese:

+--------+--------+--------------------------------+---------------------------+
| type   | ref    | uri                            | title                     |
+========+========+================================+===========================+
| prefix | person | \https://www.w3.org/ns/person# |                           |
+--------+--------+--------------------------------+---------------------------+
|        | pii    | \https://data.gov.lt/pii/      |                           |
+--------+--------+--------------------------------+---------------------------+
| model  |        | person:Person                  | Fizinio asmuo             |
+--------+--------+--------------------------------+---------------------------+
| string |        | person:patronymicName          | Tėvavardis                |
+--------+--------+--------------------------------+---------------------------+
| string |        | person:birthName               | Pilnas vardas             |
+--------+--------+--------------------------------+---------------------------+
| string |        | person:placeOfBirth            | Vieta kurioje gimė        |
+--------+--------+--------------------------------+---------------------------+
| string |        | person:placeOfDeath            | Vieta kurioje mirė        |
+--------+--------+--------------------------------+---------------------------+
| string |        | person:countryOfBirth          | Šalis kurioje gimė        |
+--------+--------+--------------------------------+---------------------------+
| string |        | person:countryOfDeath          | Šalis kurioje mirė        |
+--------+--------+--------------------------------+---------------------------+
| string |        | person:citizenship             | Tautybė                   |
+--------+--------+--------------------------------+---------------------------+
| string |        | person:residency               | Vieta kurioje gyvena      |
+--------+--------+--------------------------------+---------------------------+
| string |        | pii:name                       | Vardas ir/arba pavardė    |
+--------+--------+--------------------------------+---------------------------+
| date   |        | pii:dob                        | Gimimo data               |
+--------+--------+--------------------------------+---------------------------+
| string |        | pii:phone                      | Telefono numeris          |
+--------+--------+--------------------------------+---------------------------+
| string |        | pii:email                      | El. pašto adresas         |
+--------+--------+--------------------------------+---------------------------+
| string |        | pii:id                         | Asmens kodas              |
+--------+--------+--------------------------------+---------------------------+
| string |        | pii:address                    | Asmens adresas            |
+--------+--------+--------------------------------+---------------------------+
| string |        | pii:age                        | Amžius                    |
+--------+--------+--------------------------------+---------------------------+


Viešieji asmenys duomenys
=========================

Jokie asmens duomenys negali būti teikiami, kaip atviri duomenys, tačiau gali
būti teikiami pakartotiniam naudojimui laikantis :term:`BDAR` ir :term:`kitų
duomenų valdymo <duomenų valdymo aktas>` reikalavimų.

Siekiant užtikrinti viešąjį interesą, tam tikri viešųjų asmenų duomenys gali
būti teikiami pakartotiniam naudojimui, tačiau ribojant duomenų naudojimo tikslą
ir laikantis visų reikalavimų taikomų asmens duomenims.

Šiame skyriuje aptariama, kaip gali būti teikiami viešųjų asmenų duomenys.


Asmens duomenų identifikavimas
------------------------------

:term:`DSA` lentelėje, duomenys kuriuos galima viešinti, tačiau jų naudojimui
taikomi papildomi apribojimai, :data:`access` stulpelyje turi būti pažymėti
`public` reikšme (toliau vadinami `public` duomenimis).

Viename :term:`modelyje <modelis>` negali būti sumaišyti asmens ir kiti
duomenys. Pavyzdžiui jei vienoje lentelėje galima rasti tiek fizinių, tiek
juridinių asmenų duomenis, tada, fizinių ir juridinių asmenų duomenys turi
būti išskaidyti į atskirus duomenų :term:`modelius <modelis>`, iš kurių
vienas gali būti teikiamas, kaip atviri duomenys, o kitas su `public`
prieigos teis.

`public`  žyme galima žymėti viešus asmenis, kurių duomenų viešinimas yra
būtinas siekiant užtikrinti viešąjį interesą. Privačių asmenų ar kiti
konfidencialūs duomenys turi būti žymimi griežtesnėmis `protected` arba
`private` žymėmis.


Duomenų naudotojų autorizavimas
-------------------------------

`public` duomenys nėra teikiami, kaip atviri duomenys. Duomenų naudotojai,
pageidaujantys gauti `public` duomenis, privalo save identifikuoti. Tada
tokie duomenų naudotojai užregistruojami ir jiems išduodamas naudotojo
identifikavimo kodas ir slaptažodis.

Registruoti naudotojai gali kreiptis į duomenų saugyklą su prašymu išduoti
:ref:`autorizacijos raktą <autorizacija>`.

Duomenų naudotojai vykdydami užklausas duomenims gauti, `public` duomenų
atveju yra nukreipiami į savitarnos puslapį, kuriame gali susipažinti su
pageidaujamų duomenų naudojimo sąlygomis. Susipažinę su sąlygomis ir
patvirtinę, kad su sąlygomis sutinka, gauna prieigą prie duomenų.

Skirtingi `public` duomenų rinkiniai gali turėti skirtingas naudojimo
sąlygas, su kuriomis susipažinti ir su jomis sutikti reikia atskirai. Tačiau
visus `public` duomenis, su kurių naudojimo sąlygomis sutiko, duomenų
naudotojas gauna vienu ir tuo pačiu prieigos raktu.

Duomenų naudotojo registracija yra ilgalaikė, išduotas autorizacijos raktas
yra trumpalaikis, galiojantis kelias minutes ar kelias valandas. Duomenų
naudotojo sutikimai su sąlygomis yra ilgalaikiai, tačiau priklausomai nuo
duomenų rinkinio, gali būti terminuoti.


Duomenų naudotojų įsipareigojimai
---------------------------------

Duomenų naudotojas, gavęs prieigos raktą, įsipareigoja laikytis duomenų
naudojimo sąlygų ir įgyvendinti priemones asmens duomenų šalinimui iš savo
duomenų saugyklos. Duomenų šalinimui, duomenų naudotojas privalo teikti
sutartinį API prieigos tašką :ref:`aprašytą šiame vadove <saugykla>`. Privaloma
įgyvendinti tik :ref:`wipe` operaciją.

Jei keičiasi viešų asmens duomenų naudojimo reglamentavimas ar pats viešųjų
asmens duomenų subjektas atšaukia sutikimą naudoti savo duomenis arba baigiasi
terminas, kurio metu buvo galima naudoti duomenis arba duomenų naudotojas
nesilaiko duomenų naudojimo sąlygų, tada duomenų tiekėjas vykdo :ref:`wipe`
užklausą, duomenų naudotojo duomenų saugykloje, taip nurodant, kad duomenų
naudotojas privalo visiškai pašalini arba nuasmeninti nurodyto asmens subjekto
arba visus asmens duomenis.

Įvykdžius :ref:`wipe`, duomenų tiekėjas, kelis kartus tikrina ar duomenys tikrai
ištrinti vykdydamas :ref:`getone` užklausą.

Taip pat, duomenų tiekėjas gali vykdyti :ref:`getone` užklausą, jei viešų
asmens duomenų subjektas prašo eksportuoti visus savo duomenis.

Dėl minėtų priežasčių, duomenų naudotojas įsipareigojai įgyvendinti
:ref:`getone` ir :ref:`wipe` operacijas savo duomenų saugykloje ir suteikti
:ref:`prieigą <autorizacija>` prie savo saugyklos duomenų tiekėjui su
:ref:`getone` ir :ref:`wipe` teisėmis iš tiekėjo gautiems duomenims.

Jei duomenų naudotojas nesilaiko duomenų naudojimo taisyklių, tuomet duomenų
tiekėjas gali nutraukti asmens duomenų tiekimą ir papildomai vykdys eilę
:ref:`wipe` užklausų, kad pašalintu asmens duomenis duomenų naudotojo pusėje.

Duomenų naudotojas, naudojantis asmens duomenis, tampa asmens duomenų
valdytoju ir prisiima visą su tuo susijusią atsakomybę, įsipareigoja laikytis
visų :term:`BDAR` reikalavimų.


Subjektų savitarna
------------------

Asmens duomenų subjektams yra prieinama savitarnos sritis, kurioje subjektai
gali matyti kokie jų duomenys saugomi saugykloje, kam, kokiu pagrindu ir kokiu
tikslu duomenys teikiami, gali atšaukti sutikimą teikti duomenis, gali
eksportuoti visus savo duomenis.
