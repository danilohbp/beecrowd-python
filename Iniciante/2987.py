# -*- coding: utf-8 -*-

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
L = str(input()).upper()
for i, v in enumerate(alfabeto):
    if L == v:
        print(i + 1)
