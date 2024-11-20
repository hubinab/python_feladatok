Szoveg = input("Irj be egy szoveget: ")

# Betunkent egyel no a kiirt szoveg
for i in range(1,len(Szoveg)+1):
    print(Szoveg[:i])

# Atlosan
for i in range(0,len(Szoveg)):
    if i == 0:
        print(Szoveg[i])
    else:    
        print(' ' * (i-1), Szoveg[i])


