.. default-role:: literal

.. _atverimas:

Duomenų atvėrimo procesas
#########################

Labai apibendrintai, kiekviena įstaiga atverianti duomenis turi atlikti šiuos
žingsnius:

1. Paskirti atvirų duomenų koordinatorių ir `užsiregistruoti portale`__.

   __ https://data.gov.lt/opening/learningmaterial/10

2. Sudaryti savo valdomų :term:`duomenų rinkinių <duomenų rinkinys>` sąrašą
   (preliminari inventorizacija).

3. Parengti atveriamų :ref:`duomenų struktūros aprašus <dsa>` (detali
   inventorizacija).

4. Atverti duomenis savarankiškai, su rangovo arba Vyriausybės įgaliotos
   institucijos (Statistikos departamento) pagalba.

Visas duomenų atvėrimo procesas, kiek įmanoma yra automatizuotas, todėl
duomenis atveriančiai įstaigai tenka labai nedidelė dalis darbo.

Toliau aptarsime kiekvieną žingsnį detaliau.


Koordinatoriaus registracija
============================

Kiekviena duomenis atverianti įstaiga turi paskirti vieną žmogų atsakingą už
duomenų atvėrimo koordinavimą.

Koordinatoriaus paskyrimas įteisinamas į atvirų duomenų portalą pateikianti
įstaigos vadovo pasirašytą `raštą`__.

__ https://data.gov.lt/opening/learningmaterial/10

Turinti įstaigos vadovo pasirašytą raštą, paskirtasis koordinatorius
`registruojasi atvirų duomenų portale`__.

__ https://data.gov.lt/

.. image:: static/koordinatoriaus-registracija.png
    :target: https://data.gov.lt/


.. _inventory:

Inventorizacija
===============

Inventorizacija yra procesas kurio metu surašomas turimas turtas. Duomenų
atveju, surašomi turimi duomenų šaltiniai. Inventorizaciją reikia
atlikti tam, kad geriau suprasti kokius duomenis įstaiga turi ir atrinkti
kuriuos duomenis galima atverti.

Duomenų inventorizacija susideda iš dviejų dalių:

- Duomenų rinkinių sąrašo sudarymas (preliminari inventorizacija)

- Duomenų struktūros aprašo parengimas (detali inventorizacija)

Pati sudėtingiausia dalis yra duomenų struktūros aprašo parengimas. Todėl
rekomenduojama pirmiausia susidaryti rinkinių sąrašą ir jį publikuoti
:term:`atvirų duomenų portale <ADK>`, o po to, pereiti prie duomenų struktūros
aprašų, prioritetą teikiant duomenų rinkiniams, kurie turi paklausą.


Rinkinių sąrašas
----------------

Preliminarios inventorizacijos metu, įstaigos paskirtas koordinatorius
peržvelgia įstaigos veiklos nuostatus, valdomas informacines sistema,
registrus ir sudaro įstaigos valdomų :term:`duomenų rinkinių <duomenų
rinkinys>` sąrašą.

Atkreipkite dėmesį, kad toks sąrašas sudaromas ir publikuojamas atvirų
duomenų portale dar prieš atveriant duomenis. Toks sąrašas padės
potencialiems atvirų duomenų naudotojams geriau suprasti, kokie duomenys yra.

Jei įstaiga jau yra atvėrusi duomenis ir juos publikuoja, tuomet, nuorodas į
atvertus duomenis taip pat pateikia :term:`atvirų duomenų portale <ADK>`.

.. image:: static/rinkinio-forma.png
    :target: https://data.gov.lt/admin/dataset/new

Sudarant duomenų rinkinių sąrašus, apie kiekvieną duomenų rinkinį reikia
pateikti tokius metaduomenis:

- pavadinimą
- aprašymą
- kategoriją
- raktinius žodžius
- kontaktinį asmenį

Šie duomenys padės potencialiems duomenų naudotojams surasti duomenis ir
išreikšti norą gauti šiuos duomenis, jei jie dar nėra atverti.

