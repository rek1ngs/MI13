import PySimpleGUI as sg
import random

sg.theme("DarkBlack")
sg.set_options(font=('Arial Bold', 16))

layout1 = [
    [sg.Text("Šī ir spēle ar X un O"), sg.Push(), sg.Button("Sākt spēli", key = "-B1-")],
    [sg.InputText(use_readonly_for_disable = True, enable_events = False, disabled = True, key = "-IN1-", background_color = "white", text_color = "black", justification = 'c')], #šaja - InputText - ievietos X un O rindu, varēs iezīmēt
    [sg.Button("Izdarīt gājienu", key = "-B2-"), sg.Push(), sg.Button("Aizvērt", key = "-B3-")]
]

def CopySymbol():
    InputWidget = window1["-IN1-"].Widget
    SelectedText = InputWidget.selection_get()
    window1.TKroot.clipboard_clear()
    window1.TKroot.clipboard_append(SelectedText)
    window1.TKroot.update() # Izveidots ar čata palīdzību

Virkne = []
VirknesGarums = random.randint(15,25)
print(VirknesGarums)
    
for x in range(0, VirknesGarums):
    Simbols = random.randint(0,1)

    if Simbols == 0:
        Virkne.append('X')
    else:
        Virkne.append('O')

VirkneString = ''.join(Virkne)
print(VirkneString)

window1 = sg.Window("Spēles logs", layout1)

while True:
    event, values = window1.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-B1-": # Sāk spēli, displayo simbolu virkni
        window1["-IN1-"].update(VirkneString)
    
    if event == "-B2-": 
        CopySymbol()
        Copied = window1.TKroot.clipboard_get()
        print(Copied)

    if event == "-B3-":
        break

window1.close()
