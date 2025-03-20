# KODA PAMATS (DATU STRUKTURA UN KOKA GENERESANA) -  2.2.TĒMA: SPĒLES KOKS - STĀVOKĻU TELPAS GRAFA PIELIETOJUMS



# ----------------------------
# KOKS | KLAŠU DEFINĒŠANA
# ----------------------------

# Klase, kas atbilst vienai virsotnei spēles kokā
class Virsotne:
    
    #Klases konstruktors, kas izveido virsotnes eksemplāru
    #Katrā virsotnes eksmeplārā glabājas virsotnes unikāls identifikators (id), skaitliskā virkne (virkne)
    #pirmā spēlētāja punkti (p1), otrā spēlētāja punkti(p2), un virsotnes atrašanās līmeņa numurs
    #Glabātie dati tiek padoti kā konstruktora argumenti
    def __init__(self, id, virkne, p1, p2, limenis):
        self.id=id
        self.virkne=virkne
        self.p1=p1
        self.p2=p2
        self.limenis=limenis


#Klase, kas atbilst spēles kokam        
class Speles_koks:
    
    #Klases konstruktors, kas izveido spēles koka eksemplāru
    #Spēles koka eksemplārs ietver sevī virsotņu kopu, kas tiek veidota kā Python saraksts un
    #loku kopu, kas tiek veidota kā Python vārdnīca (dictionary)
    #Gan virsotņu kopa, gan loku kopa sākotnējie ir tukšas
    #Virsotņu kopā glabāsies virsotnes viena aiz otras
    #Loku kopā glabāsies virsotnes unikāls identifikators kā vārdnīcas atslēga (key) un
    #ar konkrētu virsotni citu saistītu virsotņu unikālie identifikatori kā vērtības (values)
    def __init__(self):
        self.virsotnu_kopa=[]
        self.loku_kopa=dict()
    
    #Klases Speles_koks metode, kas pievieno spēles kokam jaunu virsotni, kuru saņem kā argumentu
    def pievienot_virsotni(self, Virsotne):
        self.virsotnu_kopa.append(Virsotne)
        
    #Klases Speles_koks metode, kura papildina loku kopu, saņemot kā argumentus
    #virsotnes identifikatoru, no kuras loks iziet, un virsotnes identifikatoru, kurā loks ieiet
    def pievienot_loku(self, sakumvirsotne_id, beiguvirsotne_id):
        self.loku_kopa[sakumvirsotne_id]=self.loku_kopa.get(sakumvirsotne_id,[])+[beiguvirsotne_id]


    #Iztira visu speles koku
    def clear(self):
        self.virsotnu_kopa = []
        self.loku_kopa = dict()









# ----------------------------
# KOKS | GĀJIENU PĀRBAUDE UN PATI ĢENERĒŠANA
# ----------------------------

#mainīgais, kurš skaita virsotnes
j=2

#Funkcija, kas atbilstoši veiktajam gājienam iegūst jaunu spēles koka virsotni un
#papildina speles koka virsotņu kopu un loku kopu
#Funkcija kā argumentus saņem spēles koku, saģenerētās virsotnes un pašreizējo virsotni
def gajiena_parbaude(sp, generetas_virsotnes, pasreizeja_virsotne):

    global j #Definē, globālos mainīgos, j ir kurš skaita virsonts
    global turpinat_speli #Definē globālo mainīgo, kas paredzēts vai spēle var turpināt

    #Tiek noteiktas visas iespējamās darbības
    # Spēlētajs X var mainit OO uz X un OX uz X
    # Spēlētājs O var mainīt XX uz O un XO uz O
    iespejas = {
        'X': {'1': ('OO', 'X'), '2': ('OX', 'X')},
        'O': {'1': ('XX', 'O'), '2': ('XO', 'O')}
    }

    #Mainīgais, kas paredzēts, lai pārbītu vai gājiens ir izdarīts visā iterācijā
    gajiens_izdarits = False

    #Veic no iespējamajiem gājieniem OO un tadXX vai  OX/XO variantu (atkarībā no spēlētaja)
    for gajiena_tips in ['1', '2']:
        # Nosaka spēlētaja kārtu balstoties uz līmeni (pāra vai nepara skaitlis), bet sāk spēlētajs O
        speletajs = 'O' if pasreizeja_virsotne.limenis % 2 == 0 else 'X'

        #Uzstādam tipu un tā aizstājēju balstoties no iespējām, spēlētāja un tipa (šeit tiek ņemts no iepriekš definētajām iespējām)
        mainamais, mainitajs = iespejas[speletajs][gajiena_tips]

        #Iegūstam pašreizējo virkni un nosakām to garumu (lai varētu zināt cik ilgi mums ir jāpārbauda simboli virknē)
        virkne = pasreizeja_virsotne.virkne
        length = len(virkne)

        #Iniciējam While funkciju
        i = 0
        while i <= length and length > 1: #Kāmēr garums nepārsniedz i un kāmēr garums ir lielaks par vienu simbolu
            # Pārbaudam vai esošais un nākošais elements sakrīt ar mainamo
            current_pattern = virkne[i:i+2]
            print(current_pattern)
            if current_pattern == mainamais:
                # Ja sakrīt, tad aizstāj un iegūst jauno virkni [sakums:beigas] (+2 jo 2 neieskaita, tapec bus 2 simboli nevis 3)
                jauna_virkne = virkne[:i] + mainitajs + virkne[i+2:]
                #Uzstāda jaunos punktu skaitus
                jauns_p1 = pasreizeja_virsotne.p1 + (2 if speletajs == 'O' and gajiena_tips == '1' else -1 if speletajs == 'X' and gajiena_tips == '2' else 0)
                jauns_p2 = pasreizeja_virsotne.p2 + (2 if speletajs == 'X' and gajiena_tips == '1' else -1 if speletajs == 'O' and gajiena_tips == '2' else 0)
                #Uzstāda nākošo līmeni
                jauns_limenis = pasreizeja_virsotne.limenis + 1
                #Piešķir jaunu virsotne id
                jauns_id = 'A' + str(j)
                #Palielina virsotnes skaitu virsotnes
                j += 1
                #Izveido jaunas virsotnes caur klasi un pievieno lokus
                jauna_virsotne = Virsotne(jauns_id, jauna_virkne, jauns_p1, jauns_p2, jauns_limenis)
                sp.pievienot_virsotni(jauna_virsotne)
                #Pievieno generēto virsotņu sarakstam jauno virsotni
                generetas_virsotnes.append(jauna_virsotne)
                sp.pievienot_loku(pasreizeja_virsotne.id, jauns_id)
                #Atzīmē, ka gājiens ir izdarīts
                gajiens_izdarits = True
            
            #Atzīmē, ka aplis iziets un var veikt nākošā mainīgā pārbaudi
            i += 1

    #Ja gājiens nav izdarīts, tad mēs neturpinam spēli un atgriežam False
    if gajiens_izdarits == False:
        turpinat_speli = False
        return False
    else:
        return True







