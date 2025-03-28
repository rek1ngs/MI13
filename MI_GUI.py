# ----------------------------
# Informācijas avots Python un PySimpleGUI
# https://www.w3schools.com/python/
# https://docs.pysimplegui.com/en/latest/
# ----------------------------



# ----------------------------
# KODA SAGATAVOŠANA | IMPORTI
# ----------------------------
import PySimpleGUI as sg



# ----------------------------
# SPĒLES "DATUBĀZE" | IESTATĪJUMI
# ----------------------------
#PySimpleGUI iestatījumi
sg.theme("DarkBlack")
sg.set_options(font=('Arial Bold', 16))






# ----------------------------
# LOGS "OPCIJAS" | FUNCKIJA
# ----------------------------
#Funckija, kas tiek izsaukta no Main.py palaišanas brīdī, lai atvērtu spēles opciju izvēles logu.
def opcijas_logs():

    #Tiek definētas visas opcijas, ja grib izņem kādu opciju, vienkārši izdzēš no šejienes
    speletaju_opcijas = ['Cilvēks', 'Dators']
    algoritma_opcijas = ['Minimaksa', 'Alfa-beta']

    # Šī koda daļa izveido izkārtojumu izmantotjot PySimpleGUI:
    #- sg.Text ir virsraksti
    #- sg.Button poga(nosaukums, atslēga)
    #- sg.Combo ir dropdown menu, kurā ieliek visas spēlētāju opcijas, uzstāde defaul value un iedot atslēgu
    #- sg.Slider ir slideris, kur var izvēlēties ģenerējamās virknes garumu
    # P.S. Atslēgas nozīme ir, lai mēs varētu ar loop checkot un iegūt value un piesaistīt
    opciju_izkartojums = [
        [sg.Text("Šī ir spēle ar X un O"), sg.Push(), sg.Button("Sākt spēli", key="-SAKT-")],
        [sg.HorizontalSeparator()],
        [sg.Text('Ievadiet virknes garumu:'), sg.Slider((15,25), orientation = 'horizontal', key = '-VIRKNE-')],
        [sg.VPush()],
        [sg.Text('Izvēlēties, kurš uzsāk spēli:'), sg.Combo(speletaju_opcijas, default_value=speletaju_opcijas[0], key='-SPELETAJS-')],
        [sg.VPush()],
        [sg.Text('Izvēlēties, kuru algoritmu izmantos dators:'), sg.Combo(algoritma_opcijas, default_value=algoritma_opcijas[0], key='-ALGORITMS-')],
    ]

    #Izveido opciju logu, kurā ir nosaukums un tiek ievadīts opciju_izkartojums izkārtojums
    opciju_logs = sg.Window('Spēle X un O', opciju_izkartojums)

    #While cikls, kurā mēs kāmēr true lasam event un values. 
    #Ja event ir WINDOWS.CLOSED, tas nozīmē, ka logs ir aizvēts un spēle tiek beigta ar exit()
    #Ja event ir "-SAKT-", kas ir pogas KEY value un tiek izsaukts, kad nospiež pogu, tad tiek aizvērts logs un tiek atgrieztas izvēlētas vērtības
    while True:
        event, values = opciju_logs.read()
        if event == sg.WINDOW_CLOSED:
            opciju_logs.close()
            exit()
        elif event == "-SAKT-":
            opciju_logs.close()
            return values









# ----------------------------
# LOGS "SPĒLE" | FUNCKIJA
# ----------------------------

#Funckija, kas tiek izsaukta no Main.py pēc opciju iestatīšanas
#- VirkneString - Sākuma virkne
#- Symbol - spēlētaja simbols, lai zinātu kurus gājienus var veikt
#- GajienaVeicejs - spēlētājs, kuram ir tagad jāveic gājiens
def galvenais_logs(VirkneString, SpeletajaSimbols, GajienaVeicejs):

    #Sagatavojam pogas atkarībā no šobrīdējā spēletaja (jo, kad būs datora gājiens spelētājs redzēs datora izmaiņas un varēs turpinat kad vēlēsies)
    if GajienaVeicejs == "Dators":
        Poga = sg.Button("Turpināt", key="-B4-")
    else:
        Poga = sg.Button("Izdarīt gājienu", key="-B2-")


    #Šis izveidot izkārtojumu izmantotjot PySimpleGUI:
    #- sg.Text ir virsraksti
    #- sg.Button poga(nosaukums, atslēga)
    #- sg.ImputText ir teksta lodziņš, kurā (readonly_for_disable nozīmē, ka nav grayed out, bet nevar editot) (enable_events izslēdz opciju izpildīt eventus) (disabled neatļauj editot) (justification ir centrēšana 'c')
    galvenais_izkartojums = [
        [sg.Text("Šī ir spēle ar X un O")],
        [sg.Push(), sg.InputText(default_text=VirkneString, use_readonly_for_disable = True, enable_events = False, disabled = True, key = "-IN1-", background_color = "white", text_color = "black", justification = 'c'), sg.Push()], #šaja - InputText - ievietos X un O rindu, varēs iezīmēt
        [Poga, sg.Push(), sg.Button("Aizvērt", key = "-B3-")],
        [sg.Text(f"Gājienu tagad jāveic: {GajienaVeicejs} {SpeletajaSimbols}"), sg.Multiline(f"Iespējamie gājieni:\nX: 'OO' -> 'X', 'OX' -> 'X'\nO: 'XX' -> 'O', 'XO' -> 'O'", size = (20,3), disabled = True)],
    ]

    #Izveidojam speles logu
    window1 = sg.Window("Spēles logs", galvenais_izkartojums)

    # While cikls, kas lasa šī loga vērtības
    while True:
        #Nolasa loga vērtības un eventus
        event, values = window1.read()

        #Ja events ir WINDOW_CLOSED vai "-B3-" (AIZVĒRT), tad tiek aizvērts logs un atgriezts FALSE
        if event == sg.WINDOW_CLOSED or event == "-B3-":
            window1.close()
            return False
        
        # Ja nospiež "Veikt gājienu" tiek nokopēts gājiens un nosūtīts uz main.py
        if event == "-B2-": 
            # Izsaukta funkcija, kas definēta nedaudz zemāk, ja tiek atgriezta pareiza vērtība, tad mēs paņemam no sistēmas clipboard, aizveram logu un atgriežam izmainīto virkni
            if (CopySymbol(SpeletajaSimbols, window1) == True):
                Copied = window1.TKroot.clipboard_get()
                print(Copied)
                window1.close()
                return Copied

        # Ja nospiež "Turpināt", kad ir datora gājiens, tad aizver logu un izsauc spēles turpināšanu.
        if event == "-B4-":
            window1.close()
            return True








