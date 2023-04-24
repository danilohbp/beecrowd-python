# -*- coding: utf-8 -*-

lista = list(map(int, input().split()))
soma = 0
i = 0
for j in range(1,len(lista)):
    N = lista[j]
    i = 0
    if N >= 0:
        while i < N:
            soma += lista[0] + i
            i += 1
print(soma)