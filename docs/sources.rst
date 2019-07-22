.. default-role:: literal

.. _sources:

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

- rinkinys
- resursas
- objektas
- savybė

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

Resurso, objekto ir savybės šaltiniai (`source` parametras) priklauso nuo
šaltinio tipo, žemiau pateikti visų palaikomų šaltinių aprašymai su
paaiškinimais kaip interpretuojamas `source` kiekvienam iš jų.

`sourceparams` yra papildomi parametrai, kurie priklauso nuo šaltinio tipo.

Visuose pavyzdžiuose naudojama tie patys šalies duomenys, tik duomenys
pateikiami skirtingais formatais, tačiau galutinis rezultatas visais atvejais
yra identiškas (išskyrus `id` lauko reikšmes, plačiau apie tai skaitykite
skyriuje :ref:`pk`).


SQL
===

SQL arba reliacinės duomenų bazių valdymo sistemos.

resurso šaltinis
   SQL resurso šaltinis nurodo duomenų bazę, kurios duomenų struktūra aprašoma.

   Dažniausiai duomenų bazės prisijungimai nėra nurodomas duomenų struktūros
   apraše, kadangi duomenų bazės prisijungimai negali būti viešinami. Duomenų
   bazės prisijungimai turi būti perduodami per :term:`aplinkos kintamuosiuos
   <aplinkos kintamasis>` arba konfigūracijos failus.

   :term:`Aplinkos kintamasis <aplinkos kintamasis>` formuojamas taip::

      SPINTA_DATASETS_{manifest.name}_{dataset.name}_{resource.name}

   `{manifest.name}` dažniausiai bus `default`, nebent naudojante kelis
   manifestų katalogus.

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


Pavyzdys
--------

Tarkime turime PostgreSQL duomenų bazę, kurioje yra lentelę pavadinimu
`COUNTRY`, lentelėje yra tokie duomenys:

=======  ========  ===========
id       code      country
=======  ========  ===========
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ===========

Šios lentelės duomenų aprašas atrodys taip:

.. code-block:: yaml

   name: pavyzdziai/sql
   type: dataset
   resources:
     duombaze:
       type: sql
       source: postgresql://user:password@host/dbname
       objects:
         geografija/salis:
           source: COUNTRY
           properties:
             id:
               type: pk
               source: id
             kodas:
               type: string
               source: code
             pavadinimas:
               type: string
               source: country

Pavyzdyje duomenų šaltinis nurodytas tiesiogiai pačiame YAML faile, tačiau
šaltinį galima nurodyti ir :term:`aplinkos kintamojo <aplinkos kintamasis>`
pagabla::

      SPINTA_DATASETS_DEFAULT_PAVYZDZIAI_SQL_DUOMBAZE=postgresql://user:password@host/dbname

Rezultate gauname atvertus duomenis, kuriuos galima pasiekti per šį prieigos
tašką::

   /geografija/salis/:dataset/pavyzdziai/sql

Atverta lentelė atrodys taip:

==========================================  ===========  =================
id                                          kodas        pavadinimas
==========================================  ===========  =================
`23fcdb953846e7c709d2967fb549de67d975c010`  lt           Lietuva
`6f9f652eb6dae29e4406f1737dd6043af6142090`  lv           Latvija
`11a0764da48b674ce0c09982e7c43002b510d5b5`  ee           Estija
==========================================  ===========  =================


CSV
===

Kableliais atskirti failai.

resurso šaltinis
   Gali būti nenurodomas, o jei nurodomas naudojamas kaip URL bazė objekto
   šaltiniui.

objekto šaltinis
   Pilnas URL iki CSV failo arba reliatyvus kelias iki CSV failo, jei nurodytas
   resurso šaltinis.

savybės šaltinis
   Stulpelio pavadinimas iš CSV failo.


Pavyzdys
--------

Tarkime turime CSV failą, kuris pasiekiamas adresu
`https://example.com/countries.csv`, failo turinys yra toks::

   id,code,country
   1,lt,Lietuva
   2,lv,Latvija
   3,ee,Estija

Šio CSV failo duomenų aprašas atrodys taip:

.. code-block:: yaml

   name: pavyzdziai/csv
   type: dataset
   resources:
     example:
       type: csv
       source: https://example.com/
       objects:
         geografija/salis:
           source: countries.csv
           properties:
             id:
               type: pk
               source: id
             kodas:
               type: string
               source: code
             pavadinimas:
               type: string
               source: country

Rezultate gauname atvertus duomenis, kuriuos galima pasiekti per šį prieigos
tašką::

   /geografija/salis/:dataset/pavyzdziai/csv

Atverta lentelė atrodys taip:

==========================================  ===========  =================
id                                          kodas        pavadinimas
==========================================  ===========  =================
`23fcdb953846e7c709d2967fb549de67d975c010`  lt           Lietuva
`6f9f652eb6dae29e4406f1737dd6043af6142090`  lv           Latvija
`11a0764da48b674ce0c09982e7c43002b510d5b5`  ee           Estija
==========================================  ===========  =================


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
   JSON objekto atributas.


