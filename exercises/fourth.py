#!/urs/bin/python3

def sommatrice(lista):
    risultato = 0
    for numero in lista:
        risultato += numero 
    print('Il risultato della somma è: ' + str(risultato))

lista = [16,24,32]

sommatrice(lista)
