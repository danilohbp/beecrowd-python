import math

R, L = map(int, input().split())
PI = 3.1415

v = (4/3) * (PI * math.pow(R, 3))

v = L/v

print(int(v))