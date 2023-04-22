# -*- coding: utf-8 -*-

N = int(input())
d = 1

while d <= N:
    if N % d == 0:
        print(d)
    d += 1