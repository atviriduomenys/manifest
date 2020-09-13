.. default-role:: literal

.. _api:

API
###

Prieš pradedant
===============

Pavyzdžių skaitymas
-------------------

Prieš pradedant skaityti verta susipažinti kokie įrankiai naudojami šios
dokumentacijos pavyzdžiuose.

Pavyzdžiuose HTTP užklausos atliekamos naudojant patogią httpie_ programėlę.

.. _httpie: https://httpie.org/

Pavyzdžiui::

    http /version

.. code-block:: http

    HTTP/1.1 200 OK
    content-type: application/json

    {
        "api": {
            "version": "0.0.1"
        },
        "build": null,
        "implementation": {
            "name": "Spinta",
            "version": "0.1.6"
        }
    }

Šiame pavyzdyje `http` komanda buvo įvykdyta su `/version` argumentu.

Pavyzdžiuose nepateikiamas konkretus domenas, kadangi domenas gali skirtis
priklausomai nuo to, kurią atvirų duomenų saugyklą naudojate, tačiau adreso
dalis einanti po domeno visada vienoda.

Apart to, kad pavyzdžiuose nenurodomas domenas, visa kita veikia taip kaip
parašyta httpie_ dokumentacijoje. Todėl rekomenduojame pirmiausia
pasiskaityti su httpie_ dokumentacija, prieš pradedant gilintis į šią atvirų
duomenų saugyklos dokumentaciją.


Duomenų modelis
---------------

Visuose pavyzdžiuose bus naudojamas vienas ir tas pats miestų ir šalių
duomenų modelis, kurios struktūra atrodo taip:


+---+---+-------------+---------+---------+
| d | m | property    | type    | ref     |
+===+===+=============+=========+=========+
| datasets/gov/dc/geo |         |         |
+---+---+-------------+---------+---------+
|   | planet          |         |         |
+---+---+-------------+---------+---------+
|   |   | name        | string  |         |
+---+---+-------------+---------+---------+
|   | country         |         |         |
+---+---+-------------+---------+---------+
|   |   | code        | string  |         |
+---+---+-------------+---------+---------+
|   |   | name        | string  |         |
+---+---+-------------+---------+---------+
|   |   | planet      | ref     | planet  |
+---+---+-------------+---------+---------+
|   |   | capital     | ref     | city    |
+---+---+-------------+---------+---------+
|   | city            |         |         |
+---+---+-------------+---------+---------+
|   |   | name        | string  |         |
+---+---+-------------+---------+---------+
|   |   | country     | ref     | country |
+---+---+-------------+---------+---------+

Duomenų modelis kiek futuristinis, darant prielaidą, kad netrukus bus
apgyvendinta ir Marso planeta, todėl šalys priklauso planetai, o miestai
šalims. Kiekviena šalis turi vieną miestą sostinę.


API adreso struktūra
====================

API yra generuojamas dinamiškai iš duomenų saugykloje esančių modelių (arba
lentelių) pavadinimų. Modelių pavadinimai gali turėti vardų erdves, vardų
erdvės yra atskirtos `/` simboliu, pavyzdžiui::

    /datasets/gov/dc/geo/planet

Šis adresas sudarytas iš `datasets/gov/dc/geo` vardų erdvės ir `planet`
modelio pavadinimo.

`datasets` vardų erdvė rodo, kad duomenys yra žali, t.y. tokie kokie pateikti
tam tikros įstaigos. Su laiku visų įstaigų duomenys bus transformuoti į vieningą
šalies masto žodyną ir pavyzdžiui `datasets/gov/dc/geo/planet` gali būti
sulietas į vieną bendrą `planets` modelį, šakninėje vardų ardvėje. Tačiau
užtikrinant stabilų ir nekintantį API bus paliekami ir pradiniai žalių duomenų
API taškai.

Konkrečiai visi `datasets` vardų erdvėje esantys modeliai turi aiškiai apibrėžtą
struktūrą, pavyzdžiui nagrinėjant `datasets/gov/dc/geo/planet` pavyzdį atskirų
kelio komponentų prasmės būdų tokios:

- `datasets/` - vardų erdvė skirta žaliems pirminiams įstaigų duomenimis.
- `gov/` - vardų erdvė skirta valstybinių įstaigų duomenimis.
- `dc/` - konkrečios valstybinės įstaigos trumpinys.
- `geo/` - įstaigos atverto duomenų rinkinio trumpinys.
- `planet` - duomenų modelis (arba lentelė).


Adreso parametrai
-----------------

Adresas gali turėti parametrus, parametrai atrodo taip::

    /:ns
    /:changes
    /:format/csv

Jei adreso kelio elementas prasideda `:` simboliu, tai po jo seka parametro
pavadinimas ir jei konkretus parametras turi argument, gali sekti vienas ar
daugiau argumentų.


Identifikatorius
----------------

Identifikatorius gali taip pat yra adreso parametras, tik jis neprasideda `:`
simboliu, o eina iš karto po modelio pavadinimo ir tai turi būti UUID
simbolių eilutė, pavyzdžiui::

    /datasets/gov/dc/geo/planet/77e0bb52-f8ae-448f-b4c2-7de6bb150ff0

Identifikatorius taip pat gali turėti argumentus, identifikatoriaus
argumentai yra modelio savybė, pavyzdžiui::

    /datasets/gov/dc/geo/city/7d473db2-d363-4318-9b84-138eb5d70f70/planet

Tokiu būdu yra galimybė gauti tik konkrečios modelio savybės duomenis.


Užklausa
--------

URL Query dalyje, po `?` simbolio galima pateikti papildomus užklausos
parametrus, pavyzdžiui::

    /datasets/gov/dc/geo/planet?select(name)&sort(name)


Rezervuoti pavadinimai
----------------------

Įvairiose API vietose, įskaitant ir adreso struktūrą naudojami rezervuoti
pavadinimai, kurių pavadinimas prasideda simboliu `_`.


Vardų erdvės
============

Atvirų duomenų saugykla yra didelis katalogas, kuriame sudėta daug įvairių
duomenų. Katalogai vadinami vardų erdvėmis.

Aukščiausiame lygyje yra globali vardų erdvė::

    http /

.. code-block:: http

    HTTP/1.1 200 OK
    content-type: application/json

    {
        "_data": [
            {
                "_id": "datasets/:ns",
                "_type": "ns",
                "title": "datasets"
            }
        ]
    }


Globalioje vardų erdvėje yra kita vardų erdvė `datasets`. Žinome, kad `datasets`
yra vardų erdvė, kadangi tai nurodyta `_type` savybėje, kurios reikšmė `ns`, kas
reiškia *Name Space* arba *Vardų Erdvė* išvertus į Lietuvių kalbą.

Į vardu erdves reikia kreiptis nurodant `/:ns` parametrą::

    http /datasets/gov/dc/geo/:ns

.. code-block:: http

    HTTP/1.1 200 OK
    content-type: application/json

    {
        "_data": [
            {
                "_id": "datasets/gov/dc/geo/planet",
                "_type": "model",
                "title": "Planet"
            },
            {
                "_id": "datasets/gov/dc/geo/country",
                "_type": "model",
                "title": "Country"
            },
            {
                "_id": "datasets/gov/dc/geo/city",
                "_type": "model",
                "title": "City"
            }
        ]
    }

Jei `/:ns` parametras nebūtų nurodytas, tada saugykla bandytų ieškoti modelio
pavadinimu `datasets/gov/dc/geo` ir neradus tokio modelio būtų gražintas `404
Not Found` klaidos kodas.