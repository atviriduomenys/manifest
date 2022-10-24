.. default-role:: literal


Atvirų duomenų struktūros aprašų katalogas
##########################################

Šiame repozitoriume rengiami ir saugomi Lietuvos atvirų duomenų struktūros
aprašai.

Duomenų struktūros aprašai rengiami vadovaujantis `Duomenų struktūros aprašo
specifikacija`__.

__ https://atviriduomenys.readthedocs.io/dsa/index.html


Vienas struktūros aprašas atitinka vieną duomenų rinkinį, `Lietuvos atvirų
duomenų kataloge`__. Struktūros aprašai saugomi CSV failuose, kurie
organizuojami kataloguose, kurie atitinka struktūros apraše nurodytą `vardų
erdvę`__.

__ https://data.gov.lt/datasets
__ https://atviriduomenys.readthedocs.io/dsa/formatas.html#vardu-erdves

Pilnai parengti struktūros aprašai publikuojami Kataloge.

Duomenų parengimo atvėrimui procesas
====================================

Dirbant prie duomenų atvėrimo, kiekvienam duomenų rinkiniui sukuriama po
atskirą `GitHub užduotį <issues_>`_, o užduotys valdomos vienoje iš šių lentų:

- `II duomenų atvėrimo etapas <board_>`_ - į šią lentą keliamos tik tie
  rinkiniai kurie atveriami II duomenų atvėrimo etapo projekto apimtyje.

- `Atvėrimas <board-atverimas_>`_ - į šią lentą keliami rinkiniai, kurie
  neįeina į II duomenų atvėrimo etapo projektą.

Kieviena užduotis yra siejama su `GitHub keitimais (Pull Request)
<issue-link-pr_>`_.

Visas atvėrimo procesas vykdomas perkeliant užduotis projekto lentoje iš vieno
stulpelio į kitą, tokia tvarka:

1.  **Suplanuota** - prieš pradedant dirbti prie duomenų rinkinio atvėrimo,
    reikia sukurti `užduotį <issues_>`_ (jei ji dar nebuvo sukurta) ir įtraukti
    užduotį į projekto lentą, nurodyti statusą „Suplanuota“.

    Prie užduoties nurodoma organizacijos, kuriai priklauso rinkinys žymė. Ir
    atvėrimo būdas:

    - `centralizuotai`
    - `per paslaugos teikėją`
    - `savarankiškai`

    Užduoties aprašyme pateikiama nuoroda į duomenų rinkinį data.gov.lt
    svetainėje.

2.  **Daroma** - pradedant duomenų rinkinio atvėrimo darbus, užduotis projekto
    lentoje perkeliama į **Daroma** stulpelį ir žmogus, kuris dirba prie
    atvėrimo prisiskira save prie užduoties. Reikia pradėti nuo tokių užduočių,
    kurios nėra priklausomos nuo kitų užduočių (duomenų rinkiniai gali būti
    siejami ryšiais, ko pasekoje vienas rinkinys gali būti priklausomas nuo
    kito).

    Duomenų atvėrimo metu, prie užduoties reikia susikurti naują darbinę šaką
    (Development -> Create a branch).

    Susikurtoje šakoje įkeliamas atveriamo duomenų rinkinio struktūros aprašas
    CSV formatu. Struktūros aprašai turi būti įkeliami į katalogą, kuris
    sutampa su struktūros apraše nurodyta vardų erdve, o struktūros aprašo CSV
    failo pavadinias turi sutapti su paskutiniu vardų erdvės komponentu +
    `.csv` galūnė.

    Galiausiai sukuriamas `Pull Request <pulls_>`_. Pull Request veikia
    automatinis struktūros aprašo patikrinimas. Jei patikrinimo metu aptinkamos
    klaidos reikia jas pataisyti.

    Jei manote, kad klaida yra tikrinimo mechanizme, tada reikia apie tai
    `pranešti sukuriant užduotį Spinta projekto užduočių sąraše
    <spinta-issues_>`_, jei tokia užduotis dar nebuvo sukurta. Kol Spintos
    klaida nėra pataisyta, tuomet struktūros apraše, reikia `įrašyti komentarą
    <comments_>`_ `uri` stulpelyje pateikiant nuorodą į užduotį.

    Jei duomenų rinkinio duomenys bus publikuojami `Saugykloje <saugykla_>`_,
    tuomet, struktūros aprašo failas turi būti įtrauktas į `get_data_gov_lt.in`
    failą.

