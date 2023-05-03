# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    y = 0
    a, b, ta, tb = map(float, input().split())
    aux = int(a * (ta/100))
    bux = int(b * (tb/100))
    while True:
        a += aux
        b += bux
        y += 1
        if y > 100:
            print("Mais de 1 seculo.")
            break
        elif a > b:
            print(f"{y} anos.")
            break
        aux = int(a * (ta/100))
        bux = int(b * (tb/100))