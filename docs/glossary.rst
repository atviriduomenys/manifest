Terminai
########

.. glossary::

    aplinkos kintamasis
        Angliškai tai vadinama *environment variables*, tai yra operacinės
        sistemos aplinkos kintamieji.

        Plačiau apie tai skaitykite `Vikipedijoje
        <https://en.wikipedia.org/wiki/Environment_variable>`__.

    ADP
        Atvirų duomenų portalas, sudarytas iš atvirų duomenų katalogo ir duomenų
        saugyklos.

    ADK
        Atvirų duomenų katalogas.

    ADS
        Atvirų duomenų saugykla.

    DSA
        Duomenų struktūros aprašas - lentelė, kurioje išsamiai aprašyta tam
        tikro duomenų šaltinio duomenų struktūra.

    ADSA
        :term:`DSA` lentelė, kurioje aprašomi jau atverti ir viešai prieinami
        duomenys.

    ŠDSA
        :term:`DSA` lentelė, kurioje aprašoma neatvertų, :term:`pirminio
        duomenų šaltinio <pirminis duomenų šaltinis>` duomenų struktūra.

    duomenų serializavimo formatas
        Duomenys gali būti serializuojami įvairiais formatais, pavyzdžiui YAML
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

    kanoniniai duomenys
        Kanoniniai duomenys yra tarsi duomenų etalonas, kuris nusako kokios
        duomenų reikšmės yra teisingos. Pavyzdžiui įmonės pavadinimas gali būti
        užrašomas įvairiausiomis formomis, pavyzdžiui:

        ============ =================================
        Įmonės kodas Įmonės pavadinimas
        ============ =================================
        \-           UAB "Duomesta"
        \-           UAB „Duomesta“
        \-           Duomesta
        \-           DUOMESTA
        \-           Uždaroji akcinė bendrovė Duomesta
        \-           Duomesta, UAB
        \-           DSTA UAB
        ============ =================================

        Jei duomenų rinkinyje nėra pateiktas įmonės registracijos kodas, tada
        unikaliai identifikuoti įmonę yra gan sudėtinga.

        Tačiau turint autoritetingus kanoninius duomenis:

        ============ =================================
        Įmonės kodas Įmones pavadinimas
        ============ =================================
        111111111    UAB "Duomesta"
        ============ =================================

        Užduotis unikaliai identifikuoti įmonę pasidaro paprastesnė. Todėl
        kanoniniai duomenys yra labai svarbūs.

    kodinis pavadinimas
        Pavadinimas, kuriam keliami tam tikri apribojimai. Kodiniame pavadinime
        visos raidės turi būti mažosios, pavadinimo pirma simbolis turi būti
        mažoji lotyniška raidė, o visos sekančios raidės turi būti mažosios
        lotyniškos raidės, skaičiai arba pabraukimo simbolis `_`.

        Kodinis pavadinimas atitinka šią reguliąriąją išraišką:

        .. code-block:: regex

            [a-z][a-z0-9_]*


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
        susietųjų duomenų tinkui kurti (angl. *linked data*).

    sisteminis pavadinimas
        Sisteminis pavadinimas yra naudojamas objektų identifikavimui ir yra
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

    pirminis duomenų šaltinis
        Įstaigos ar kitos organizacijos pagrindinis duomenų šaltinis.

    duomenų rinkinys
        Duomenų grupė charakterizuojanti modelį arba susijusius modelius jų
        savybes ir tarpusavio ryšius. Sąsaja tarp modelių apibrėžiama ne
        reliacinių ryšių prasme, o loginės arba tematinės sąsajos prasme.

        Duomenys neskaidomi į skirtingus duomenų rinkinius, pagal vietos, laiko
        ar kitas savybes.
