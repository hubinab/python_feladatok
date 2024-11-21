
# Fuggveny
def Paros(szam):
    return szam % 2 == 0

# Eljaras
def teglalap (magassag, szelesseg, katrakter = '*'):
#    print((karakter*szelesseg + "\n")*magassag)
    for i in range(magassag):
        for j in range(szelesseg):
            print(katrakter, end="")
        print()


