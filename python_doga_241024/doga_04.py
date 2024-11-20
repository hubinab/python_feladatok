szam = int(input("Adj meg egy számot: "))

prim = True

for i in range(2,szam):
    if szam%i == 0 and i != szam:
        prim = False

if prim:
    print("Ez primszám!")
else:
    print("Ez nem primszám!")

