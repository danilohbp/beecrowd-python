# -*- coding: utf-8 -*-

N = [0] * 10
V = int(input())
for i in range(len(N)):
    if i == 0:
        N[0] = V
    else:
        N[i] = N[i - 1] * 2

for i, v in enumerate(N):
    print(f"N[{i}] = {v}")