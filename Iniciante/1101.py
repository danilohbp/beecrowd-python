lista = list()
lista_sequencia = list()

while True:
    M, N = map(int, input().split())
    if M <= 0 or N <= 0:
        for i in range(0, len(lista)):
            sequencia = ""
            somatorio = 0
            for j in range(lista[i][0], lista[i][1] + 1):
                if len(sequencia) == 0:
                    sequencia += str(j)
                else:
                    sequencia += " " + str(j)
                    
                somatorio += j
            lista_sequencia.append((sequencia, somatorio))
            
        for j in range(0, len(lista_sequencia)):
            print(f"{lista_sequencia[j][0]} Sum={lista_sequencia[j][1]}")
        
        break
    else:
        if M > N:
            lista.append((N, M))
        elif N > M:
            lista.append((M, N))