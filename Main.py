#pip3 install PySimpleGUI
#python3 Main.py

# ----------------------------
# KODA SAGATAVOŠANA | IMPORTI
# ----------------------------
import Tree_Generation #Python kods koka ģenerēšanai
import MI_GUI #Python kods GUI īstenošanai
import Algorithms #Python kods Algoritmiem
import random #Bibliotēka, kas ļaus ģenerēt nejaušas virknes
import os #Bibliotēka, kas ļauj ietekmēt sistēmas mainīgos
import sys #Bibliotēka, kas ļauj ietekmēt Pythona vidi pārtraukt kodu utml.




# ----------------------------
# SPĒLES "DATUBĀZE" | MAINĪGIE
# ----------------------------
izmantotais_algoritms = None #Šeit tiks saglabāts pēc izvēles izmantojamais algoritms
speletajs_1 = None #Šeit tiks saglabāts pirmais spēlētājs 'Dators' vai 'Cilvēks'
speletajs_2 = None #Šeit tiks saglabāts otrais spēlētājs 'Dators' vai 'Cilvēks'
sobrideja_virkne = None #Šeit tiks saglabāta pašreizējā stāvokļa virkne
nakosais_gajiens = None #Šeit tiks saglabāts, kam ir nākošais gājiens 'Dators' vai 'Cilvēks'
speles_koks = None #Šeit tiks saglabāts spēles koks
izveleta_virsotne = None #Šeit tiks saglabāta pēdējā izvēlētā virsotne, no kuras tiks tālāk ģenerēts koks
maksimizetajs = None




# ----------------------------
# SPĒLES "DATUBĀZE" | IESTATĪJUMI
# ----------------------------
automatiski_genereta = True #Vai ģenerēt virkni vai arī izmantot statiski ievadītu
statiska_virkne = 'XOOXXO' #Statiskā virkne, kas tiks izvēlēta, ja tiks izslēgta automātiskās ģenerēšanas funkcija
dzilums = 4 #Šis norāda cik dziļi koks ģenerēs virsotnes, ņemot verā, ka resursu nav pietiekami, lai visu koku ģenerētu
izvadit = True #Vai pēc katra gājiena izvadīt daļējo koku terminālī?









# ----------------------------
# GALVENAIS | SPĒLES LOĢIKA
# ----------------------------

# 1 | SPĒLES UZSĀKŠANA
# Spēli uzsākot tiek izsaukts no MI_GUI.py opciju izvēles logs un sagaidam atbildi
iestatijumi = MI_GUI.opcijas_logs() #Tiek izsaukts opciju logs, turpinājumu meklēt MI_GUI zem funckiajs opcijas_logs, pēc tā sasglabā iestatījumus mainīgajā iestatijumi
izmantotais_algoritms = iestatijumi['-ALGORITMS-'] #Tālāk no mainīgā iestatijumi tiek izvlikts izvēlētais algoritms (saglabā "datubāzē" vēlākai lietošanai)
speletajs_1 = iestatijumi['-SPELETAJS-'] #Tālāk no mainīgā iestatijumi tiek izvlikts izvēlētais primais spēlētājs (saglabā "datubāzē" vēlākai lietošanai)
nakosais_gajiens = speletajs_1 #Uzstādam, ka pirmais gājiens būs arī pirmajam spēlētajam
length = int(iestatijumi['-VIRKNE-']) #Spēlētāja iestatītais virknes garums

#Attiecīgi uzstādām pēc loģikas otro spēlētāju
if speletajs_1 == 'Dators':
    speletajs_2 = 'Cilvēks'
    maksimizetajs = 'P1'
else:
    speletajs_2 = 'Dators'
    maksimizetajs = 'P2'

#Izvade pārbaudēm:
# print(izmantotais_algoritms)
# print(speletajs_1)
# print(speletajs_2)






