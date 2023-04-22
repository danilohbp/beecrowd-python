import math

i = float(0)
j = float(0)
seq = 0.2
c = 0
while True:
    if int(i) == 2 and c % 3 == 0:
        break
    
    if c != 0 and c % 3 == 0:
        j = 1
        i = 0
        i += seq
        j += seq
        
        if i > 1.8 and i < 2.0:
            i = float(round(i))
        
        if i.is_integer():
            if j.is_integer():
                print(f"I={int(i)} J={int(j)}")
            else:
                print(f"I={int(i)} J={j:.1f}")
        else:
            print(f"I={i:.1f} J={j:.1f}")
        seq += 0.2
    else:
        j += 1
        
        if i.is_integer():
            if j.is_integer():
                print(f"I={int(i)} J={int(j)}")
            else:
                print(f"I={int(i)} J={j:.1f}")
        else:
            if j.is_integer():
                print(f"I={i:.1f} J={int(j)}")
            else:
                print(f"I={i:.1f} J={j:.1f}")
    c += 1