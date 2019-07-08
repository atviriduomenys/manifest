.. manifest documentation master file, created by
   sphinx-quickstart on Sun Jul  7 15:44:01 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. default-role:: literal

Atvirų duomenų manifestas
=========================

Kas yra manifestas?
-------------------

IT srityje `manifestu <manifest_file>`_ vadinamas failas - rodyklė, kuriame pateikiamas
visą paketą sudarančių failų sąrašas. Lyginant su knygomis, tai yra kažkas
panašaus į knygos vardų ar dalykų rodyklę su nuorodomis, kuriame puslapyje apie
tai rašoma. Lietuvos atvirų duomenų :term:`manifestas` yra duomenų rodyklė, kurioje
surašyta informacija kur rasti duomenis.

.. _manifest_file: https://en.wikipedia.org/wiki/Manifest_file

Jei tiksliau, manifestas yra failų rinkinys, o tuose failuose pateikta
informacija apie duomenų rinkinius, duomenų šaltinius ir duomenų struktūras.

Yra kelių rūšių manifesto failai, kurie skirti aprašyti skirtingiems dalykams:

- baziniam duomenų modeliui atliekančiam žodyno vaidmenį,
- tiekėjų duomenų rinkiniams,
- duomenų naudotojų naudojamų duomenų rinkiniams.

Štai pavyzdys, kaip atrodo duomenų rinkinio aprašas:

.. code-block:: yaml

   ---
   type: dataset
   name: gov/lrs/ad
   title: "Seimo nariai"
   owner: gov/lrs
   resources:
     seimo_nariai:
       type: xml
       source: http://apps.lrs.lt/sip/p2b.ad_seimo_nariai
       objects:
         politika/seimas/seimo_narys:
           source: /SeimoInformacija/SeimoKadencija/SeimoNarys
           properties:
             id:
               type: pk
               source: "@asmens_id"
             vardas:
               type: string
               source: "@vardas"
             pavarde:
               type: string
               source: "@pavardė"

Šiame pavyzdyje `type: dataset` nurodo, kad turime duomenų rinkinio aprašą.
Šiame apraše nurodytas Seimo kanceliarijos XML duomenų prieigos taškas ir
aprašyta `politika/seimas/seimo_narys` objekto duomenų struktūra. Objektą
`politika/seimas/seimo_narys` sudaro trys duomenų laukai `id`, `vardas` ir
`pavarde`. XML duomenų šaltinyje esantys duomenys susieti su vidiniu žodynu.
Pavyzdžiui, XML duomenų šaltinyje Seimo nario objektas pavadintas
`/SeimoInformacija/SeimoKadencija/SeimoNarys`, o vidiniame žodyne tai pavadinta
`politika/seimas/seimo_narys`.

Norint pasiekti šiuose duomenis, galima naudoti tokį duomenų prieigos tašką::

   /politika/seimas/seimo_narys/:dataset/gov/lrs/ad

Šiame duomenų rinkinyje naudojamo duomenų modelio aprašas atrodytų taip:

.. code-block:: yaml

   type: model
   name: politika/seimas/seimo_narys
   title: "Seimo narys"
   properties:
     id:
       type: pk
     vardas:
       type: string
       title: "Vardas"
     pavarde:
       type: string
       title: "Pavardė"

Visi duomenų rinkiniai turi naudoti vieningą duomenų modelį ir vieningą objektų
ir savybių pavadinimų žodyną, todėl ir reikalingas atskiras duomenų modelio
struktūros aprašas.

Daug skirtingų duomenų šaltinių gali turėti tuos pačius duomenis. Apjungus
tokius duomenis ir suteikus jiems globalius identifikatorius, duomenys tampa
kanoniniais ir nepriklausomais nuo vieno tiekėjo. Tokius kanoninius duomenis
galima pasiekti per tokį prieigos tašką::

   /politika/seimas/seimo_narys

Analogiškai, projektai naudojantys atvirus duomenis, pateikia tokius duomenų
struktūros aprašus:

.. code-block:: yaml

   type: project
   name: manoseimas
   title: "manoseimas.lt"
   objects:
     politika/seimas/seimo_narys:
       target: manoseimas.mps_v2.models.ParliamentMember
       properties:
         vardas:
           type: string
           target: first_name
         pavarde:
           type: string
           target: last_name

Turinti tokį aprašą, projektas lengvai gali gauti visus naujausius pakeitimus
ir taip sinchronizuoti atvirus duomenis į savo vidinę duomenų bazę, visa tai
padaroma tokio prieigos taško pagalba::

   /:project/manoseimas/:changes

Šis prieigos taškas, gražina visos su projektu susietų duomenų pakeitimus ir
konvertuoja objektų ir savybių pavadinimus iš vidinio atvirų duomenų žodyno į
vidinį projekto naudojamą žodyną.


.. toctree::
   :maxdepth: 2
   :caption: Turinys:

   glossary.rst