# ----------------------------
# GĀJIENA PĀRBAUDE | FUNCKIJA
# ----------------------------

# !!!!!!!!!!!!!!!!!!!!!!
# Modificēts no (OpenAI. ChatGPT https://chatgtp.com/)
# !!!!!!!!!!!!!!!!!!!!!!

#Funkcija kas nodrošina iezīmēto simbolu kopēšanu un apstrādi izvadot gala virkni (ja varēja veikt to gājienu)
def CopySymbol(SpeletajaSimbols, window1):
    #Mēģina atrast ievades logu ar atslēgu -IN1- un tad iegūst iezīmēto tekstu
    try:
        InputWidget = window1["-IN1-"].Widget
        SelectedText = InputWidget.selection_get()
    except:
        sg.popup("Lūdzu, iezīmē simbolus!")
        return False

    #Pārbauda vai ir izvēlēti divi simboli
    if len(SelectedText) != 2:
        sg.popup("Lūdzu, izvēlieties tieši divus simbolus!")
        return False

    #Iespējamie gājieni spelētajiem
    iespejas = {
        'X': {'OO': 'X', 'OX': 'X'},
        'O': {'XX': 'O', 'XO': 'O'}
    }

    #Saņemam iespējamos gājienu spēlētajam (datoram šeit nav tik svarīgi)
    iespejamie_gajieni = iespejas.get(SpeletajaSimbols, {})

    #Pārbaudam vai veiktais gājiens ir šajā sarakstā
    if SelectedText in iespejamie_gajieni:
        jaunais_simbols = iespejamie_gajieni[SelectedText]

        #Atrod sākumu un beigu elementu (indeksu) šajā Widget
        start = InputWidget.index("sel.first")
        end = InputWidget.index("sel.last")

        #Aizstājam šos divus simbolus ar jauno simbolu
        jauna_virkne = window1['-IN1-'].get()[:start] + jaunais_simbols + window1['-IN1-'].get()[end:]

        #Izdzēs sistēmas clipobordu (idejiski līdzīgi CTRL+C), pievieno atzīmēto tekstu un updeito, lai automātiski tiktu atjaunināts
        window1.TKroot.clipboard_clear()
        window1.TKroot.clipboard_append(jauna_virkne)
        window1.TKroot.update()
        return True
    
    else:
        #Attiecīgi ja nav pareiz gājiens, tad ir popup ar paziņojumu
        sg.popup("Nevar veikt šādu gājienu. Mēģiniet vēlreiz!")
        return False
    









# ----------------------------
# LOGS "BEIGAS" | FUNCKIJA
# ----------------------------
#Funckija, kas tiek izsaukta no Main.py - spēles beigās
def beigu_logs(Uzvaretajs, Speletajs, Dators):

    #Šis izveidot izkārtojumu izmantotjot PySimpleGUI:
    #- sg.Text ir virsraksti
    #- sg.Button poga(nosaukums, atslēga)
    #P.S. Atslēgas nozīme ir, lai mēs varētu ar loop checkot un iegūt value un piesaistīt
    beigu_izkartojums = [
        [sg.Text("Šī ir spēle ar X un O"), sg.Push(), sg.Button("Spēlēt vēlreiz", key="-VELREIZ-")],
        [sg.HorizontalSeparator()],
        [sg.Text(f"Uzvarēja: {Uzvaretajs}")],
        [sg.Text(f"Cilvēka punkti: {Speletajs}")],
        [sg.Text(f"Datora punkti: {Dators}")],
    ]

    #Izveido beigu logu, kurā ir nosaukums un tiek ievadīts beigu_izkartojums izkārtojums
    beigas_logs = sg.Window('Spēle X un O', beigu_izkartojums)

    #While cikls, kurā mēs, kāmēr true lasām event un values. 
    #Ja event ir WINDOWS.CLOSED, tas nozīmē, ka logs ir aizvēts un spēle tiek beigta ar exit()
    #Ja event ir "-VELREIZ-", kas ir pogas KEY value un tiek izsaukts, kad nospiež pogu, tad tiek aizvērts logs un atgriezta true vērtība, kas nozīmē, ka grib spēlēt vēlreiz
    while True:
        event, values = beigas_logs.read()
        if event == sg.WINDOW_CLOSED:
            beigas_logs.close()
            exit()
        elif event == "-VELREIZ-":
            beigas_logs.close()
            return True