# 2 | SAGATAVOŠANĀS SPĒLEI
# Kad saņemta atbilde, tad mēs sagatavojamies spēlei
# 2.1 | Tiek ģenerēta nejauša virkne, ja automātiskā ģenerēšana ir ieslēgta
if automatiski_genereta == True:
    sobrideja_virkne = ''.join(random.choices('XO' , k = length)) # Attiecīgi no izvēlēm "XO" izvēlēsies k skaitu, ko savienos ar join.
else:
    sobrideja_virkne = statiska_virkne # Savādāk, ja automatiskā ģenerēšana ir izslēgta, tad mēs šobrīdējo virkni uzstādam statisko virkni, kas definēta iestatījumos

speles_koks = Tree_Generation.Speles_koks() # No Tree_Generation faila Speles_koks() izveidojam jaunu objektu, ko saglabājam mainīgajā vēlākai lietošanai
izveleta_virsotne = Tree_Generation.Virsotne('A1', sobrideja_virkne, 0, 0, 0) # Tālāk mēs uzstādam pirmo izvēlēto virsotni, kurā norādām (ID, VIRKNI, SP1-PUNKTI, SP2-PUNKTI, LIMENIS)

statuss = Tree_Generation.generet_koku(speles_koks, izveleta_virsotne, dzilums, izvadit) # Attiecīgi izsaucam no Tree_Generation funkciju generet_koku, kurā ievadam (izvadīt ir printēt), kas atgriež stāvokli
if statuss:
    print("Nav vairs atrasti gājieni") #Ja statuss ir True, tas nozīmē, ka netika atrasts neviens iespējamais gājiens, kas nozīmē, ka spēle beidzas
    sys.exit() #Iziet no koda un beidz
else:
    print("Atrasti gājieni - turpinam") #Ja tika atrasts kāds gājiens, tad tiek turpināts ar kodu un izvadīts paziņojums






