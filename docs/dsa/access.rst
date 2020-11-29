.. default-role:: literal
.. _prieigos-lygiai:

Prieigos lygiai
===============

Duomenų prieigos lygis nurodomas :data:`access` stulpelyje.

.. describe:: access

    .. describe:: private

        **Vidiniam naudojimui**

        Duomenys skirti tik vidiniam konkrečios sistemos naudojimui.

    .. describe:: protected

        **Pakartotiniam naudojimui**

        Duomenys gali būti naudojami integracijai su išorinėmis sistemomis.

    .. describe:: public

        **Viešam naudojimui**

        Duomenys skirti viešam naudojimui, tačiau duomenų panaudojimo tikslai
        ribojami.

    .. describe:: open

        **Atviram naudojimui**

        Duomenys skirti viešam naudojimui, neribojant panaudojimo tikslo.


Viešam pakartotiniam naudojimui gali būti teikiami tik `public` ir `open`
prieigos lygio duomenys.

`public` duomenys gali būti teikiami tik autorizuotiems duomenų valdytojams,
kurie yra susipažinę ir sutinka su duomenų naudojimo taisyklėmis ir naudoja
duomenis tik `nurodytu tikslu`__ (*purpose limitation*), laikosi BDAR_
reikalavimų.
Asmens duomenys gali būti viešinami tik public ar žemesniu prieigos lygiu.

.. __: https://gdpr-info.eu/art-5-gdpr/
.. _BDAR: https://gdpr-info.eu/

`open` duomenys turėtu būti teikiami atvirai be jokios autorizacijos ir
neribojant duomenų naudojimo tikslo. Asmens duomenys negali būti teikiami `open`
prieigos lygiu.

Prieigos lygiai gali būti paveldimi iš aukštesneės dimensijos. Tačiau žemesnė
dimensija apsprendžia realų prieigos lygį. Pavyzdžiui jei :data:`dataset.access`
yra `private`, o toje :data:`dataset` dimensijoje esantis :data:`property` yra
`open`, tada visos to :data:`property` aukštesnės dimensijos taip pat tampa
`open`, nors visos kitos dimensijos yra `private`, nes paveldi
:data:`dataset.access` reikšmę.
