#!/usr/bin/python3

def my_max(a,b):
    if a == b:
        print('I numeri sono identici')
    elif a > b:
        print('Il numero più grande dei due è: ' + str(a))
    else:
        print('Il numero più grande dei due è: ' + str(b))

my_max(3,2)