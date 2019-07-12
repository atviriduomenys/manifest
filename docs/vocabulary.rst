.. default-role:: literal

.. _vocab:

Žodynas
#######

Duomenų kontekste, žodynas yra tiesiog pavadinimų rinkinys, kuriais vadinami
objektai ir objektų savybės. Iš mūsų `countries.csv` pavyzdžio, duomenų
šaltinis naudoja vienokius laukų pavadinimus, tačiau importuojant duomenis
nurodome kitokius pavadinimus.

Aprašant duomenų struktūras nebūtina laikytis vieningo žodyno. Jei naudojami
pavadinimai yra ne iš žodyno, tada prieš pavadinima turi būti rašomas taško
simbolis (`.`). Po taško galima naudoti lygiai tokius pačius laukų pavadinimas
arba bet kokius kitus pavadinimus. Tačiau vieningas atvirų duomenų portale
naudojamas žodynas padeda geriau suvaldyti duomenis ir didina atvertų duomenų
brandos lygį.

Tikriausiai iškyla klausimas, kas sudaro žodynus ir kaip žinoti kokie
pavadinimai yra naudojami atvirų duomenų portalo žodyne? Mūsų `countries.csv`
pavyzdyje duomenų aprašo tipas yra `dataset`, yra dar vienas duomenų aprašo
tipas pavadinimu `model`. Mūtend `model` aprašuose ir aprošomi atvirų duomenų
portalo žodyno pavadinimai. Štai pavyzdys, kaip toks aprašas atrodo:

.. code-block:: yaml

   type: model
   name: geografija/salis
   properties:
     kodas:
       type: string
     pavadinimas:
       type: string

Dažniausiai visi `model` aprašai saugomi `models/` kataloge ir failas iki YAML
failo atitinka modelio pavadinimą, tai šuo atveju šis modelis turūtų būti
išsaugotas `models/geografija/salis.yml` faile. Toks katalogas padeda langviau
naviguoti tarp modelių aprašų ir naudoti tuos pačius pavadinimus aprašant
duomenų šaltinius.
