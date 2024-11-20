ElemBe = int(input("Hány Lego elem van a dobozban?"))
Elem = ElemBe
j = 0
i = 2
Osszesen = 0

while Elem > 0:
    j = j + 1
    print("Teszt: torony sorszáma:", j, "magassága:", i)
    Osszesen = Osszesen + i 
    i = i + 3
    Elem = Elem - i

Maradek = ElemBe - Osszesen

if Maradek != 0:
    j = j + 1

print("A megépíthető tornyok száma:", j)

if Maradek != 0:
    print("Az utolsó torony magassága:", Maradek)
