N = [0] * 20

for i in range(0, len(N)):
    N[i] = int(input())

aux = 0
size = len(N) - 1
for i, v in enumerate(N):
    if i <= (len(N) - 1)/2:
        aux = N[i]
        N[i] = N[size]
        N[size] = aux
        size -= 1

for i, v in enumerate(N):
    print(f"N[{i}] = {v}")