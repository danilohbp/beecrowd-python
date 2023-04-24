# -*- coding: utf-8 -*-

N = int(input())

soma = 0
while N > 0:
    x = int(input())
    for i in range(x - 1, 0, -1):
        if x % i == 0:
            soma += i
    if soma == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
    soma = 0
    N -= 1