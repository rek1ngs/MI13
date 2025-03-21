# ----------------------------
# HEIRISTISKA FUNKCIJA
# ----------------------------
# Heiristiskajai funkcijai ir nepieciešams novērēt koka virsotnes, piešķirt tām vērtības, tā, lai varētu noteikt labāko ceļu.
# Izpētot doto spēli ir secināmi potenciālie:
# - punktu atšķirība starp abiem spēlētajiem
# - XX un OO daudzums, jo tie vairāk dod punktus un mazāk otrs spēlētajs var kaut ko ietekmēt
# Attiecīgi ja pirmais spēlētājs ir tad maksimizējam, ja otrai minimizējam

def heiristiska(virsotne, maksimizetajs):
    # 1. Punktu atšķirība, jo lielāka, jo labāka
    if maksimizetajs == 'P1':  # If PC is P1
        punktu_atskriba = virsotne.p1 - virsotne.p2
        pozitivi_pari = virsotne.virkne.count('OO')
        paositiva_izmaina = virsotne.virkne.count('XO')
        negativa_izmaina = virsotne.virkne.count('OX')
    else:  # If PC is P2
        punktu_atskriba = virsotne.p2 - virsotne.p1
        pozitivi_pari = virsotne.virkne.count('XX')
        paositiva_izmaina = virsotne.virkne.count('OX')
        negativa_izmaina = virsotne.virkne.count('XO')

    # Calculate points combining all aspects
    punkti = punktu_atskriba * 4 + pozitivi_pari * 2 + paositiva_izmaina - negativa_izmaina

    return punkti