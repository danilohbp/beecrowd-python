# -*- coding: utf-8 -*-

N = int(input())
soma = 0
c = 0

while N > 0:
    soma = 0
    X, Y = map(int, input().split())
    while Y > 0:
        if X != 0 and X % 2 != 0:
            soma += X
            X += 2
            Y -= 1
        else:
            X += 1
    print(soma)
    N -= 1