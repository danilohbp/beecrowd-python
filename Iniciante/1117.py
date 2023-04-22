qtd_notas_validas = 0
resultado = 0

while True:
    nota = float(input())
    if nota < 0.0 or nota > 10.0:
        print("nota invalida")
    else:
        resultado += nota
        qtd_notas_validas += 1
        if qtd_notas_validas == 2:
            resultado = resultado/2
            print(f"media = {resultado:.2f}")
            break