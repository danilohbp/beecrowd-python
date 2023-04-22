# -*- coding: utf-8 -*-

while True:
    X, Y = map(int, input().split())
    
    if X < Y:
        print(f"Crescente")
    elif X > Y:
        print(f"Decrescente")
    else:
        break