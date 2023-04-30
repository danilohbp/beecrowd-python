# -*- coding: utf-8 -*-

while True:
    qtd_quadrados_diferentes = 0
    N = int(input())
    if N == 0:
        break
    else:
        for i in range(N, 0, -1):
            qtd_quadrados_diferentes += (i * i)
        print(qtd_quadrados_diferentes)