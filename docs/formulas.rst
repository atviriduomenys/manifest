.. default-role:: literal

.. _formulas:

Formulės
########

Formulės pildomas :data:`prepare` stulpelyje. Formulių pagalba galima atlikti
įvairius duomenų transformavimo, nuasmeninimo, filtravimo ir kokybės tikrinimo
veiksmus.

Kadangi yra labai didelė įvairovė duomenų formatų ir duomenų valdymo mechanizmų,
siekiant suvaldyti visą šią įvairovę :term:`DSA` formulės leidžia vieningai
aprašyti veiksmus su duomenimis. Vėliau formulės verčiamos į vieningą AST_, kurį
gali interpretuoti automatizuotos priemonės, priklausomai nuo duomenų šaltinio
ir konteksto ir DSA sluoksnio.

.. _AST: https://en.wikipedia.org/wiki/Abstract_syntax_tree

Gramatika
=========

Formulių sintaksė atitinką šią ABNF_ gramatiką:

.. code-block:: abnf

    formula     = testlist
    testlist    = test *("," test) *1","
    test        = or
    or          = and *("|" and)
    and         = not *("&" not)
    not         = "!" not / comp
    comp        = expr *(compop expr)
    expr        = term *(termop term)
    term        = factor *(factorop factor)
    factor      = sign factor / composition
    composition = atom *trailer
    atom        = "(" *1group ")"
                / "[" *1list "]"
                / func / value / name
    group       = test *("," test) *1","
    list        = test *("," test) *1","
    trailer     = "[" *1filter "]" / method / attr
    func        = name call
    method      = "." name call
    call        = "(" *1arglist ")"
    arglist     = argument *("," argument) *1","
    argument    = test / kwarg
    kwarg       = name ":" test
    filter      = test *("," test) *1","
    attr        = "." name
    value       = null / bool / integer / number / string / star
    compop      = ">=" / "<=" / "!=" / "=" / "<" / ">"
    termpop     = "+" / "-"
    factorop    = "*" / "/" / "%"
    sign        = "+" / "-"
    star        = "*"
    name        = ~/[a-z_][a-z0-9_]*/i
    number      = ~/\d+(\.\d+)?/
    integer     = ~/0|[1-9]\d*/
    bool        = "false" / "true"
    null        = "null"
    string      = ~/(?!"").*?(?<!\\)(\\\\)*?"|'(?!'').*?
                    (?<!\\)(\\\\)*?'/i


Sintaksės medis
===============

Formulės verčiamos į vieningą abstraktų sintaksės medį. Vieningas abstraktus
sintaksės medis leidžia atskirti formulės skaitymo ir interpretavimo veiklas.

Abstraktus sintaksės medis sudarytas iš vienodų elementų turinčių tokias
savybes:

.. describe:: name

    Funkcijos pavadinimas.

.. describe:: args

    Funkcijos argumentų sąrašas, kurį gali sudaryti konkrečios reikšmės ar kiti
    medžio elementai, veiksmai.

Visos formulėje naudojamos išraiškos sintaksės medyje verčiamos į funkcijų ir
argumentų medį. Pavyzdžiui `test("a", "b")` bus verčiamas į:

.. code-block:: python

    {
        "name": "test",
        "args": ["a", "b"],
    }


Funkcijų iškvietimas
====================

Formulės susideda iš vykdomų funkcijų sekos. Pavyzdžiui funkcijos pavadinimu
`test` vykdymas formulėje atrodys taip:

.. code-block:: python

    test()

Aukščiau pavyzdyje pateikta furmulė vykdo funkciją `test`, be argumentų. Tačiau
funkcijos gali turėti pozicinius ir vardinius argumentus.


Poziciniai argumentai
=====================

Poziciniai argumentai perduodami taip:

.. code-block:: python

    test(a, b, c)

Pavyzdyje, funkcijai `test` perduodami trys argumentai `a`, `b` ir `c`. Šioje
dokumentacijoje, tais atvejais, kai funkcijos pozicinių argumentų skaičius nėra
fiksuotas, naudojama `*args` išraiška, kur `*` nurodo, kad pozicinių argumentų
gali būti 0 ar daugiau.


Vardiniai argumentai
====================

Vardiniai argumentai funkcijai perduodami taip:

.. code-block:: python

    test(a: 1, b: 2, c: 3)

Pozicinius argumentus būtina perduoti tiksliai tokia tvarka, kokios tikisi
funkcija. Tačiau vardinius argumentus, galima perduoti, bet kuria tvarka.

Jei vardinių argumentų sąrašas nėra fiksuotas, dokumentacijoje toks argumentų
sąrašas užrašomas `**kwargs` forma, kur `**` nurodo, kad vardinių argumentų
gali būti 0 ar daugiau.


Alternatyvus funkcijos iškvietimas
==================================

Funkcijų iškvietimas gali būti užrašomas įprastiniu būdu, pavyzdžiui:

.. code-block:: python

    test(test(test(a), b), c)

Arba funkcijų grandinės (angl. `Method chain`_) būdu:

.. _Method chain: https://en.wikipedia.org/wiki/Method_chaining

.. code-block:: python

    a.test().test(b).test(c)

