N = int(input())
n = 0
c = 0
pg = []

while N > 0:
    for j in range(1, N + 1):
        if N % j == 0:
            n += 1     
    if n == 2:
        pg.append(N)
        n = 0
        c += 1
        if c == 2:
            if abs(pg[0] - pg[1]) == 2:
                print(f"{pg[1]} {pg[0]}")
                break
            else:
                pg = []
                pg.append(N)
                c = 1
    if n > 2:
        n = 0
    N -= 1