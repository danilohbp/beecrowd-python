# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    R = eval("((3 * x) * (3 * x)) + (y * y)")
    B = eval("(2 * (x * x)) + ((5 * y) * (5 * y))")
    C = eval("-100 * x + (y * y * y)")
    if R > B and R > C:
        print(f"Rafael ganhou")
    elif B > R and B > C:
        print(f"Beto ganhou")
    elif C > R and C > B :
        print(f"Carlos ganhou")