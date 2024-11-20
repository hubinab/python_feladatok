szam = int(input("Adj meg egy számot:"))

if szam%2 == 0:
    print("A szám osztható 2-vel")

if szam%3 == 0:
    print("A szám osztható 3-al")

if szam%5 == 0:
    print("A szám osztható 5-el")

if szam%7 == 0:
    print("A szám osztható 7-el")

if szam%2 == 0 and szam%3 == 0 and szam%5 == 0 and szam%7 == 0:
    print("Ez a szám varázsszám!")

