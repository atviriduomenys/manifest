.. default-role:: literal

.. _atvėrimas:

#################
Duomenų atvėrimas
#################

.. image:: /static/zingsnis_4.png

Duomenų atvėrimo žingsnį atlieka ne Teikėjas, o Atvėrėjas - Vyriausybės
įgaliota įstaiga, kuri atsakinga už duomenų atvėrimą.

.. image:: /static/atverimas.png

Sekantys žingsniai yra :ref:`anksčiau aptartų žingsnių <sdsa-gavimas>` tęsinys.

1. :ref:`duomenų-paruošimas`
2. :ref:`duomenų-perdavimas`
3. :ref:`kokybės-ir-konfidencialumo-užtikrinimas`
4. :ref:`duomenų-publikavimas`
5. :ref:`metaduomenų-atnaujinimas`

Priklausomai nuo situacijos, ne visi šie žingsniai yra privalomi, detaliau
apie išimtis yra paaiškinta prie kiekvieno žingsnio.


.. _duomenų-paruošimas:

Duomenų paruošimas atvėrimui
****************************

Administratorius sudaręs infrastruktūros paruošimo sutartį, Duomenų teikėjo
infrastruktūroje įdiegia ir sukonfigūruoja duomenų paruošimo atvėrimui
priemones.


Atvėrimas per VDV IS
====================

Jei duomenys atveriami per VDV IS, tuomet duomenų paruošimas reikalingas tik
tais atvejais, kai VDV IS duomenų jungtis nepalaiko duomenų šaltinio.

Jei VDV IS duomenų jungtis nepalaiko duomenų formato, tuomet duomenys
transformuojami ir pateikiami VDV IS duomenų jungčiai naudojant standartines
priemones.


Atvėrimas naudojant standartines priemones
==========================================

Jei duomenys atveriame ne per VDV IS, tuomet galima naudoti Standartines
priemones, kurių pagalba duomenys bus perduodami tiesiogiai į atvirų duomenų
Saugyklą.

:data:`resource.type` skyriuje galite rasti pilną palaikomų formatų sąrašą.

.. note::
    Net jei duomenų struktūros apraše formatas yra palaikomas, tačiau
    standartinės priemonės, gali nepalaikyti visų specifikacijoje aprašytų
    formatų.

Jei Standartinės priemonės nepalaiko Duomenų šaltinio formato, tuomet
Administratorius turi transformuoti duomenis į tokį formatą, kurį palaiko
Standartinės priemonės.


Nepalaikomų duomenų formatų paruošimas
======================================

Jei standartinės priemonės nepalaiko duomenų šaltinio formato, tuomet duomenų
paruošimui reikia naudoti konkrečiam duomenų šaltiniui pritaikytą
specializuotą sprendimą.

Duomenys turi būti transformuojami į vieną iš formatų, kurį palaiko
standartinės priemonės.


Atvėrimas savo infrastruktūroje
===============================

Jei duomenys publikuojami Duomenų teikėjo infrastruktūroje, tuomet Atvirų
duomenų Kataloge, kiekvieną kartą atnaujinus publikuojamus duomenis, reikia
atnaujinti ir :ref:`publikuojamų duomenų metaduomenis
<distribucijos-metaduomenų-atnaujinimas>`.


.. _duomenų-perdavimas:

Duomenų perdavimas atvėrimui
****************************

Atveriant duomenis per VDV IS, Administratorius, Teikėjo infrastruktūroje
įdiegia ir sukonfigūruoja VDV IS duomenų jungtį. VDV IS duomenų jungtis
kopijuoja duomenis į VDV IS, apibrėžtus duomenų atvėrimo sutartyje, duomenų
struktūros priede.

Toks duomenų perdavimas vyksta nustatytu periodiškumu.


.. _kokybės-ir-konfidencialumo-užtikrinimas:

Duomenų kokybės ir konfidencialumo užtikrinimas
***********************************************

Perkėlus duomenis iš Teikėjo infrastruktūros į VDV IS, naudojantis VDV IS
funkcionalumu užtikrinama duomenų kokybė, atliekamas nuasmeninimas ir
užtikrinamas neatvertinų duomenų konfidencialumas.

Pilnai paruošti atvėrimui duomenys perduodami publikavimui į atvirų duomenų
Saugyklą.


.. _duomenų-publikavimas:

Duomenų publikavimas
********************

Atvirų duomenų Saugykla iš Katalogo gauna ADSA, tokiu būdu Saugykla yra
paruošiama duomenų priėmimui, kurie atitinka ADSA.

