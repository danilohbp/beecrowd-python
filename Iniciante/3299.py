# -*- coding: utf-8 -*-

N = int(input())
N = str(N)

anterior = 0
ma_sorte = False
for i in N:        
    if anterior == '1' and i == '3':
        ma_sorte = True
        break
    else:
        anterior = 0
    
    if i == '1':
        anterior = i        
     
if ma_sorte:
    print(f"{N} es de Mala Suerte")
else:
    print(f"{N} NO es de Mala Suerte")