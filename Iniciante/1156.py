n = 3
d = 2
S = 1
while n <= 39:
    S += n/d
    n += 2
    d *= 2
print(f"{S:.2f}")