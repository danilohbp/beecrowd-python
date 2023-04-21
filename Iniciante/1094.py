# -*- coding: utf-8 -*-

N = int(input())
Quantia, Tipo = map(str, input().split())
Quantia = int(Quantia)

dict = {'C': 0, 'S': 0, 'R': 0}
total = Quantia

dict[Tipo.upper()] += Quantia

for i in range(1, N):
    Quantia, Tipo = map(str, input().split())
    Quantia = int(Quantia)
    total += Quantia
    dict[Tipo.upper()] += Quantia

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {dict['C']}")
print(f"Total de ratos: {dict['R']}")
print(f"Total de sapos: {dict['S']}")
print(f"Percentual de coelhos: {(dict['C']/total * 100):.2f} %")
print(f"Percentual de ratos: {(dict['R']/total * 100):.2f} %")
print(f"Percentual de sapos: {(dict['S']/total * 100):.2f} %")