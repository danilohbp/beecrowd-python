# -*- coding: utf-8 -*-

fu, fd = map(float, input().split())

flutuacao = 0

if fu >= -100.0 and fu <= 100.0 and fd >= -100 and fd <= 100.0:
    ano_um = (100 * (1 + (fu/100)))
    ano_dois = (ano_um * (1 + (fd/100)))
    print(f"{(ano_dois - 100):.6f}")