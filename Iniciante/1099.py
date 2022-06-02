N = int(input())
lista_saida = []
for i in range(N):
    X, Y = input().split(" ")
    X = int(X)
    Y = int(Y)
    soma = 0
    if X <= Y:
        for j in range(X + 1, Y):
            if j % 2 != 0:
                soma += j
    else:
        for j in range(Y + 1, X):
            if j % 2 != 0:
                soma += j
    lista_saida.append(soma)

for i in range(len(lista_saida)):
    print(lista_saida[i], end="\n")