Kadangi formulės dažnai naudojamos tam tikros reikšmės transformavimui, todėl
dažnai formulė yra lengviau skaitoma, naudojant funkcijų grandinę.

`test(a)` yra `a.test()` arba `test(a, b)` ir `a.test(b)` yra ekvivalentūs
(UFCS_).

.. _UFCS: https://en.wikipedia.org/wiki/Uniform_Function_Call_Syntax


Funkcijos
=========

Priklausomai nuo duomenų šaltinio ar konteksto gali būti naudojami skirtingi
veiksmai, tačiau žemiau yra pateikti bendrosios paskirties veiksmai:

.. function:: bind(name)

    Rodo į reikšmę pavadinimu `name` iš konteksto. Reikšmės ieškoma tokia
    tvarka:

    - :func:`var`

    - :func:`param`

    - :func:`item`

    - :func:`prop`

.. function:: prop(name)

    Modelio savybė pavadinimu `name` iš :data:`property` stulpelio.

.. function:: item(name)

    Sąrašo elemento savybė pavadinimu `name`.

.. function:: param(name)

    Parametras pavadinimu `name`. Žiūrėti :ref:`parametrizacija`.

.. function:: var(name)

    Kintamasis apibrėžtas :func:`set` funkcijos pagalba.

.. function:: self

    Rodo į aktyvią reikšmę, naudojamas :data:`property.prepare` formulėse.

.. function:: or(*args)

    Taip pat galima naudoti tokia išraiška::

        a | b | c

    Grąžiną pirmą netuščią reikšmę. Pirmoji netuščia reikšmė nutraukia sekančių
    `args` argumentų interpretavimą.

.. function:: and(*args)

    Taip pat galima naudoti tokia išraiška::

        a & b & c

    Grąžina pirmą tuščią reikšmę arba paskutinę reikšmę, jei prieš tai esančios
    reikšmės netuščios.

.. function:: not(arg)

    Taip pat galima naudoti tokia išraiška::

        !arg

    Jei `arg` tuščia grąžina `true`, priešingu atveju `false`.

.. function:: eq(a, b)

    Taip pat galima naudoti tokia išraiška::

        a = b

    `a` lygus `b`.

.. function:: ne(a, b)

    Taip pat galima naudoti tokia išraiška::

        a != b

    `a` nelygus `b`.

.. function:: lt(a, b)

    Taip pat galima naudoti tokia išraiška::

        a < b

    `a` mažiau už `b`.

.. function:: le(a, b)

    Taip pat galima naudoti tokia išraiška::

        a <= b

    `a` mažiau arba lygu už `b`.

.. function:: gt(a, b)

    Taip pat galima naudoti tokia išraiška::

        a > b

    `a` daugiau už `b`.

.. function:: ge(a, b)

    Taip pat galima naudoti tokia išraiška::

        a >= b

    `a` daugiau arba lygu už `b`.

.. function:: add(a, b)

    Taip pat galima naudoti tokia išraiška::

        a + b

    `a` ir `b` suma.

.. function:: sub(a, b)

    Taip pat galima naudoti tokia išraiška::

        a - b

    `a` ir `b` skirtumas.

.. function:: mul(a, b)

    Taip pat galima naudoti tokia išraiška::

        a * b

    `a` ir `b` sandauga.

.. function:: div(a, b)

    Taip pat galima naudoti tokia išraiška::

        a / b

    `a` ir `b` dalyba.

.. function:: mod(a, b)

    Taip pat galima naudoti tokia išraiška::

        a % b

    `a` ir `b` modulis.

.. function:: positive(a)

    Taip pat galima naudoti tokia išraiška::

        +a

    Gali būti interpretuojamas skirtingai, priklausomai nuo konteksto.
    Įprastiniu atveju keičia skaičiaus ženklą.

.. function:: negative(a)

    Taip pat galima naudoti tokia išraiška::

        -a

    Gali būti interpretuojamas skirtingai, priklausomai nuo konteksto.
    Įprastiniu atveju keičia skaičiaus ženklą.

.. function:: group(*args)

    Taip pat galima naudoti tokia išraiška::

        (*args)

    Grupė argumentų.

    ()
        Tuščia grupė.

    a, b
        Tas pats, kas `group(a, b)`.

.. function:: list(*args)

    Taip pat galima naudoti tokia išraiška::

        [*args]

    Sąrašas reikšmių.

.. function:: getattr(object, attr)

    Taip pat galima naudoti tokia išraiška::

        object.attr

    Gaunamos reikšmės pagal atributą arba raktą.

.. function:: getitem(object, item)

    Taip pat galima naudoti tokia išraiška::

        a[item]

    Gaunamos reikšmės pagal atributą arba raktą.

    :func:`getitem` gali būti interpretuojamas kaip sąrašo reikšmių filtras::

        a[b > c]


.. function:: dict(**kwargs)

    Taip pat galima naudoti tokia išraiška::

        {a: b}

    Sudėtinė duomenų struktūra.

.. function:: set(**kwargs)

    Taip pat galima naudoti tokia išraiška::

        {a, b}

    Reikšmių aibė.

.. function:: op(operator)

    Taip pat galima naudoti tokia išraiška::

        a(*)

    Operatoriai gali būti naudojami kaip argumentai.
