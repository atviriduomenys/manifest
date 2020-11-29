.. default-role:: literal
.. _kaupiami-duomenys:

Kaupiami duomenys
#################

:data:`level` = 1.

Duomenys, kurie kaupiami bet kokia forma, kurioje yra matoma tam tikra duomenų
struktūra, tačiau patys duomenys pateikti taip, kad matomos struktūros
nuskaityti galimybės nėra, tada :data:`level` stulpelyje nurodome `1`. Tokiu
būdu pažymėdami, kad duomenys yra, juose aiškiai matoma tam tikra struktūra, bet
jų nuskaityti galimybės nėra.

Nestruktūruotų duomenų inventorizacija yra svarbi, kadangi tai leidžia matyti
pilnesnį viso duomenų ūkio vaizdą, leidžia užpildyti trūkstamų duomenų skyles.

Inventorizuojant nestruktūruotus duomenis, pirmiausia reikia surasti tam tikrą
pasikartojančią struktūrą ir ją aprašyti.

Kaip pavyzdį galima galime imti skaitmenintus RKB metrikus.

.. image:: /static/metrikai.png

Konkrečiai šiame pavyzdyje pateikti santuokos metrikų įrašai, tokių
skaitmenintų paveikslėlių yra ištisos knygos ir visose knygose pateikiami
gimimo, santuokos ir mirties įrašai, turintys labai aiškią struktūrą.

Deja, nuskaityti duomenis iš tokių paveiksliukų galimybės nėra, arba tokių
duomenų nuskaitymas yra ypač sunkiai įgyvendinimas, tačiau galime pateikti
tokių duomenų struktūros aprašą, kuris atrodys taip:

+----+---+---+---+---+------------+--------+-------+--------+-------+
| id | d | r | b | m | property   | type   | ref   | source | level |
+====+===+===+===+===+============+========+=======+========+=======+
|    | datasets/gov/rkb/metrikai  |        |       |        |       |
+----+---+---+---+---+------------+--------+-------+--------+-------+
|    |   | epaveldas              |        |       |        |       |
+----+---+---+---+---+------------+--------+-------+--------+-------+
|    |   |   |   | Lapas          |        |       |        |       |
+----+---+---+---+---+------------+--------+-------+--------+-------+
|    |   |   |   |   | paveikslas | image  |       |        | 1     |
+----+---+---+---+---+------------+--------+-------+--------+-------+
|    |   |   |   | Asmuo          |        |       |        |       |
+----+---+---+---+---+------------+--------+-------+--------+-------+
|    |   |   |   |   | vardas     | string |       |        | 1     |
+----+---+---+---+---+------------+--------+-------+--------+-------+
|    |   |   |   |   | pavarde    | string |       |        | 1     |
+----+---+---+---+---+------------+--------+-------+--------+-------+
|    |   |   |   | Ivykis         |        |       |        |       |
+----+---+---+---+---+------------+--------+-------+--------+-------+
|    |   |   |   |   | tipas      | string |       |        | 1     |
+----+---+---+---+---+------------+--------+-------+--------+-------+
|    |   |   |   |   | asmuo      | ref    | asmuo |        | 1     |
+----+---+---+---+---+------------+--------+-------+--------+-------+
|    |   |   |   |   | data       | date   |       |        | 1     |
+----+---+---+---+---+------------+--------+-------+--------+-------+
|    |   |   |   |   | lapas      | ref    | lapas |        | 1     |
+----+---+---+---+---+------------+--------+-------+--------+-------+

Paruošus, kad ir labai primityvų inventorizacijos lentelės variantą, galima
toliau su ja dirbti, sieti su kitais modeliais, gauti paklausos rodiklius i
duomenų naudotojo, tobulinti duomenų modelį, dokumentuoti duomenų laukus.

Tai, kad tokie duomenys dalyvauja bendroje apskaitoje, reiškia, kad galima
matyti, kiek potencialių projektų galėtų įdarbinti šiuos duomenis ir kokią
naudą tai galėtų atnešti.