Saugykla, duomenis gali gauti vienu iš šių būdų:

- jei duomenys atveriami per VDV IS, tuomet duomenis į Saugyklą PUSH būdu
  perduoda VDV IS,

- jei duomenys į Saugyklą perduodami tiesiogiai, tuomet Saugykla duomenis
  priima tiesiogiai iš Duomenų teikėjo infrastruktūros PUSH būdu, tokiu būdu
  duomenys gali būdu perduodami realiu laiku,

- jei duomenys publikuojami Teikėjo infrastruktūroje arba Kataloge, tuomet
  Saugykla naudojantis ADSA metaduomenis išorėje publikuojamus duomenis
  importuoja PULL būdu, nurodytu periodiškumu.

Saugykla užtikrina, kad perduodami duomenys atitinka ADSA, duomenys atitinka
nurodytus duomenų tipus.

Į Saugyklą patenkantys duomenys saugomi vidinėje bazėje iš kurios
publikuojami per API, įvairiais formatais, realiu laiku, suteikiama galimybė
atsisiųsti duomenis tiek po vieną įrašą, tiek visus vienu kartu.


.. _metaduomenų-atnaujinimas:

Metaduomenų atnaujinimas
************************

:ref:`Pasirašius sutartį <atvėrimo-sutartis>`, Teikėjas perduoda Katalogo API
raktą Atvėrėjui, kuris automatiškai per Katalogo Partnerių API atnaujinam
atvertų duomenų metaduomenis ir po kiekvieno duomenų atnaujinimo siunčia
pranešimą per API į Katalogą apie tai, kad duomenys buvo sėkmingai atnaujinti.

Tokiu būdu Katalogas gali patikrinti, kad duomenys atnaujinami nustatytu
periodiškumu.

Plačiau apie metaduomenų atnaujinimą galite skaityti
:ref:`distribucijos-metaduomenų-atnaujinimas` skyriuje ir `Katalogo Partnerių
API dokumentacijoje`__.

__ https://data.gov.lt/partner/api/1


.. _struktūros-pasikeitimų-valdymas:

Struktūros pasikeitimų valdymas
*******************************

Siekiant užtikrinti atvertų duomenų kokybę, pasikeitimai duomenų struktūroje
turi būti daromi aiškiai apibrėžtu ir kontroliuojamu būdu.

Atvirų duomenų naudotojai, užsiregistravę portale, turi galimybę gauti
pranešimus apie planuojamus duomenų struktūros pasikeitimus. Prieš darant
pakeitimus, kurie yra nesuderinami su anksčiau publikuota duomenų struktūra
(toliau Nesuderinami pakeitimai), duomenų naudotojai turi būti informuojami
prieš 6 mėnesius, kad turėtų pakankamai laiko atsinaujinti savo turimas
integracijas.

Nesuderinami pakeitimai yra:

- anksčiau publikuoto duomenų lauko, modelio ar vardų erdvės pavadinimo
  keitimas,
- anksčiau publikuoto duomenų lauko, modelio ar vardų erdvės panaikinimas,
- anksčiau publikuoto duomenų lauko tipo keitimas,
- anksčiau publikuoto duomenų lauko reikšmių mastelio, vienetų ar formato
  keitimas, nekeičiant duomenų tipo.

Vis šie, su anksčiau publikuota struktūros versija nesuderinami pakeitimai,
galo būti daromi tik įspėjus apie planuojamus pakeitimus, prieš šešis
mėnesius. Pakeitimai gali būti atliekami praėjus 6 mėnesiams nuo įspėjimo.

Naujų vardų erdvių, modelių ar duomenų laukų įtraukimas yra su ankstesne
struktūros versija suderinamas pakeitimas, nereikalaujantis išankstinio
įspėjimo.

Duomenų naudotojų informavimas apie struktūros ar duomenų pasikeitimus
darotas atvirų duomenų Kataloge, pateikiant naują duomenų struktūros versiją,
kurioje pažymėta, kas keičiasi, nurodant datą 6 mėnesius į priekį. Įkėlus
tokį duomenų struktūros aprašą, Kataloge užsiregistravę duomenų naudotojai
bus automatiška informuojami apie planuojamus struktūros pasikeitimus,
nurodant data į priekį, kada jie įsigalios.

Apie struktūros pasikeitimų žymėjimą skaitykite skyriuje
:ref:`struktūros-keitimas`.
