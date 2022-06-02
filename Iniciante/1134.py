cod = int(input())
alcool = 0
gasolina = 0
diesel = 0
while cod != 4:
    if cod == 1:
        alcool += 1
    elif cod == 2:
        gasolina += 1
    elif cod == 3:
        diesel += 1
    cod = int(input())
print("MUITO OBRIGADO", end="\n")
print("Alcool:", alcool, end="\n")
print("Gasolina:", gasolina, end="\n")
print("Diesel:", diesel, end="\n")
