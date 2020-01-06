#!/urs/bin/python3

def moltiplicatore(lista):
    risultato = 1
    for numero in lista:
        if numero != 0:
            risultato *= numero
    print('Il risultato della moltiplicazione è ' + str(risultato))

numeri = [12,24,1]

moltiplicatore(numeri)
