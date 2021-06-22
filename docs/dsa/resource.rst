.. _resource:

Duomenų šaltiniai
=================

.. _resource-type-sql:

SQL
---

.. module:: sql

.. _sql-resource-source:

.. describe:: resource.source

    Duomenų bazės URI. Duomenų bazės URI formuojamas naudojant tokį ABNF_
    šabloną:

    .. _ABNF: https://en.wikipedia.org/wiki/Augmented_Backus–Naur_form

    .. code-block:: abnf

        uri = type ["+" driver] "://"
              [user [":" password] "@"]
              host [":" port]
              "/" database ["?" params]

    Šablone naudojamų kintamųjų aprašymas:

    .. describe:: type

        Duomenų bazių serverio pavadinimas:

        .. describe:: sqlite

        .. describe:: postgresql

        .. describe:: mysql

        .. describe:: oracle

        .. describe:: mssql

    .. describe:: driver

        Konkretaus duomenų bazių serverio tvarkyklė naudojama komunikacijai su
        duomenų baze.

    .. describe:: user

        Naudotojo vardas jungimuisi prie duomenų bazės.

    .. describe:: password

        Duomenų bazės naudotojo slaptažodis.

    .. describe:: host

        Duomenų bazių serverio adresas.

    .. describe:: port

        Duomenų bazių serverio prievadas.

    .. describe:: database

        Konkrečios duomenų bazės pavadinimas.

    .. describe:: params

        Papildomi parametrai Query string formatu.

.. describe:: resource.prepare

    Formulė skirta papildomiems veiksmams reikalingiems ryšiui su duomenų baze
    užmezgimui ir duomenų bazės paruošimui, kad būtų galima skaityt duomenis.

.. describe:: resource.type

    Galimos reikšmės: `sql`.

.. describe:: resource.prepare

    .. function:: connect(dsn, schema: str = None, encoding: str = 'utf-8')

        :arg dsn: Duomenų bazės URI, kaip nurodyta :ref:`resource.source
            <sql-resource-source>`.
        :arg schema: Duomenų bazės schema.
        :arg encoding: Duomenų bazės koduotė.

        Naudojama tais atvejais, kai jungiantis prie duomenų bazės reikia
        perduoti papildomus parametrus.

.. describe:: model.source

    Duomenų bazėje esančios lentelės pavadinimas.

.. describe:: property.source

    Lentelės stulpelio pavadinimas.


.. _resource-type-sql-dump:

SQL Dump
--------

.. describe:: resource.source

    Kelias iki failo, kuriame yra SQL dump.

    Jei nurodyta `-`, tada SQL dump failas bus skaitomas iš standartinės
    įvesties.

    Pavyzdžiui, norint iš SQL dump generuoti :term:`DSA`, galima naudoti
    tokią komandą::

        spinta inspect -f sqldump /kelias/iki/dump.sql

    Arba, perduodant duomenis per standartinė įvestį::

        cat /kelias/iki/dump.sql | spinta inspect -f sqldump -


.. describe:: resource.prepare

    Žiūrėti :ref:`failai`.

.. describe:: resource.type

    Galimos reikšmės: `sqldump`.


CSV
---

.. module:: tabular

.. describe:: resource.type

    Galimos reikšmės: `csv`, `tsv`.

.. describe:: resource.source

    Žiūrėti :ref:`failai`.

.. describe:: resource.prepare

    .. function:: sep(separator)

        Nurodoma kaip CSV faile atskirti stulpeliai. Pagal nutylėjimą
        `separator` reikšmė yra `,`.

.. describe:: model.source

    Nenaudojama, kadangi CSV resursas gali turėti tik vieną lentelę.

.. describe:: model.prepare

    Žiūrėti :ref:`stulpeliai-lentelėje`.

.. describe:: property.source

    Žiūrėti :ref:`stulpeliai-lentelėje`.


JSON
----

.. module:: json

.. describe:: resource.type

    Galimos reikšmės: `json`, `jsonl`.

.. describe:: resource.source

    Žiūrėti :ref:`failai`.

.. describe:: model.source

    JSON objekto savybės pavadinimas, kuri rodo į masyvą reikšmių, kurios bus
    naudojamos kaip modelio duomenų eilutės. Kiekvienas masyvo elementas
    atskirai aprašomas :data:`property` dimensijoje. Jei JSON objektas yra
    kompleksinis žiūrėti :ref:`kompleksinės-struktūros`.

.. describe:: property.source

    JSON objekto savybė, kurioje pateikiami aprašomo stulpelio duomenys.

.. describe:: property.prepare

    Žiūrėti :ref:`kompleksinės-struktūros`.


XML
---

.. module:: xml

.. describe:: resource.type

    Galimos reikšmės: `xml`, `html`.

.. describe:: resource.source

    Žiūrėti :ref:`failai`.

.. describe:: model.source

    `XPath <https://en.wikipedia.org/wiki/XPath>`_ iki elementų sąrašo kuriame
    yra modelio duomenys.

.. describe:: model.prepare

    Jei neužpildyta, vykdoma :func:`xpath(self) <xml.xpath>` funkcija.

    .. function:: xpath(expr)

        Vykdo nurodyta `expr`, viso XML dokumento kontekste.

.. describe:: property.source

    `XPath <https://en.wikipedia.org/wiki/XPath>`_ iki elemento kuriame yra
    duomenys.

.. describe:: model.prepare

    Jei neužpildyta, vykdoma :func:`xpath(self) <xml.xpath>` funkcija, iš
    :data:`model` gauto elemento kontekste.


Skaičiuoklių lentelės
---------------------

.. module:: spreadsheet

.. describe:: resource.type

    Galimos reikšmės: `xlsx`, `xls` arba `odt`.

.. describe:: resource.source

    Žiūrėti :ref:`failai`.

.. describe:: model.source

    Skaičiuoklės faile esančio lapo pavadinimas.

.. describe:: model.prepare

    Žiūrėti :ref:`stulpeliai-lentelėje`.

.. describe:: property.source

    Žiūrėti :ref:`stulpeliai-lentelėje`.


WSDL
----

.. module:: wsdl

.. describe:: resource.type

    Galima reikšmė: `wsdl`.

.. describe:: resource.source

    WSDL URI.

.. describe:: model.source

    Nenaudojamas.

.. describe:: model.prepare

    .. function:: service(name, *args, **kwargs)

        WSDL funkcijos `name` iškvietimas.

    .. function:: wsdl(type, **kwargs)

        Inicializuoja nurodytą `type` WSDL tipą.

.. describe:: property.source

    Rezultato objekto atributas.

.. describe:: property.prepare

    Žiūrėti :ref:`kompleksinės-struktūros`.
