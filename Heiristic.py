# ----------------------------
# HEIRISTISKA FUNKCIJA
# ----------------------------
# Heiristiskajai funkcijai ir nepieciešams novērēt koka virsotnes, piešķirt tām vērtības, tā, lai varētu noteikt labāko ceļu.
# Izpētot doto spēli ir secināmi potenciālie:
# - punktu atšķirība starp abiem spēlētajiem
# - XX un OO daudzums, jo tie vairāk dod punktus un mazāk otrs spēlētajs var kaut ko ietekmēt
# Attiecīgi ja pirmais spēlētājs ir tad maksimizējam, ja otrai minimizējam


def heiristiska(virsotne, maksimizetajs):
    # Heiristiskās funkcijas izveide balstoties uz vērtībām:
    # 1. Punktu atšķirība, jo uzvar tas, kuram vairāk punktu un jo vairāk jo labāk
    # 2. Cik ir OO un XX pāri (atkarīgs no spēlētaja), jo piemēram O spēlētajam ir izdevīgāk, ja ir vairāk XX pāri, jo tos var aizstāt un no katra dabūt 2 punktus
    # 3. Cik ir XO un OX pāri (atkarīgs no spēletāja), jo piemēram O spēlētājam ir izdevīgāk ja ir XO pāri, jo var atņem punktu pretiniekam, bet OX nes mīnusus O spēlētājam
    if maksimizetajs == 'P1':
        punktu_atskriba = virsotne.p1 - virsotne.p2
        pozitivi_pari = virsotne.virkne.count('OO')
        paositiva_izmaina = virsotne.virkne.count('XO')
        negativa_izmaina = virsotne.virkne.count('OX')
    else:
        punktu_atskriba = virsotne.p2 - virsotne.p1
        pozitivi_pari = virsotne.virkne.count('XX')
        paositiva_izmaina = virsotne.virkne.count('OX')
        negativa_izmaina = virsotne.virkne.count('XO')

    # Attiecīgi izmantojot šīs vērtības atkarībā no maksimizētāja var aprēķināt "punktus" jeb heirisitsko vertību ar savu koeficientu
    punkti = punktu_atskriba * 4 + pozitivi_pari * 2 + paositiva_izmaina - negativa_izmaina

    # Atgriežam Heiristisko vērtību atpakaļ uz izsaucošo algoritmu
    return punkti