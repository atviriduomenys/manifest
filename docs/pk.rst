.. default-role:: literal

.. _pk:

Pirminis raktas
###############

Manifesto duomenų modelis yra :ref:`normalizuotas <norm>`, tai reiškia, kad objektai yra
išskaidyti į plokščius objektus ir objektai tarpusavyje gali būti jungiami
pirminio rakto (lauko `id`) pagalba.

Laukas `id` yra rezervuotas ir visi duomenų aprašai privalo nurodyti šį lauką.
Lauko `id` tipas turi būti `pk`, pavyzdys:

.. code-block:: yaml

   id:
     type: pk
     source: id

Būtina užtikrinti, kad objektas turėtų unikalų pirminį raktą. Jei duomenų
šaltinis teikia duomenis su pirminiu raktu, tada viskas labai paprasta, tačiau
jei pirminio rakto nėra, tada tenka pirminį raktą išgauti jungiant kelias
reikšmes, kurie visi kartu unikaliai identifikuoja objektą.

Kai reikia jungti kelias reikšmes, pirminio rakto aprašas atrodo taip:

.. code-block:: yaml

   id:
     type: pk
     source:
       - foo
       - bar
       - baz
      
`id` lauko reikšmė gaunama serializuojant `id` lauko reikšmę MsgPack_ formatu
ir rezultatą verčiant į SHA1_ kontrolinę sumą. Jei `id` reikšmė nėra sąrašas,
tada reikšmė verčiama į sąrašą. Pavyzdžiui `[1, 2, 3]` sąrašas būtų verčiamas
į::

   78a74af6c06029985f388dfeceb9794100377124

Atkreipkite dėmesį, kad laukų sąrašo tvarka yra svarbi, sukeitus sąrašo
elementus vietomis, pasikeis ir pirminio rakto reikšmė.


Globalūs identifikatoriai
=========================

Jei tik įmanoma, reikėtų naudoti tokius identifikatorius, kurie yra globalūs.
Pavyzdžiui jei turime tokią lentelę:

=======  ========  ===========
id       code      country
=======  ========  ===========
1        lt        Lietuva
2        lv        Latvija
3        ee        Estija
=======  ========  ===========

Čia pirminiam raktui geriau naudoti `code`, o ne `id`, kadangi `id` yra lokalus
duomenų rinkinio identifikatorius, o šalies kodas yra globalus. Tačiau, jei
šiame duomenų rinkinyje objektai jungiami tik naudojant lokalų pirminį raktą,
tai žinoma, tada `id` laukui geriau naudoti lokalų pirminį raktą, su kuriuo
jungiasi visi kiti duomenų rinkinio objektai.


.. _MsgPack: https://msgpack.org/
.. _SHA1: https://en.wikipedia.org/wiki/SHA-1
