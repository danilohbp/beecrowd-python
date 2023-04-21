I = 0
J = 1

c = 1
d = 0
while True:
    print(f"I={I} J={J}")
    if c % 3 == 0:
        if I == 2:
            break
        c = 0
        d += 0.2
        J = 0 + d
        I = 0 + d
        
    c += 1
    J += 1
    I = round(I, 1)
    J = round(J, 1)