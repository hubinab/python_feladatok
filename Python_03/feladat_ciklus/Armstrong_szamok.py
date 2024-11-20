#for i in range(1,10):
#    for j in range(0, 10):
#        for k in range(0, 10):
#            print(f"{i}{j}{k}")

for i in range(1,10):
    for j in range(0, 10):
        for k in range(0, 10):
            c=f"{i}{j}{k}"
            if i**3 + j**3 + k**3 == int(c):
                print(c)
    