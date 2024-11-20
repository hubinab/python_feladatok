

for i in range(2,101):
    prim = True
    if i > 3:
        for j in range(2,i):
            if i % j == 0:
                prim = False
                break
    if prim:
        print(f"A {i} prímszám!")
        