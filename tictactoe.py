#Initierar ett spelbräde med tomma utrymme
rutnät = [' ' for x in range(10)]

# Poängmätare för varje spelare. 
poäng_spelare_X = 0
poäng_spelare_O = 0

#här har vi en funktion, parametrarna är letteroch pos. Vad denna funktion huvudsakligen gör är att infoga en given bokstav på en specifik position på spelplanen som användaren väljer
def insticksbokstav(bokstav, pos):
    rutnät[pos] = bokstav  

#Kontrollerar om ett visst utrymme vid en position är tillgängligt eller inte
def ledigplats(pos):
    return rutnät[pos] == ' '

#Skriver ut det som händer / aktuellt tillstånd i spelet
def utskrifttavla(rutnät):
    print('   |   |   ')
    print(' ' + rutnät[1] + ' | ' + rutnät[2] + ' | ' + rutnät[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + rutnät[4] + ' | ' + rutnät[5] + ' | ' + rutnät[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + rutnät[7] + ' | ' + rutnät[8] + ' | ' + rutnät[9])
    print('   |   |   ')

#Kontrollerar om spelplanen är full genom att räkna antalet tomma platser
def ärrutnätfylld(rutnät):
    if rutnät.count(' ') > 1:
        return False
    else:
        return True

#Ser till om spelaren X eller O är vinnaren!
def Är_vinnaren(b, bokstav):
    global poäng_spelare_X, poäng_spelare_O
    if ((b[1] == bokstav and b[2] == bokstav and b[3] == bokstav) or
        (b[4] == bokstav and b[5] == bokstav and b[6] == bokstav) or
        (b[7] == bokstav and b[8] == bokstav and b[9] == bokstav) or
        (b[1] == bokstav and b[4] == bokstav and b[7] == bokstav) or
        (b[2] == bokstav and b[5] == bokstav and b[8] == bokstav) or
        (b[3] == bokstav and b[6] == bokstav and b[9] == bokstav) or
        (b[1] == bokstav and b[5] == bokstav and b[9] == bokstav) or
        (b[3] == bokstav and b[5] == bokstav and b[7] == bokstav)):
        if bokstav == 'X':
            poäng_spelare_X += 1
        elif bokstav == 'O':
            poäng_spelare_O += 1
        return True
    return False


#funktionen för användares input.  tar emot ett integer, dvs en nummer mellan 1-9 
def användaresdrag():
    kör = True
    while kör:
        drag = input("vänligen välj en position för att ange X mellan 1 och 9\n")
        try:
            drag = int(drag)
            if drag > 0 and drag < 10:
                if ledigplats(drag):
                    kör = False
                    insticksbokstav('X' , drag)
                else:
                    print('Tyvärr, det här utrymmet är upptaget')
            else:
                print("Skriv ett nummer mellan 1 och 9")

        except:
            print('Vänligen skriv ett nummer')

#skriver ut/baserar datorns output till användares input 
def datornsdrag():
    möjligadrag = [x for x , bokstav in enumerate(rutnät) if bokstav == ' ' and x != 0  ]
    drag = 0

    for let in ['O' , 'X']:
        for i in möjligadrag:
            rutnätkopia = rutnät[:]
            rutnätkopia[i] = let
            if Är_vinnaren(rutnätkopia, let):
                drag = i
                return drag

    öppnahörn = []
    for i in möjligadrag:
        if i in [1 , 3 , 7 , 9]:
            öppnahörn.append(i)

    if len(öppnahörn) > 0:
        drag = väljslump(öppnahörn)
        return drag

    if 5 in möjligadrag:
        drag = 5
        return drag

    öppnakanter = []
    for i in möjligadrag:
        if i in [2,4,6,8]:
            öppnakanter.append(i)

    if len(öppnakanter) > 0:
        drag = väljslump(öppnakanter)
        return drag

#Väljer ett slumpmässigt drag från en lista över möjliga drag. Det här är viktigt att veta eftersom respons för en input är random, och inte riggad på något sätt 
def väljslump(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

#En loop för själva spelet
def huvud():
    global poäng_spelare_X, poäng_spelare_O
    print("Välkommen till spelet!! :D")
    print("Poängställning - Spelare X: {}, Spelare O: {}".format(poäng_spelare_X, poäng_spelare_O))
    utskrifttavla(rutnät)

    while not(ärrutnätfylld(rutnät)):
        if not(Är_vinnaren(rutnät , 'O')):
            användaresdrag()
            utskrifttavla(rutnät)
        else:
            print("Du förlorade! :( Lycka till nästa gång ")
            break

        if not(Är_vinnaren(rutnät , 'X')):
            drag = datornsdrag()
            if drag == 0:
                print(" ")
            else:
                insticksbokstav('O' , drag)
                print('Datorn placerade ett O på plats' , drag , ':')
                utskrifttavla(rutnät)
        else:
            print("Du vann!")
            break

    if ärrutnätfylld(rutnät):
        print("Oj, Ser ut som ingen vann eller förlorade! (utan segrare)")

#Loop som kör om spelet om man vill köra eller "break" tar plat man om man vill inte. 
while True:
    x = input("Vill du spela tictactoe? Svara i (ja/nej)\n")
    if x.lower() == 'ja':
        rutnät = [' ' for x in range(10)]
        
        print('   |   |   ')
        print(' 1 | 2 | 3 ')
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(' 4 | 5 | 6 ')
        print('   |   |   ')
        print('-----------')
        print('   |   |   ')
        print(' 7 | 8 | 9 ')
        print('   |   |   ')
        print("Här är en liten guide om hur man ska skriva in sitt svar! \nMan skriver sitt nummer var man vill ha sin X/0 \n")
        print('--------------------')
        huvud()
    else:
        break
