#!/usr/bin/env python3

while True:
    
    print('''
    Benvenuto al programma calcolatrice!
    Creata da Debora
    Qui di seguito un elenco delle varie funzioni disponibili:

    -Per effettuare un'addizione, seleziona 1;
    -Per effettuare una sottrazione, seleziona 2;
    -Per effettuare una moltiplicazione, seleziona 3;
    -Per effettuare una divisione, seleziona 4;
    -Per effettuare un calcolo esponenziale, seleziona 5;
    -Per uscire dal programma puoi digitare ESC;
    ''')
    scelta = input('Inserisci il numero corrispondente all\'azione desiderata ---> ')

    if scelta == "1":
        print('\nHai scelto: Addizione\n')
        a = float(input('Inserisci il primo numero ->'))
        b = float(input('Inserisci il secondo numero ->'))
        print('Il risultato della somma è: ' +str(a + b))

    elif scelta == "2":
        print('\nHai scelto: Sottrazione\n')
        a = float(input('Inserisci il primo numero ->'))
        b = float(input('Inserisci il secondo numero ->'))
        print('Il risultato della somma è: ' +str(a - b))

    elif scelta == "3":
        print('\nHai scelto: Moltiplicazione\n')
        a = float(input('Inserisci il primo numero ->'))
        b = float(input('Inserisci il secondo numero ->'))
        print('Il risultato della somma è: ' +str(a * b))

    elif scelta == "4":
        print('\nHai scelto: Divisione\n')
        a = float(input('Inserisci il primo numero ->'))
        b = float(input('Inserisci il secondo numero ->'))
        print('Il risultato della somma è: ' +str(a / b))

    elif scelta == "5":
        print('\nHai scelto: Calcolo Esponenziale\n')
        a = float(input('Inserisci la base ->'))
        b = float(input('Inserisci l\'esponente ->'))
        print('Il risultato della somma è: ' +str(a ** b))

    elif scelta == "ESC":
        break 

    loop = input('\nDesideri ancora utilizzare l\'applicazione? S/N?\n')
    if loop == "S" or loop == "s":
        continue 
    else:
        break
