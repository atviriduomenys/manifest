.. _ryšiai:

Ryšiai tarp modelių
###################

Pats ryšys pateikiamas :data:`property.ref` stulpelyje. :data:`property.ref`
stulpelyje ryšį su modeliu galima nurodyti tokiais būdais:

.. describe:: property.ref

    .. describe:: model

        `model` nurodo kito :data:`model` pavadinimą kurio :data:`model.ref`
        siejamas su :data:`property`.

        Jei :data:`model.ref` pirminiam raktui naudoja daugiau nei vieną lauką,
        tada :data:`property.source` laukas turi būti tuščias, o
        :data:`property.prepare` turi būti pateikiamos kableliu atskirtos
        property reikšmės, kurios bus naudojamos susiejimui.

    .. describe:: model[property]

        Tais atvejais, kai :data:`property` duomenys nesutampa su siejamo
        :data:`model.ref,` galima nurodyti :data:`property` iš :data:`model.`

    .. describe:: model[*property]

        Jei susiejimui reikia daugiau nei vieno duomenų lauko ir jie nesutampa
        su model.ref, tada galima nurodyti kelias property reikšmes atskirtas
        kableliu. Tačiau šiuo atveju taip pat būtina nurodyti ir
        :data:`property.prepare` kelias reikšmes atskirtas kableliu, o
        :data:`property.source` reikšmė turi būti tuščia.
        :data:`property.prepare` stulpelyje nurodomi kiti modelio
        :data:`property` pavadinimai iš kurių duomenų reikšmių turi būti
        formuojamas sudėtinis raktas.
