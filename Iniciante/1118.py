media = 0.0
c = 0
while True:
    n = float(input())
    if n < 0.0 or n > 10.0:
        print("nota invalida")
    else:
        c += 1
        media += n
        if c == 2:
            media = media/2
            print(f"media = {media:.2f}")
            print("novo calculo (1-sim 2-nao)")
            X = int(input())
            while X < 1 or X > 2:
                print("novo calculo (1-sim 2-nao)")    
                X = int(input())
            if X == 2:
                break
            c = 0
            media = 0