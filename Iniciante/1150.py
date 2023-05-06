# -*- coding: utf-8 -*-

X = int(input())
Z = int(input())
c = 0
somatorio = 0
while True:
    if Z > X:       
        for i in range(X, Z + 1):
            somatorio += i
            c += 1
            if somatorio > Z:
                break
        break
    Z = int(input())
print(c)