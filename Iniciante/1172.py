# -*- coding: utf-8 -*-

x = [None] * 10
t = 0

while t <= 9:
    x[t] = int(input())
    if x[t] <= 0:
        x[t] = 1
    t += 1

for i, v in enumerate(x):
    print(f"X[{i}] = {v}")