# ----------------------------
# KOKS | FUNKCIJA, KAS INICIĒS KOKA ĢENERĒŠANU
# ----------------------------
# Izvada visu koku, kas ir ģenerēts noteiktam dziļumam
# Funkcijā ievada spēles koku, izvēlēto virsotni, dziļumu (iestatījumi) un vai izdrukāt visu koku (iestatījumi)
def generet_koku(speles_koks, virsotne, dzilums, drukat):

    #Notīram iepriekšējo koku un pievienojam tukšajam kokam iepriekšējo izvēlēto virsotni
    speles_koks.clear()
    speles_koks.pievienot_virsotni(virsotne)
    sobridejas_virsotnes = [virsotne]

    # Kamēr nav apskatītas visas saģenerētas virsotnes viena pēc otras
    for i in range(dzilums):
        nakosa_limena_virsotnes = [] #Tiks saglabātas visas +1 līmeņa virostnes
        for v in sobridejas_virsotnes: # Iet cauri visām šobrīdejām virsotnēm
            
            # print(nakosa_limena_virsotnes)
            # print(v)
            # print(speles_koks)

            #Izsauc augstāk definēto gājiena pārbaudes funckiju, kurā ievada spēles koku, nokošo līmeņa virsotņu masīvu un šobrīdejo virsotni
            gajiena_parbaude(speles_koks, nakosa_limena_virsotnes, v)

        # Ja visas līmeņa virsotnes tiek izskatītas, tad pārbaudām vai šis bija pirmais līmenis (ja ir, tas nozīmē, ka nav vairs gājienu, ja nav, tad iespējams vienkārši otrajā vai trešajā (pēc dziļuma) nav gājienu)
        if not nakosa_limena_virsotnes:
            if i == 0: # 0, jo sākas ar 0 līmeni, kas ir sākuma virsotne
                return True #Nozīmē, ka ir problēma

        # Turpinām un uzstādām uz šobrīdejām virstotnēm atrastās virsotnes un ejam dziļāk kokā
        sobridejas_virsotnes = nakosa_limena_virsotnes

    # Ja iestatījumos bija ieslēgta koka izdruka, tad šis izvadad saģenerēto koku
    if drukat == True:
        #ciklam beidzoties, tiek izvadīta spēles koka virsotņu kopa
        for x in speles_koks.virsotnu_kopa:
            print(x.id,x.virkne,x.p1,x.p2,x.limenis)

        #ciklam beidzoties, tiek izvadīta spēles koka loku kopa
        for x, y in speles_koks.loku_kopa.items():
            print(x, y)   

    # False nozīmē, ka viss ir noritējis veiksmīgi
    return False





# ----------------------------
# KOKS | FUNKCIJA, KAS ATROD VIRSOTNI KOKĀ
# ----------------------------
# Funkcija, kas tiek izsaukta Main.py daļā, kur ievadām spēles koku, meklējamo virkni un sākuma virsotni
def atrast_virsotni(speles_koks, virkne, izveleta_virsotne):
    # Ies cauri visām virsotnēm, kas ir kokā
    for virsotne in speles_koks.virsotnu_kopa:
        # Pārbaudīs vai virsotnes līmenis sakrīt ar sakuma virstones līmeni (jo meklējam šo virkni pirmajā līmeni, jo nevaram izlaist gājienus)
        if virsotne.limenis == ((izveleta_virsotne.limenis) + 1):
            # Pārbaudām vai virknes sakrīt
            if virsotne.virkne == virkne:
                #Ja sakrīt atgriežam virsotni uz Main.py
                return virsotne
    return None