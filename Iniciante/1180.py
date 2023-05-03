# -*- coding: utf-8 -*-

N = int(input())
vetor = [0] * N

e = str(input())
vaux = e.split()

menor = 0
pos = 0

for i in range(N):
    vetor[i] = int(vaux[i])

for i in range(N):
    if i == 0:
        menor = vetor[i]
    elif menor > vetor[i]:
        menor = vetor[i]
        pos = i
print(f"Menor valor: {menor}")
print(f"Posicao: {pos}")