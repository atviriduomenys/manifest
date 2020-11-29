.. default-role:: literal
.. _išoriniai-žodynai:

Išoriniai žodynai
=================

Išorinių žodynų pagalba, galima susieti aprašomus duomenis su išoriniais
žodynais. Susiejimas atliekamas :data:`model.uri` ir :data:`property.uri`,
naudojant :ref:`išorinių žodynų URI prefiksus <išorinių-žodynų-prefiksai>`.

Pavyzdžiui turint tokį duomenų šaltinį:

===  =========
country
--------------
id   name
===  =========
1    Vilnius
===  =========

Ir šį šaltinį atitinkančią :term:`DSA` lentelę:

+----+---+---+---+---+----------+---------+-------+-----------------------------+
| id | d | r | b | m | property | type    | ref   | uri                         |
+====+===+===+===+===+==========+=========+=======+=============================+
|    |   |   |   |   |          | prefix  | locn  | \http://www.w3.org/ns/locn# |
+----+---+---+---+---+----------+---------+-------+-----------------------------+
|    | datasets/example/org     |         |       |                             |
+----+---+---+---+---+----------+---------+-------+-----------------------------+
|    |   | salys                | sql     |       |                             |
+----+---+---+---+---+----------+---------+-------+-----------------------------+
|    |   |   |   | Country      |         | id    | locn:Location               |
+----+---+---+---+---+----------+---------+-------+-----------------------------+
|    |   |   |   |   | id       | integer |       |                             |
+----+---+---+---+---+----------+---------+-------+-----------------------------+
|    |   |   |   |   | name     | string  |       | locn:geographicName         |
+----+---+---+---+---+----------+---------+-------+-----------------------------+

Galima duomenis eksportuoti `RDF Turtle`_ formatu, kas atrodytų taip:

.. _RDF Turtle: https://en.wikipedia.org/wiki/Turtle_(syntax)

.. code-block:: ttl

    @base <https://data.gov.lt/> .
    @prefix locn: <http://www.w3.org/ns/locn#> .

    <datasets/example/org/Country/eb09946c-26e1-4698-a298-7bb1e468b165>
        a locn:Location ;
        locn.geographicName "Vilnius" .


Išoriniai žodynai ne tik suteikia galimybę eksportuoti duomenis :term:`RDF`
formatu, bet taip pat naudojami ir :ref:`asmenį identifikuojančių duomenų
žymėjimui <pii>`.

