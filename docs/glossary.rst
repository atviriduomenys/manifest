Terminai
########

.. glossary::

   aplinkos kintamasis
      Angliškai tai vadinama *environment variables*, tai yra operacinės
      sistemos aplinkos kintamieji.

      Plačiau apie tai skaitykite `Vikipedijoje
      <https://en.wikipedia.org/wiki/Environment_variable>`__.

   duomenų serializavimo formatas
      Duomenys gali būti serializuojami įvairiais formatais, pavyzdžui YAML
      formatu:

      .. code-block:: yaml

         type: project
         title: Manifestas

      JSON formatu:

      .. code-block:: json

         {"type": "project", "title": "Manifestas"}

      Turtle formatu:

      .. code-block:: ttl

         @prefix foaf: <http://xmlns.com/foaf/0.1/> .
         @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
         <http://atviriduomenys.lt> a foaf:Project;
             rdfs:label "Manifestas" .

      MessagePack dvejetainiu formatu, kurio turinys pateiktas naudojant BASE64
      koduotę::

         gqR0eXBlp3Byb2plY3SkbmFtZapNYW5pZmVzdGFz

      Visuose šiuose pavyzdžiuose yra pateikti tie patys duomenys, tačiau
      naudojami skirtingi duomenų serializavimo formatai, koduotės ir skirtingi
      žodynai.

   manifestas
      Atvirų duomenų manifestas yra :term:`YAML` failų rinkinys, kuriuose
      aprašyti duomenų šaltiniai ir struktūra.

      Žodžiu „Manifest“ IT kontekste vadinamas failas, kuriame pateiktas kitų į
      vieną paketą įtrauktų failų sąrašas. Plačiau apie tai skaitykite
      `Vikipedijoje <https://en.wikipedia.org/wiki/Manifest_file>`__.

   metaduomenys
      Duomenys apie duomenis yra vadinami metaduomenimis. Pavyzdžiui duomenų
      struktūros aprašas konkrečiam CSV duomenų failui gali būti vadinamas CSV
      failo metaduomenimis.

   normalizavimas
      Duomenų normalizavimas yra duomenų struktūros transformavimo procesas
      taikant taip vadinamas normalines formas, tam kad sumažinti duomenų
      pasikartojimą.

      Plačiau apie tai skaitykite `Vikipedijoje
      <https://en.wikipedia.org/wiki/Database_normalization>`__.

   prieigos taškas
      Prieigos taškas yra :term:`REST API` terminas, nurodantis URL kelio dalį iki tam
      tikro resurso.

      Plačiau skaitykite `Vikipedijoje
      <https://en.wikipedia.org/wiki/Web_API#Endpoints>`__.

   REST API
      Representational State Transfer (REST) yra taisyklių ir rekomendacijų
      rinkinys sirtas :term:`web servisams <web servisas>` kurti.

      Plačiau skaitykite `Vikipedijoje
      <https://en.wikipedia.org/wiki/Representational_state_transfer>`__.

   web servisas
      Web servisas yra interneto paslauga skirta automatizuotiems robotams.
      Interneto svetainės dažniausiai yra skirtos žmonėms, tačiau web servisai
      yra skirti mašioms, kurios gali komunikuoti viena su kita.

      Plačiau skaitykite `Vikipedijoje
      <https://en.wikipedia.org/wiki/Web_service>`__.

   YAML
      YAML yra :term:`duomenų serializavimo formatas`, kuris skirtas ne tik
      mašininiam skaitymui, bet su šio formato turiniu tiesiogiai gali dirbti
      ir žmogus. YAML formato pavyzdys:

      .. code-block:: yaml

         container:
           name: value

      YAML yra sukurtas JSON formatu pagrindu, siekant palengvinti darbą su
      JSON serializuotais duomenimis žmonėms. Analogiškas pavyzdys JSON formatu
      atrodo taip:

      .. code-block:: json

         {"container": {"name": "value"}}

   viešasis žodynas
      Viešieji žodynai, dar vadinami ontologijomis, šie žodynai dažnai yra
      gerai dokumentuoti ir skelbiami viešai, jie yra skirti globaliam
      susietūjų duomenų tinkui kurti (angl. *linked data*).

   sisteminis pavadinimas
      Sistemionis pavadinimas yra naudojamas objektų identifikavimui ir yra
      naudojamas URL nuorodose ir visur kitur, kure reikia nurodyti ryšį su
      objektų, naudojamas to objekto sisteminis pavadinimas.

      Sisteminis pavadinimas sudaromas tik iš lotyniškų raidžių ir `-_/`
      simbolių.

   žodynas
      Duomenų kontekste, žodynas yra susitarimas, kokiais pavadinimais vadinami
      objektai ir jų savybės. Dažniausiai kiekvienas duomenų rinkinys turi savo
      vidinį naudojamą žodyną, visas Lietuvos atvirų duomenų modelis turi savo
      vidinį žodyną, kuris suvienodina skirtingus duomenų rinkinių naudojamus
      žodynus. Yra :term:`viešieji žodynai <viešasis žodynas>`, dar vadinami
      ontologijomis, kurie yra skelbiami viešai ir skirti globaliam susietųjų
      duomenų tinklui kurti.


