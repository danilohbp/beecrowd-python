N = int(input())

while N >= 1:
    c = 0
    x = int(input())
    d = x
    while d > 0: 
        if x % d == 0:
            c += 1
    
        if d == 1:
            if c == 2:
                print(f"{x} eh primo")
            else:
                print(f"{x} nao eh primo")
        d -= 1
    N -= 1