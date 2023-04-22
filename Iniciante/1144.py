N = int(input())

for i in range(1, N + 1):
    texto_um = str(i) + " " + str(i * i) + " " + str(i * (i * i))
    texto_dois = str(i) + " " + str((i * i) + 1) + " " + str((i * (i * i)) + 1)
    print(texto_um)
    print(texto_dois)