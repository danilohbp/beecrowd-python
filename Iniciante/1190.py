O = input()
m = list()
for i in range(12):
    v = [0] * 12
    m.append(v)

soma = 0
media = 0
qtd = 0

for i in range(len(m)):
    for j in range(len(m)):
        m[i][j] = float(input())
        if i != j and i < j and i + j > 11:
            soma += m[i][j]
            qtd += 1

if O == 'S':
    print(f"{soma:.1f}")
elif O == 'M':
    media = soma/qtd
    print(f"{media:.1f}")             