Pavyzdys
--------

Tarkime turime JSON failą, kuris pasiekiamas adresu
`https://example.com/countries.json`, failo turinys yra toks:

.. code-block:: json

   {
       "countries": [
           {"id": 1, "code": "lt", "name": "Lietuva"},
           {"id": 1, "code": "lv", "name": "Latvija"},
           {"id": 1, "code": "ee", "name": "Estija"}
       ]
   }

Šio JSON failo duomenų aprašas atrodys taip:

.. code-block:: yaml

   name: pavyzdziai/json
   type: dataset
   resources:
     example:
       type: json
       source: https://example.com/countries.json
       objects:
         geografija/salis:
           source: countries
           properties:
             id:
               type: pk
               source: id
             kodas:
               type: string
               source: code
             pavadinimas:
               type: string
               source: name

Rezultate gauname atvertus duomenis, kuriuos galima pasiekti per šį prieigos
tašką::

   /geografija/salis/:dataset/pavyzdziai/json

Atverta lentelė atrodys taip:

==========================================  ===========  =================
id                                          kodas        pavadinimas
==========================================  ===========  =================
`23fcdb953846e7c709d2967fb549de67d975c010`  lt           Lietuva
`6f9f652eb6dae29e4406f1737dd6043af6142090`  lv           Latvija
`11a0764da48b674ce0c09982e7c43002b510d5b5`  ee           Estija
==========================================  ===========  =================


XML
===

resurso šaltinis
   URL iki XML failo.

objekto šaltinis
   XPath užklausa iki elemento iš kurio norime imti duomenis.

savybės šaltinis
   XPath užklausa, kuri vykdoma objekto šaltinio elementų kontekste.


Pavyzdys
--------

Tarkime turime XML failą, kuris pasiekiamas adresu
`https://example.com/countries.xml`, failo turinys yra toks:

.. code-block:: xml

   <root>
      <country id="1" code="lt">Lietuva</country>
      <country id="2" code="lv">Latvija</country>
      <country id="3" code="ee">Estija</country>
   </root>

Šio XML failo duomenų aprašas atrodys taip:

.. code-block:: yaml

   name: pavyzdziai/xml
   type: dataset
   resources:
     example:
       type: xml
       source: https://example.com/countries.xml
       objects:
         geografija/salis:
           source: /root/country
           properties:
             id:
               type: pk
               source: "@id"
             kodas:
               type: string
               source: "@code"
             pavadinimas:
               type: string
               source: "text()"

Rezultate gauname atvertus duomenis, kuriuos galima pasiekti per šį prieigos
tašką::

   /geografija/salis/:dataset/pavyzdziai/xml

Atverta lentelė atrodys taip:

==========================================  ===========  =================
id                                          kodas        pavadinimas
==========================================  ===========  =================
`23fcdb953846e7c709d2967fb549de67d975c010`  lt           Lietuva
`6f9f652eb6dae29e4406f1737dd6043af6142090`  lv           Latvija
`11a0764da48b674ce0c09982e7c43002b510d5b5`  ee           Estija
==========================================  ===========  =================



XLSX
====

resurso šaltinis
   URL iki XLSX failo.

objekto šaltinis
   Skaičiuoklės lapo pavadinimas.

savybės šaltinis
   Skaičiuoklės lentelės stulpelio pavadinimas.


Pavyzdys
--------

Tarkime turime XLSX failą, kuris pasiekiamas adresu
`https://example.com/countries.xlsx`, šiame skaičiuoklės faile yra lapas
pavadinimu `COUNTRIES`, o lapo turinys atrodo taip:

=======  ========  ===========
id       code      country
=======  ========  ===========
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ===========

Šios lentelės duomenų aprašas atrodys taip:

.. code-block:: yaml

   name: pavyzdziai/xlsx
   type: dataset
   resources:
     duombaze:
       type: sql
       source: https://example.com/countries.xlsx
       objects:
         geografija/salis:
           source: COUNTRIES
           properties:
             id:
               type: pk
               source: id
             kodas:
               type: string
               source: code
             pavadinimas:
               type: string
               source: country

Rezultate gauname atvertus duomenis, kuriuos galima pasiekti per šį prieigos
tašką::

   /geografija/salis/:dataset/pavyzdziai/xlsx

Atverta lentelė atrodys taip:

==========================================  ===========  =================
id                                          kodas        pavadinimas
==========================================  ===========  =================
`23fcdb953846e7c709d2967fb549de67d975c010`  lt           Lietuva
`6f9f652eb6dae29e4406f1737dd6043af6142090`  lv           Latvija
`11a0764da48b674ce0c09982e7c43002b510d5b5`  ee           Estija
==========================================  ===========  =================
