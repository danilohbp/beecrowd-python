# -*- coding: utf-8 -*-

T = int(input())

nova_posicao = 0
while T > 0:
    N = int(input())
    fib = [0, 1, 1]
    
    if N > 2:
        for i in range(3, N + 1):
            nova_posicao = fib[i - 1] + fib[i - 2]
            fib.append(nova_posicao)
            
    print(f"Fib({N}) = {fib[N]}")
    
    T -= 1