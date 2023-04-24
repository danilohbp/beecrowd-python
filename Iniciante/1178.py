# -*- coding: utf-8 -*-

N = [0] * 100
X = float(input())

N[0] = X
for i in range(1, len(N)):
    N[i] = N[i - 1]/2

for i in range(len(N)):
    print(f"N[{i}] = {N[i]:.4f}")