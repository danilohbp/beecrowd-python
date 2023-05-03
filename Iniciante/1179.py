# -*- coding: utf-8 -*-

par = []
impar = []

cp = 0
ci = 0

for i in range(15):
    e = int(input())
    if e % 2 == 0 or e == 0:
        par.append(e)
        cp += 1
        if cp == 5:
            for i, v in enumerate(par):
                print(f"par[{i}] = {v}")
            par = []
            cp = 0
    else:
        impar.append(e)
        ci += 1
        if ci == 5:
            for i, v in enumerate(impar):
                print(f"impar[{i}] = {v}")
            impar = []
            ci = 0
for i, v in enumerate(impar):
    print(f"impar[{i}] = {v}")

for i, v in enumerate(par):
    print(f"par[{i}] = {v}")