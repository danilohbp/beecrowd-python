X = int(input())
Y = int(input())
lista_saida = []
if X <= Y:
    for i in range(X + 1, Y):
        if i % 5 == 2 or i % 5 == 3:
            lista_saida.append(i)    
else:
    for i in range(Y + 1, X):
        if i % 5 == 2 or i % 5 == 3:
            lista_saida.append(i)
lista_saida.sort()
for i in range(len(lista_saida)):
    print(lista_saida[i],end="\n")
