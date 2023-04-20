I=1
J=7

while True:
    print(f"I={I} J={J}")
    sequencia =  J - I
    if sequencia == 4:
        I += 2
        J += 4
    else:
        J -= 1
        
    if I == 11 and J == 17:
        break