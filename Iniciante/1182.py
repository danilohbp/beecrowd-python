# -*- coding: utf-8 -*-

matriz = list()
for i in range(12):
    vetor = [0] * 12
    matriz.append(vetor)

C = int(input())
T = str(input())
soma = 0
media = 0

if C >= 0 and C <= 11:
    for i in range(12):
        for j in range(12):
            matriz[i][j] = float(input())
    
    if T == 'S':
        for i in range(12):
            for j in range(12):
                if j == C:
                    soma += matriz[i][j]    
        print(f"{soma:.1f}")   
    elif T == 'M':
        for i in range(12):
            for j in range(12):
                if j == C:
                    media += matriz[i][j]
        media = media/12    
        print(f"{media:.1f}")