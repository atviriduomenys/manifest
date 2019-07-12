.. default-role:: literal

Duomenų šaltiniai
#################

Duomenų šaltinių aprašai leidžia automatizuoti duomenų surinkimą iš įvairių
šaltinių, juos patikrinti ir konvertuoti į kitus formatus.

Šaltinio duomenų struktūros aprašas atrodo taip:

.. code-block:: yaml

   name: <rinkinys>
   type: dataset
   resources:
     <resursas>:
       type: <šaltinio tipas>
       source: <resurso šaltinis>
       sourceparams:
       objects:
         <objektas>:
           source: <objekto šaltinis>
           sourceparams:
           properties:
             <savybė>:
               type: <savybės tipas>
               source: <savybės šaltinis>
               sourceparams:

Šis aprašas yra suderinamas su DCAT_ žodynu, tačiau DCAT_ žodyno elementai
sudaro tik nedidelę dalį. Šaltinio aprašas yra išplėstas ir leidžia aprašyti ne
tik duomenų rinkinio ir resurso metaduomenis, bet ir detalią objektų ir savybių
struktūrą, duomenų šaltinius, susieti pavadinimus su vieningu žodynu ir pan.

.. _DCAT: https://www.w3.org/TR/vocab-dcat/

Šaltinio duomenų aprašo pagrindą sudaro:

- duomenų rinkinys

- resursas,

- objektas,

- savybė,

Žemiau pateikiami išsamesni apraše naudojamų elementų pažymėtų `<>` žymėmis
aprašymai.

rinkinys
   Duomenių rinkinio :term:`sisteminis pavadinimas`. Duomenų rinkinys jungia
   vieną ar kelis duomenų išteklius (resursus).

resursas
   Resurso pavadinimas gali būti bet koks, tačiau prasminga jį sieti su duomenų
   bazės ar duomenų failo pavadinimu.

šaltinio tipas
   Šiuo metu palaikomi tokie šaltinio tipai:

   - `csv`
   - `html`
   - `json`
   - `sql`
   - `xlsx`
   - `xml`

   Priklausomai nuo šaltinio tipo keičiasi visų kitų elementu interpretavimas.

resurso šaltinis
   Gali būti duomenų bazė, JSON, XML ar skaičiuoklės failas. Priklauso nuo
   šaltinio tipo.

objektas
   Objekto pavadinimas gali būti bet koks pavadinimas, tačiau jei pavadinimas
   yra siejamas su vidiniu žodynu, tada pavadinimas turi atitikti vieną iš
   `type: model` aprašų `name` reikšmę.

   Jei pavadinimas yra nesiejamas su žodynu, tada pavadinimas turi prasidėti
   taško simboliu `.`.

objekto šaltinis
   Priklausomai nuo duomenų šaltinio, gali būti duomenų bazės lentelė, CSV
   failas, JSON elemento kelias, XPath ar skaičiuoklės lapo pavadinimas.

savybė
   Objekto savybės pavadinimas. Jei nesiejama su žodyno, turi prasidėti taško
   simboliu.

   Yra trys rezervuoti savybių pavadinimai:

   - `id` - pirminis objekto raktas
   - `type` - objekto pavadinimas
   - `revision` - kontrolinė suma skirta užtikrinti duomenų vientisumą

savybės tipas
   Šiuo metu paliekami šie duomenų tipai:

   - `pk` - pirminis raktas
   - `ref` - ryšys su kitu objektu
   - `backref` - atgalinis ryšys su kitu objektu
   - `generic` - ryšis su kitu neapibrėžtu objektu
   - `array` - masyvas, kuris gali būti sudarytas iš bet kokių kitų tipų reikšmių
   - `object` - objektas, kuris gali būti sudarytas iš bet kokių kitų tipų
     reikšmių
   - `string` - bet kokio ilgio simbolių eilutė
   - `integer` - sveikas skaičius, gali būti neigiamas
   - `number` - racionalusis skaičius
   - `boolean` - loginis tipas
   - `date` - data
   - `datetime` - data ir laikas
   - `spatial` - erdviniai duomenys, gali būti taškas, linija arba plokštuma
   - `file` - failas
   - `image` - paveiksliukas
   - `url` - URL adresas

