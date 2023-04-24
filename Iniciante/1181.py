# -*- coding: utf-8 -*-

L = int(input())
T = str(input())
M = list()
for i in range(12):
    c = [0] * 12
    M.append(c)

for i in range(12):
    for j in range(12):
        M[i][j] = float(input())
        
linha = M[L]
q = 0
soma = 0
for v in linha:
    soma += v
    q += 1

if T.upper() == "S":
    print(f"{soma:.1f}")
elif T.upper() == "M":
    print(f"{(soma/q):.1f}")