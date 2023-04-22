while True:
    X, Y = map(int, input().split())
    if X > 0:
        if Y > 0:
            print(f"primeiro")
        elif Y < 0:
            print(f"quarto")
    elif X < 0:
        if Y > 0:
            print(f"segundo")
        elif Y < 0:
            print(f"terceiro")
    
    if X == 0 or Y == 0:
        break