3.  **Tikrinama** - pilnai parengus struktūros aprašą, projekto lentoje
    užduotis perkeliama į **Tikrinama** stulpelį, kuriame atvirų duomenų
    komandos žmonės peržiūrės struktūros aprašą.

    Žmogus, kuris tikrina taip pat turėtu prisiskirti save prie užduoties.

    Jei patikrinimo metu, struktūros apraše randama klaidų, tuomet Pull Request
    surašomi komentarai apie rastas klaidas ir užduotis projektų lentoje
    grąžinama į „Daroma“.

    Jei klaidų nerasta, tada užduotis projektų lentoje perkeliama į
    „Patikrinta“.


4.  **Patikrinta** - kai užduotis patenka į „Patikrinta“, Pull Request autorius
    sulieja Pull Request į pagrindinę šaką (Merge).

    Jei duomenys publikuojami ne Saugykloje, tada užduotis po suliejimo
    perkeliama į „Paruošta“.

    Jei duomenys publikuojami Saugykloje, tada užduotis paliekama „Patikrinta“
    stulpelyje. Vieną kartą per savaitę, penktadieniais, visų užduočių esančių
    „Patikrinta“ stulpelyje struktūros apraštai publikuojami Saugykoje ir tai
    padarius, užduotis perkeliama į „Paruošta“.


4.  **Paruošta** - kei užduotis patenka į „Paruošta“, tai reiškia, kad galima
    pradėti duomenų publikavimą į Saugyklą ar kur nors kitur.

    Užduotis į „Atverta“ stulpelį perkeliama tada, kai:

    - duomenys yra pilnai atverti ir publikuoti Saugykloje ar kitoje vietoje,

    - duomenų rinkinys yra sukurtas data.gov.lt svetainėje ir nuoroda į rinkinį
      yra pateikta užduoties aprašyme,

    - data.gov.lt svetainėje yra atnaujinta šaltinio nuoroda į vietą, kurioje
      publikuojami duomenys.

5.  **Atverta** - šiame stulpelyje patenka užduotys, kai duomenų atvėrimas yra
    pilnai baigtas.
    
    Po atvėrimo prie užduoties reikia pažymėti iteraciją, kada užduotis buvo
    atverta. Pati užduotis turi būti uždaryta.

    Socialiniuose tinkluose apie duomenų atvėrimą galima skelbti tik tuomet,
    kai yra pabaigti visi su atvėrimu susiję žingsniai išvardinti aukščiau.

    Jei atvėris patebimos klaidos, užduotis gali būti vėl grąžinama į „Daroma“.
    Tačiau iteracija, kurioje buvo užfiksuotas atvėrimas paliekama pirmo
    atvėrimo metu, o ne paskutinio pataisymo metu.


.. _board: https://github.com/orgs/atviriduomenys/projects/2/views/1
.. _issues: https://github.com/atviriduomenys/manifest/issues
.. _gh-pr: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
.. _issue-link-pr: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue
.. _pulls: https://github.com/atviriduomenys/manifest/pulls
.. _spinta-issues: https://github.com/atviriduomenys/spinta/issues/
.. _comments: https://atviriduomenys.readthedocs.io/dsa/dimensijos.html#komentavimas
.. _saugykla: https://get.data.gov.lt/
.. _board-atverimas: https://github.com/orgs/atviriduomenys/projects/4/views/1
