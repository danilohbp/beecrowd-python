# -*- coding: utf-8 -*-

N = int(input())

vogais = ['a', 'e', 'i', 'o', 'u']

consoantes_consecutivas = 0

for i in range(N):
    consoantes_consecutivas = 0
    sobrenome = str(input())
    for l in sobrenome:
        t = l.lower()
        if t not in (vogais):
            consoantes_consecutivas += 1
            if consoantes_consecutivas == 3:
                print(f"{sobrenome} nao eh facil")
                break
        else:
            consoantes_consecutivas = 0
    if consoantes_consecutivas < 3:
        print(f"{sobrenome} eh facil")