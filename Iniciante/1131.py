i, g = map(int, input().split())
grenais = 0

inter = 0
gremio = 0
empate = 0
vencedor = ""

parada = 1
while parada == 1:
    if i > g:
        inter += 1
    elif g > i:
        gremio += 1
    else:
        empate += 1
        
    print(f"Novo grenal (1-sim 2-nao)")
    grenais += 1
    
    parada = int(input())
    
    if parada == 2:
        print(f"{grenais} grenais")
        print(f"Inter:{inter}")
        print(f"Gremio:{gremio}")
        print(f"Empates:{empate}")
        
        if inter == gremio and empate > 0:
            print(f"Nao houve vencedor")
        elif inter > gremio:
            print(f"Inter venceu mais")
        elif gremio > inter:
            print(f"Gremio venceu mais")
        break
    i, g = map(int, input().split())