Duomenų rinkinių sąrašus galima sudaryti :term:`atvirų duomenų portale <ADK>`
arba galima parengti `rinkinių sąrašo lentelę`__ ir ją vėliau importuoti į
:term:`portalą <ADK>`.

__ https://data.gov.lt/opening/learningmaterial/14


Duomenų struktūros aprašas
--------------------------

Detali inventorizacija yra sudėtingesnė ir reikalauja daugiau laiko ir bazinių
žinių apie `duomenų modeliavimą`__. Todėl šią dalį reikėtų atlikti
pasitelkiant duomenų administratoriaus pagalbą. Detali inventorizacija
atliekama parengiant :term:`duomenų struktūros aprašą (DSA) <DSA>`. Duomenų
struktūros aprašo rengimas bus efektyvesnis dalyvaujant žmonėms, kurie buvo
atsakingi kuriant duomenų bazės modelį.

.. __: https://en.wikipedia.org/wiki/Data_modeling

Daugeliu atveju pirminį :term:`DSA` lentelės variantą galima :ref:`generuoti
automatiškai <šdsa-generavimas>` iš duomenų šaltinio, o vėliau papildyti tai ko
trūksta. Pirminio :term:`DSA` generavimu turėtu pasirūpinti duomenų bazių
administratorius, prižiūrintis informacines sistemas ar IT ūkį.

Vykdant duomenų atvėrimą, pirmiausia rengiamas :term:`šaltinio duomenų
struktūros aprašas (ŠDSA) <ŠDSA>`, kuriame yra pateikta visa duomenų šaltinio
struktūros išklotinė, vėliau sužymėjus kuriuos duomenų laukus galima atverti
:term:`ŠDSA` yra :ref:`konvertuojamas <šdsa-vertimas-į-adsa>` į :term:`ADSA`.

:term:`ADSA` dalis publikuojama :term:`atvirų duomenų portale <ADK>`, o
:term:`ŠDSA` naudojama automatizuotam duomenų atvėrimui ir publikavimui.

:term:`DSA` galima aprašyti duomenis saugomus įvairiuose duomenų šaltiniuose,
plačiau apie tai galima pasiskaityti skyriuje :ref:`duomenų-šaltiniai`, tačiau
kaip pavyzdį galime panagrinėti išgalvotą duomenų šaltinį, kuriame yra viena
lentelė:

====  ========  =======  ===============
ŠALIS
----------------------------------------
ID    KODAS     ŽEMYNAS  ŠALIS
====  ========  =======  ===============
1     lt        eu       Lietuva
2     lv        eu       Latvija
3     ee        eu       Estija
====  ========  =======  ===============

Šaltinio duomenų struktūros aprašas (ŠDSA), tariamas kaip „šadsa“. Tai yra
:term:`DSA` variantas, neskirtas viešinimui, aprašantis vidinių duomenų bazių
ar kitų vidinių šaltinių duomenų struktūras. ŠDSA leidžia geriau suprasti
turimus duomenis, tuos duomenis suskirstyti į duomenų rinkinius ir pažymėti,
kurie duomenys gali būti atverti, pakartotinai panaudoti ar skirti tik
vidiniam naudojimui.

Dažniausiai duomenų bazių valdymo sistemos jau turi pakankamai metaduomenų, kad
iš jų būtų galima :ref:`automatiškai generuoti <šdsa-generavimas>` pirminį
:term:`ŠDSA` lentelės variantą, kuris šiuo atveju atrodys taip:

.. table:: Pirminis šaltinio duomenų struktūros aprašas (:term:`ŠDSA`)

    +----+---+---+---+---+----------+---------+-------+------------+---------+-------+--------+-----+-------+-------------+
    | id | d | r | b | m | property | type    | ref   | source     | prepare | level | access | uri | title | description |
    +====+===+===+===+===+==========+=========+=======+============+=========+=======+========+=====+=======+=============+
    |    | datasets/gov/example     |         |       |            |         |       |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+------------+---------+-------+--------+-----+-------+-------------+
    |    |   | salys                | sql     |       | \sqlite:// |         |       |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+------------+---------+-------+--------+-----+-------+-------------+
    |    |   |   |   | Salis        |         | id    | ŠALIS      |         |       |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+------------+---------+-------+--------+-----+-------+-------------+
    |    |   |   |   |   | id       | integer |       | ID         |         | 4     |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+------------+---------+-------+--------+-----+-------+-------------+
    |    |   |   |   |   | kodas    | string  |       | KODAS      |         | 2     |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+------------+---------+-------+--------+-----+-------+-------------+
    |    |   |   |   |   | zemynas  | string  |       | ŽEMYNAS    |         | 2     |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+------------+---------+-------+--------+-----+-------+-------------+
    |    |   |   |   |   | salis    | string  |       | ŠALIS      |         | 2     |        |     |       |             |
    +----+---+---+---+---+----------+---------+-------+------------+---------+-------+--------+-----+-------+-------------+

Tokia automatiškai generuota :term:`DSA` lentelė vadinama pirmine :term:`ŠDSA`
lentele, kadangi ji yra generuota automatiškai ir neredaguota.

Keičiantis pirminio duomenų šaltinio struktūrai :term:`ŠDSA` galima automatiškai
atnaujinti, papildant naujai atsiradusiais duomenų laukais.

Deja, automatinėmis priemonėmis galima nuspėti tik dalį metaduomenų reikšmių.
Tai kas neįveikiama automatinėms priemonėms, pildoma rankiniu būdu:

- Suteikti :ref:`duomenų rinkinio <dataset>` struktūrai :ref:`kodinį
  pavadinimą <kodiniai-pavadinimai>`, kurio pagrindu duomenys bus publikuojami
  per :term:`API`.

- Užpildyti :data:`access` stulpelį, nurodant duomenų :ref:`prieigos lygį
  <access>`.

- Užpildyti :data:`prepare` stulpelį, jei duomenų lentelės atveriamos ne
  pilna apimtimi ir reikia jas :ref:`filtruoti <duomenų-atranka>`.

- :ref:`Sužymėti <pii>` duomenų laukus, kuriuose yra pateikiami asmenį
  identifikuojantys duomenys ir pažymėti duomenų laukus, kuriuos reikia
  :ref:`nuasmeninti <nuasmeninimas>`.

Baigus aukščiau išvardintus lentelės papildymo darbus, :term:`ŠDSA` lentelė
turėtu atrodyti taip:

.. table:: Darbinis šaltinio duomenų struktūros aprašas (:term:`ŠDSA`)

    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    | id | d | r | b | m | property   | type    | ref   | source     | prepare        | level | access  | uri | title | description |
    +====+===+===+===+===+============+=========+=======+============+================+=======+=========+=====+=======+=============+
    |    | datasets/example/countries |         |       |            |                |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   | salys                  | sql     |       | \sqlite:// |                |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   |   |   | Country        |         | id    | SALIS      | continent="eu" |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   |   |   |   | id         | integer |       | ID         |                | 4     | private |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   |   |   |   | code       | string  |       | KODAS      |                | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   |   |   |   | continent  | string  |       | ŽEMYNAS    |                | 2     | private |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+
    |    |   |   |   |   | name       | string  |       | SALIS      |                | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+------------+----------------+-------+---------+-----+-------+-------------+

Šioje lentelėje buvo atlikti tokie pataisymai:

- Pirmoje eilutėje, :data:`dataset` stulpelyje nurodytas duomenų rinkinio
  kodinis pavadinimas,

- Užpildytas :data:`access` stulpelis.

- :data:`model.prepare` stulpelyje pateiktas filtras `continent="eu"`,
  nurodantis, kad atveriamos tik Europos šalys.

- Pakeisti :data:`model` ir :data:`property` kodiniai pavadinimai.

Galiausiai, toks duomenų struktūros aprašas gali būti naudojamas
automatizuotam duomenų atvėrimui ir publikavimui.