# 2.2 | SPĒLES GALVENAIS CIKLS
# Cikls, kas tiek izpildīs visu spēles gaitu
while True:
    
    #Izvade pārbaudei 
    print(nakosais_gajiens)
    print(sobrideja_virkne)



    ####################################
    ############   CILVĒKS #############
    ####################################
    #Pārbaudām vai nākošais gājiens ir cilvēkam
    if nakosais_gajiens == 'Cilvēks':
        #Uzstādam spēletaja, kas iet, simbolu (O vai X)
        if nakosais_gajiens == speletajs_1:
            speletaja_simbols = 'O'
        else:
            speletaja_simbols = 'X'

        #Izsaucam no MI_GUI.py funckiju galvenais_logs(), kas ir galvenais spēles logs, kur ievadām šobrīdējo virkni, spēlētaja simbolu (kas spēlē X vai O vajadzīgs, lai pārbaudītu gajienu) un kuram spēlētajam tagad ir jāiet
        virkne = MI_GUI.galvenais_logs(sobrideja_virkne, speletaja_simbols, nakosais_gajiens)

        #Ja atgriež false spēli beizās
        if virkne == False:
            print(virkne)
            print("Kļūda vai spēle beiga")
            break

        #Ja tiek atgrizta virkne, tad tiek veikta virsotnes meklēšana no koka un sagatavots gājiens otram, ģenerējot jaunu koku
        else:
            izveleta_virsotne = Tree_Generation.atrast_virsotni(speles_koks, virkne, izveleta_virsotne) #Meklē virsotni no funkcijas, kas definēta Tree_Generation
            print(izveleta_virsotne.virkne) 
            sobrideja_virkne = virkne #Uzstāda šobrīdējo_virkni uz izvēlēto virkni
            nakosais_gajiens = 'Dators' #Uzstāda, ka nākošais gājiens būs jāveic datoram

            #Ja tika atrasta virsotne kokā
            if izveleta_virsotne:
                value = Tree_Generation.generet_koku(speles_koks, izveleta_virsotne, dzilums, izvadit) #Tiek ģenerēts jauns koks no šīs izvēlētās virsotnes
                # Ja funckija atgirež true, tas nozīmē, ka netika atrasts neviens vairs gājiens, ko var veikt.
                if value:
                    print("Netika atrasti vairs gājieni")
                    break
                else:
                    print("Tika atrasti iespējami gājieni")



    ####################################
    ############  DATORS  ##############
    ####################################
    #Pārbaudām vai nākošais gājiens ir datoram
    elif nakosais_gajiens == 'Dators':

        #Uzstādam spēletajam, kuram tagad gājiens, simbolu
        if nakosais_gajiens == speletajs_1:
            speletaja_simbols = 'O'
        else:
            speletaja_simbols = 'X'

        #Izsaucam MI_GUI.py funckiju galvenais_logs(), kas ir spēles logs.
        #Ievadām iekšā sobrīdējo virkni, šobrīdeja spēlētāja simbolu (lai varam pārbaudīt gājienu un pašu spēlētaju, kam ir gajiens 'cilvēks' vai 'dators')
        virkne = MI_GUI.galvenais_logs(sobrideja_virkne, speletaja_simbols, nakosais_gajiens)

        #Ja atgriež false tas nozīmē vai spēli beizās
        if virkne == False:
            print(virkne)
            print("Kļūda vai spēle beiga")
            break

        #Ja atgriež True, tas nozīmē, ka spēlētajs velas turpināt spēli
        elif virkne == True:
            print("Turpināt spēli")

            #Atkarībā no algoritma izsaucam pareizo funckiju
            if izmantotais_algoritms == 'Minimaksa':
                vertiba, izveleta_virsotne = Algorithms.minimax(izveleta_virsotne, dzilums, speles_koks, True, maksimizetajs) #Izmantojot minimax algoritmu tiek atrasta nākošā labākā virsotne
            else:
                vertiba, izveleta_virsotne = Algorithms.alpha_beta_pruning(izveleta_virsotne, dzilums, float('-inf'), float('inf'), speles_koks, True, maksimizetajs)  #Izmantojot Alpha-Beta algotritmu atrodam nākošo labāko visotni

            #Apstrādājam iegūto vērtību, iegustam virkni, lai varam attēlot un uzstādām nākoso gājienu
            sobrideja_virkne = izveleta_virsotne.virkne #Uzstāda šobrīdējo_virkni uz izvēlēto virkni
            nakosais_gajiens = 'Cilvēks' #Uzstāda, ka nākošais gājiens būs jāveic datoram

            #Ja tika atrasta virsotne kokā
            if izveleta_virsotne:
                value = Tree_Generation.generet_koku(speles_koks, izveleta_virsotne, dzilums, izvadit) #Tiek ģenerēts jauns koks no šīs izvēlētās virsotnes
                # Ja funckija atgirež true, tas nozīmē, ka netika atrasts neviens vairs gājiens, ko var veikt.
                if value:
                    print("Netika atrasti vairs gājieni")
                    break
                else:
                    print("Tika atrasti iespējami gājieni")






# 3 | SPĒLES BEIGAS
# Šajā daļā tiek sagatavoti un izvadīti rezultāti

#Iegūstam punktu skaitus no pēdējās virsotnes
p1 = izveleta_virsotne.p1
p2 = izveleta_virsotne.p2

#Nosakām uzvarētāju balstoties uz punktiem
if p1 == p2:
    uzvaretajs = "Neizšķirts"
elif p1 > p2:
    uzvaretajs = speletajs_1
elif p1 < p2:
    uzvaretajs = speletajs_2

# Uzstādām katram spēlētājam viņam atbilstošo punktu skaitu
if speletajs_1 == 'Cilvēks':
    speletajs = p1
    dators = p2
else:
    speletajs = p2
    dators = p1

# Attiecīgi izsaucam MI_GUI funkciju, kas atver beigu logu un parāda datus
value = MI_GUI.beigu_logs(uzvaretajs, speletajs, dators)

# Ja atgriež true, tas nozīmē, ka spēlētajs nospieda pogu "Spēlēt vēlreiz", tad notiek koda restartēšana
if value == True:
    os.execl(sys.executable, sys.executable, *sys.argv) #https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/