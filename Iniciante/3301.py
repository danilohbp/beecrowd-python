# -*- coding: utf-8 -*-

H, Z, L = map(int,input().split())

lista = list()
lista.append(H)
lista.append(Z)
lista.append(L)

menor = lista[0]
maior = lista[0]

for i in range(len(lista)):
    if menor > lista[i]:
        menor = lista[i]
    
    if maior < lista[i]:
        maior = lista[i]

for i in range(len(lista)):
    if lista[i] != menor and lista[i] != maior:
        if i == 0:
            print("huguinho")
        elif i == 1:
            print("zezinho")
        else:
            print("luisinho")
        break