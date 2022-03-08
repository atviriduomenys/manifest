.. default-role:: literal


Atvirų duomenų struktūros aprašų katalogas
##########################################

Šiame repozitoriume rengiami ir saugomi Lietuvos atvirų duomenų struktūros
aprašai.

Duomenų struktūros aprašai rengiami vadovaujantis `Duomenų struktūros aprašo
specifikacija <spec>`_.


Vienas struktūros aprašas atitinka vieną duomenų rinkinį, `Lietuvos atvirų
duomenų kataloge <adk>`_. Struktūros aprašai saugomi CSV failuose, kurie
organizuojami kataloguose, kurie atitinka struktūros apraše nurodytą `vardų
erdvę <ns>`_.

Pilnai parengti struktūros aprašai publikuojami `Kataloge <adk>`_.

Duomenų parengimo atvėrimui procesas
====================================

Dirbant prie duomenų atverimo, kiekvienam duomenų rinkiniui sukuriama po
atskirą `GitHub užduotį <issues>`_, o užduotys valdomos `GitHub projekto
lentoje <board>`.


1.  Pradedant dirbti prie duomenų rinkinio atvėrimo, atsakingas asmuo susikuria
    `užduotį <issues>`_ ir prisiskiria užduotį sau.

    Prie užduoties nurodoma organizacijos, kuriai priklauso rinkinys žymė.

2.  Kai pradedamas rengti duomenų rinkinio štaltinio struktūros aprašas (ŠDSA),
    tuoment užduotis perkeliama į ŠDSA būseną.

3.  Kai jau yra parengtas ŠDSA, tuomet sukuriamas naujas `GitHub pull request
    <gh-pr>`_, kurio šakoje įkeliamas ŠDSA pargrindu parengtas ADSA CSV failas.

    ADSA CSV failai įkeliami į katalogą, kuris atitinka struktūros apraše
    nurodytą vardų erdvę.

    Jei duomenis norima publikuoti get.data.gov.lt Saugykloje, tuomet
    `get_data.gov.lt.in` faile pateikiamas kelias iki rinkinio CSV failo, o
    užduotis pažymima žyme `saugykla`.

    Pull request susiejamas su duomenų rinkinio užduotimi. O užduočiai
    suteikiamas ADSA statusas.

4.  Peržiūrėjus ADSA Pull request, jei yra klaidų, užduotis grąžinama į ŠDSA
    būsiną. Apie pastebėtas klaidas informauojama Pull request komentaruose.

    Jei klaidų nėra tuoment, jei duomenys pageidaujama publikuoti
    get.data.gov.lt, tuoment struktūra įtraukiaia į get.data.gov.lt serverį.

    Galiausiai užduotis perkeliama į „Atvėrimas“ būseną.

5.  Kai duomenų atv€rimas pilnai baigtas, tuomet užduočiai suteikiama būsena
    „Atverta“.


.. _board: https://github.com/orgs/atviriduomenys/projects/2/views/1
.. _issues: https://github.com/atviriduomenys/manifest/issues
.. _spec: https://atviriduomenys.readthedocs.io/dsa/index.html
.. _adk: https://data.gov.lt/datasets
.. _ns: https://atviriduomenys.readthedocs.io/dsa/formatas.html#vardu-erdves
.. _gh-pr: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
