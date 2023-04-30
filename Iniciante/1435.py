# -*- coding: utf-8 -*-
c = 0
while True:
    N = int(input())
    if N == 0:
        break
    else:
        for i in range(N):
            for j in range(N):
                if i > j:
                    print(f"  {j + 1}", end="")
                elif i < j:
                    print(f"  {i + 1}", end="")
                elif i == j and i < N - 1:
                    print(f"  {i + 1}", end="")
                else:
                    print(f"  {(N - i)}", end="")
            print()