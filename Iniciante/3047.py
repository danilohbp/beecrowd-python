# -*- coding: utf-8 -*-

M = int(input())
A = int(input())
B = int(input())
C = 0

if A != B and (A >= 1 and A < M) and (B >= 1 and B < M):
    C = M - (A + B)
    if C > A and C > B:
        print(C)
    elif A > C and A > B:
        print(A)
    else:
        print(B)