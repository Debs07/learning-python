#!/urs/bin/python3

def traduttore():
    print('''
    Ciao! Questo programma traduce un testo passato in "rövarspråket"
    ''')

    vocali = "aeiou"
    specials = [" ", ",", ".", "?", "!", '"',"'"]

    while True:
        testo = input('\nInserisci il testo che vuoi tradurre -> ')
        tradotta = ""
        for x in testo:
            if x in vocali or x in specials:
                tradotta += x #tradotta = tradotta + x
            else:
                tradotta = tradotta + x + "o" + x
        print(f"Ecco a te la traduzione! '{tradotta}'")    
        if  input("\nVuoi tradurre un'altra frase?") == "no":
            break

traduttore()


            
            