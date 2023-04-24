# -*- coding: utf-8 -*-

N = [None] * 1000
T = int(input())
c = 0
for i in range(len(N)):
    N[i] = c
    print(f"N[{i}] = {N[i]}")
    if c < T - 1:
        c += 1
    else:
        c = 0