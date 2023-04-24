# -*- coding: utf-8 -*-

c = 0
soma = 0
while True:
    x = int(input())
    if x == 0:
        break
    else:
        if x % 2 == 0:
            for i in range(5):
                soma += x + (i + 2)
        else:
            x += 1
            for i in range(5):
               soma += x + (i + 2)
        print(soma)
        soma = 0