O į :term:`atvirų duomenų portalą <ADK>` pateikiamas ADSA variantas, kuris
konvertuojamas iš ŠDSA automatinėmis priemonėmis. ADSA, kurį reikia įkelti į
portalą atrodys taip:

.. table:: Planuojamų atverti duomenų struktūros aprašas (:term:`ADSA`)

    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+---------+-----+-------+-------------+
    | id | d | r | b | m | property   | type    | ref   | source | prepare | level | access  | uri | title | description |
    +====+===+===+===+===+============+=========+=======+========+=========+=======+=========+=====+=======+=============+
    |    | datasets/example/countries |         |       |        |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+---------+-----+-------+-------------+
    |    |   | salys                  |         |       |        |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+---------+-----+-------+-------------+
    |    |   |   |   | Country        |         |       |        |         |       |         |     |       |             |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+---------+-----+-------+-------------+
    |    |   |   |   |   | code       | string  |       |        |         | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+---------+-----+-------+-------------+
    |    |   |   |   |   | name       | string  |       |        |         | 2     | open    |     |       |             |
    +----+---+---+---+---+------------+---------+-------+--------+---------+-------+---------+-----+-------+-------------+

:term:`ADSA` lentelėje buvo padaryti tokie pakeitimai:

- Pašalinti pirminio duomenų šaltinio metaduomenys iš :data:`source` stulpelio.

- Pašalintos visos eilutės, kurio :data:`access` nėra `public` arba `open`.


Duomenų atvėrimas
=================

Kiekviena įstaiga renkasi vieną iš šių duomenų atvėrimo variantų:

- Atveria savarankiškai, jei turi vidinius IT resursus.
- Atveria su rangovo pagalba, jei neturi vidinių IT resursų.
- Atveria su Vyriausybės įgaliotos institucijos (Statistikos departamento)
  pagalba, jei neturi nei vidinių IT resursų, nei išorinio rangovo.


Savarankiškas atvėrimas
-----------------------

Atveriant duomenis savarankiškai įstaiga turi tokius variantus:

- Duomenis atveria naudojantis IVPK pateiktomis priemonėmis, kurios leidžia
  automatizuoti duomenų atvėrimą.

- Duomenis atveria naudojant savo priemones, tačiau atvertus duomenis
  publikuoja per :ref:`API <saugykla>` į :term:`atvirų duomenų saugyklą <ADS>`.

- Duomenis jau yra atvėrusi arba duomenis atveria savo priemonėmis ir
  publikuoja savo infrastruktūroje.

Nepriklausomai nuo pasirinkto varianto, įstaiga turi pateikti atvertų duomenų
rinkinius, duomenų struktūros aprašus ir nuorodas į duomenis :term:`atvirų
duomenų portale <ADK>`.


Atvėrimas per rangovą
---------------------

Atvėrimas vyksta taip pat, kaip ir savarankiškai, tik naudojantis išorinio
rangovo paslaugomis.

Su rangovu sudarant sutarti, kaip sutarties priedas turi būti pateikiamas
duomenų struktūros aprašas, kuriame tiksliai nurodyta kokius duomenis reikia
atverti.


Atvėrimas per Statistikos departamentą
--------------------------------------

Jei duomenys atveriami per Statistikos departamentą, tuomet įstaiga su
Statistikos departamentu sudaro duomenų atvėrimo paslaugos teikimo sutartį,
prie kurios, kaip priedas pateikiamas duomenų struktūros aprašas.

Statistikos departamentas numatytu laiku pasidarys visų duomenų kopiją (prie
kurių įstaiga suteikia prieigą) Valstybės Duomenų Valdysenos Informacinėje
Sistemoje (VDVIS).

Vadovaujantis duomenų struktūros apraše pateikta informacija, naudojantis VDVIS
funkcionalumu, atliks visas reikalingas transformacijas ir publikuos duomenis
:term:`atvirų duomenų saugykloje <ADS>`.
