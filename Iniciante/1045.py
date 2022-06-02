lista = input().split(" ")
lista[0] = float(lista[0])
lista[1] = float(lista[1])
lista[2] = float(lista[2])
lista.sort(reverse = True)
A = lista[0]
B = lista[1]
C = lista[2]
if A > 0 and B > 0 and C > 0:
    if A >= (B + C):
        print("NAO FORMA TRIANGULO", end="\n")
    else:
        if (A ** 2) == ((B ** 2) + (C ** 2)):
            print("TRIANGULO RETANGULO", end="\n")
        if (A ** 2) > ((B ** 2) + (C ** 2)):
            print("TRIANGULO OBTUSANGULO", end="\n")
        if (A ** 2) < ((B ** 2) + (C ** 2)):
            print("TRIANGULO ACUTANGULO", end="\n")
        if A == B == C:
            print("TRIANGULO EQUILATERO", end="\n")
        if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
            print("TRIANGULO ISOSCELES", end="\n")
