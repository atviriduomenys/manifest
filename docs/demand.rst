.. default-role:: literal

Poreikio deklaravimas
#####################


Poreikis deklaruojamas inventorizacijų lentelių pagalba. Norint deklaruoti
poreikį reikia atsisiųsti duomenų teikėjo paskelbtą inventorizacijos lentelę,
toje lentelėje pateikti duomenis apie projektą, kuriam reikia duomenų ir
lentelėje palikti tik tuos duomenų laukus, kurie yra aktualūs projektui.

Pavyzdys:

+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+
| id | d | r | b | m | property          | source     | prepare | type      | ref   | level | access | uri | title | description |
+====+===+===+===+===+===================+============+=========+===========+=======+=======+========+=====+=======+=============+
|    | projects/com/x                    |            |         | project   |       |       |        |     |       |             |
+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+
|    |   |   |   |   |                   |            |         | employees | 10    |       |        |     |       |             |
+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+
|    |   |   |   |   |                   |            |         | users     | 1000  |       |        |     |       |             |
+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+
|    |   |   |   |   |                   |            |         | revenue   | 10000 |       |        |     |       |             |
+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+
| 47 | datasets/gov/dc/countries         |            |         |           |       |       |        |     |       |             |
+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+
|    |   | sql                           |            |         |           |       |       |        |     |       |             |
+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+
|    |   |   |                           |            |         |           |       |       |        |     |       |             |
+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+
| cd |   |   |   | countries             |            |         |           | id    |       |        |     |       |             |
+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+
|    |   |   |   |   | id                |            |         | integer   |       | 4     |        |     |       |             |
+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+
|    |   |   |   |   | code              |            |         | string    |       | 2     |        |     |       |             |
+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+
|    |   |   |   |   | name              |            |         | string    |       | 2     |        |     |       |             |
+----+---+---+---+---+-------------------+------------+---------+-----------+-------+-------+--------+-----+-------+-------------+

Lentelė pildoma arba pridedant naujus laukus arba keičiant esamus. Pavyzdžiui,
jei jums reikia didesnio lauko `code` brandos lygio, vietoje `2` galima
pakeisti `3`, tokiu būdu informuojant, kad yra poreikis gauti didesnio brandos
lygio lauką.

Jei tarkim neaiški lauko `id` paskirtis, galima stulpelyje `title` įrašyti `?`
arba stulpelyje `description` įrašyti klausimą ar pastebėjimą.

Analogiškai, galima teikti ne tik poreikį bet ir pranešti apie pastebėtas
klaidas. Pavyzdžiui, jei laukas `id` turi brandos lygį `4`, tačiau jūs manote,
kad taip nėra, galite nurodyti teisingą brandos lygį, pavyzdžiui `2`. Tokiu
atveju bus pranešta, kad yra klaida.

Tokiu būdu galima keisti visus duomenis.

`projects/com/x` dalis, kartu su `employees`, `users` ir `revenue` yra
nebūtina. Tačiau jei pateikta, toks poreikis įtauna didesnį prioritetą.