savybės šaltinis
   Priklausomai nuo šaltinio, gali būti duomenų bazės lentelės laukas, JSON
   objekto savybė, reliatyvus XPath, skaičiuoklės lapo stulpelis.

Resurso, objekto ir savybės šaltiniai `source` parametras priklauso nuo
šaltinio tipo, žemiau pateikti visų palaikomų šaltinių aprašymai su
paaiškinimais kaip interpretuojamas `source` kiekvienam iš jų.

`sourceparams` yra objektas, kuriame pateikiami papildomi parametrai, kurie
priklauso nuo šaltinio tipo.


SQL
===

SQL arba reliacinių duomenų bazių valdymo sistemos, kaip duomenų šaltinis
aprašomas taip:

resurso šaltinis
   SQL resurso šaltinis nurodo duomenų bazę, kurios duomenų struktūra aprašoma.

   Dažniausiai duomenų bazės prisijungimai nėra nurodomas duomenų struktūros
   apraše, kadangi duomenų bazės prisijungimai negali būti viešinami. Duomenų
   bazės prisijungimai turi būti perduodami per :term:`aplinkos kintamuosiuos
   <aplinkos kintamasis>` arba konfigūracijos failus.

   Duomenų bazės šaltinis aprašomas naudojant tokią URL schemą::

      <db>+<valdiklis>://<naudotojas>:<slaptažodis>@<serveris>:<prievadas>/<pavadinimas>

   db
      Duomenų bazės rūšis:

      - `sqlite`
      - `postgresql`
      - `mysql`
      - `mssql`

   valdiklis
      Konkretus duomenų bazės valdiklis (angl. *driver*) naudojamas
      komunikacijai su duomenų baze.

   naudotojas, slaptažodis
      Duomenų bazės naudotojas ir jo slaptažodis.

   serveris, prievadas
      Serveris ir serverio prievadas kur veikia duomenų bazė.

   pavadinimas
      Duomenų bazės pavadinimas.


objekto šaltinis
   Duomenų bazės lentelės pavadinimas.

savybės šaltinis
   Lentelės lauko pavadinimas.


CSV
===

resurso šaltinis
   Gali būti nenurodomas, o jei nurodomas naudojamas kaip URL bazė objekto
   šaltiniui.

   Pavyzdys:

   .. code-block:: yaml

      resources:
        example:
          type: csv
          source: https://example.com/
          objects:
            geografija/salis:
              source: countries.csv

   Šiame pavyzdyje, `countries.csv` yra jungimas su `https://example.com/`.

objekto šaltinis
   Pilnas URL iki CSV failo arba reliatyvus kelias iki CSV failo, jei nurodytas
   resurso šaltinis.

savybės šaltinis
   Stulpelio pavadinimas iš CSV failo.


JSON
====

resurso šaltinis
   URL iki JSON failo.

objekto šaltinis
   Kelias iki konkretaus elemento JSON duomenyse. Pavyzdžiui, jei turime tokį
   JSON failą:

   .. code-block:: json

      {
         "foo": {
            "bar": [
               {"baz": 1},
               {"baz": 2},
               {"baz": 3}
            ]
         }
      }

   Tada objekto šaltinis gali būti `foo.bar`, kas nurodo, kad skaitomas tik
   `foo.bar` esantis masyvas.

   Jei objekto šaltinis nenurodytas, tada savybės skaitomos iš šakninio JSON
   objekto.

savybės šaltinis
   JSON objekto attributas.


XML
===

resurso šaltinis

objekto šaltinis

savybės šaltinis


XLSX
====

resurso šaltinis

objekto šaltinis

savybės šaltinis
