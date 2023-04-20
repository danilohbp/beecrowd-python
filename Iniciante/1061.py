# -*- coding: utf-8 -*-

di = int(input().split()[1])
hi, mi, si = map(int, input().split(" : "))
df = int(input().split()[1])
hf, mf, sf = map(int, input().split(" : "))

si = (di * 3600 * 24) + (hi * 3600) + (mi * 60) + si
sf = (df * 3600 * 24) + (hf * 3600) + (mf * 60) + sf 
tempo = sf - si

if tempo <= 0:
    tempo += 3600 * 24
    
W = tempo//(3600 * 24)
X = (tempo%(3600 * 24))//3600
Y = (tempo//(60))%60
Z = tempo%60

print(f"{W} dia(s)")
print(f"{X} hora(s)")
print(f"{Y} minuto(s)")
print(f"{Z} segundo(s)")
