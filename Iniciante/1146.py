# -*- coding: utf-8 -*-

X = int(input())
while X != 0:
    for i in range(1, X + 1):
        if i < X:
            print(i, end=" ")
        else:
            print(i)
    X = int(input())