EvSzam = int(input("Mikor adták ki az Aranybullát? "))
i = 0

while EvSzam != 1222:
    i = i + 1
    if EvSzam < 1222:
        print("Nem volt az olyan régen!")
    elif EvSzam > 1222:
        print("Régebben történt!")
    
    if i >= 5:
        print("A helyes válasz 1222!")
        break
    print(i)
    EvSzam = int(input("Mikor adták ki az Aranybullát? "))

if i < 5:
    print("Ez a jó válasz")
if i < 3:
    print("De ügyes vagy!")



