inicio, fim = input().split(" ")
inicio = int(inicio)
fim = int(fim)
hora_restante = 24 - inicio
if fim < inicio:
    resultado = hora_restante + fim
elif fim > inicio:
    resultado = fim - inicio
else:
    resultado = 24
print("O JOGO DUROU",resultado,"HORA(S)", end="\n")
