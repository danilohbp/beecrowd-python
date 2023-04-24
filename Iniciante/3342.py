# -*- coding: utf-8 -*-

n = int(input())
m = n * n

if m % 2 != 0:
    print(f"{(m//2) + 1} casas brancas e {m//2} casas pretas")
else:
    print(f"{int(m/2)} casas brancas e {int(m/2)} casas pretas")