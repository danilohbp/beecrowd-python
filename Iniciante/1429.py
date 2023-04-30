# -*- coding: utf-8 -*-

parada = 1
while parada != 0:
    ACM = str(input())
    if int(ACM) == 0:
        break
    else:
        decimal = 0
        c = 0
        
        for i in range(len(ACM), 0, -1):
            fatorial = 1
            for j in range(1, i + 1):
                fatorial *= j
            decimal += int(ACM[c]) * fatorial
            c += 1
        print(decimal)