# 1. Jelszó
# Írjunk programot, ami addig kérdezi a jelszavunkat, míg el nem találjuk!
# Mi a jelszó? xxx
# Nem.
# Mi a jelszó? titok
# Óóó, de ügyes vagy!

"""
jelszó = "titok"
jelszóBe = input("Mi a jelszó? ")

if jelszóBe == jelszó:
    print("Óóó, de ügyes vagy!")
else:
    print("Nem.")


while jelszóBe != jelszó:
    jelszóBe = input("Mi a jelszó? ")
    if jelszóBe == jelszó:
        print("Óóó, de ügyes vagy!")
    else:
        print("Nem.")
"""

jelszó = "titok"
jelszóBe = input("Mi a jelszó? ")

while jelszóBe != jelszó:
    print("Nem.")
    jelszóBe = input("Mi a jelszó? ")

print("Óóó, de ügyes vagy!")


# 2. Történelem
# Történelem érettségin a vizsgázó sajnos nem tudja az esemény évszámát, de a tanára segít
# neki, hátha eszébe jut. A diák jobb híján tippel, ha eltalálta, szerencséje van. Ha nem, akkor
# kap újabb esélyt, sőt segítséget is: „Régebben történt” vagy „Nem volt az annyira régen”.
# Készítsünk egy programot, amely helyettesíti a jóindulatú tanárt!
# A program próbálja meg az Aranybulla kiadásának évére rávezetni a kitartó diákot!
# Ha 3 kísérletből kitalálta, akkor még egy visszafogott dicséretet is írjon ki!
# Melyik évben is adták ki az Aranybullát? 1111
# Nem volt az olyan régen!
# Melyik évben is adták ki az Aranybullát? 1333
# Régebben történt!
# Melyik évben is adták ki az Aranybullát? 1222
# Ez a jó válasz!
# Ügyes vagy!

"""
aranybulla = 1222
tipp = int(input("Melyik évben is adták ki az Aranybullát? "))
próbálkozás = 1
while tipp != aranybulla:
    if tipp < aranybulla:
        print("Nem volt az olyan régen!")
    else:
        print("Régebben történt!")
    tipp = int(input("Melyik évben is adták ki az Aranybullát? "))
    próbálkozás += 1
    #próbálkozás = próbálkozás + 1

print("Ez a jó válasz!")
if próbálkozás <= 3:
    print("Ügyes vagy!")
"""


# Fejlesszük tovább a programot! Ha az ötödik próbálkozás sem sikeres, akkor a tanár türelme
# elfogyott, és megadja a helyes választ.

aranybulla = 1222
tipp = int(input("Melyik évben is adták ki az Aranybullát? "))
próbálkozás = 1
while tipp != aranybulla and próbálkozás <= 5:
    if tipp < aranybulla:
        print("Nem volt az olyan régen!")
    else:
        print("Régebben történt!")
    tipp = int(input("Melyik évben is adták ki az Aranybullát? "))
    próbálkozás += 1
    #próbálkozás = próbálkozás + 1

if próbálkozás <= 5:
    print("Ez a jó válasz!")
    if próbálkozás <= 3:
        print("Ügyes vagy!")
else:
    print("Elfogyott a türelmem, ne tippelgess tovább. A válasz 1222!")


# 3. Lego
# Lego elemekből tornyokat építünk. A legelső 2 elemből áll, a következő 5 és minden
# következő 3 elemmel magasabb az előzőnél. Egy doboznyi Legoból hány tornyot lehet
# elkészíteni? A legutolsó toronyhoz hány elem maradt?
# Hány Lego elem van a dobozban? 42
# teszt: torony sorszáma: 1 magassága: 2
# teszt: torony sorszáma: 2 magassága: 5
# teszt: torony sorszáma: 3 magassága: 8
# teszt: torony sorszáma: 4 magassága: 11
# teszt: torony sorszáma: 5 magassága: 14
# A megépíthető tornyok száma: 6
# Az utolsó torony magassága: 2

legoMaradék = int(input("Hány Lego elem van a dobozban? "))
toronyMagasság = 2
toronySorszám = 1
while legoMaradék >= toronyMagasság:
    print("teszt: torony sorszáma:", toronySorszám, "magassága:", toronyMagasság)
    legoMaradék -= toronyMagasság
    toronySorszám += 1
    toronyMagasság += 3
    # legoMaradék = legoMaradék - toronyMagasság
    # toronySorszám = toronySorszám + 1
    # toronyMagasság = toronyMagasság + 2
print("A megépíthető tornyok száma:", toronySorszám)
print("Az utolsó torony magassága:", legoMaradék)


# 4. Másodfokú egyenlet
# Oldjuk meg próbálgatással a 4x2 + 6x + 3 = 2419581 egyenletet a természetes számok
# halmazán!
# A megoldás: 777

x = 0
while 4*x**2 + 6*x + 3 != 2419581:
    x += 1
    # x = x + 1
print("A megoldás:", x)

# 5. Hidratálás
# Naponta legalább 2,5 liter folyadékot kell fogyasztanunk és ivásból nem vagyunk valami jók.
# Írjunk programot, amelyik bekéri, hogy egy-egy alkalommal hány decit ittunk! Teszi mindezt
# addig, amíg üres karakterláncot nem adunk meg. Minden bekéréskor kiírja, hogy addig hány
# litert ittunk összesen, és ha elérjük a 2,5 litert, akkor erről is megemlékezik. 3,5 liter fölött
# kilép, szépen elbúcsúzva tőlünk.
# Hány decit ittál? 5
# Már 0.5 litert ittál.
# ...
# Hány decit ittál? 3
# Már 2.6 litert ittál.
# Már sikerült elérned a 2,5 litert.
# Hány decit ittál? 11
# Már 3.7 litert ittál.
# Már sikerült elérned a 2,5 litert.
# Béka nő a hasadba'!

összFogyasztás = 0
while összFogyasztás < 35:
    összFogyasztás += int(input("Hány decit ittál? "))
    # összFogyasztás = összFogyasztás + int(input("Hány decit ittál? "))
    print("Már", összFogyasztás/10, "litert ittál.")
    if összFogyasztás >= 25:
        print("Már sikerült elérned a 2,5 litert.")
print("Béka nő a hasadba'!")

# 6. Szorzótábla
# Készítsük el a 10x10-es szorzótáblát:

for i in range(10):  # 0-9
    for i2 in range(10):
        print(i+1, " * ", i2+1, " = ", (i+1)*(i2+1))

"""
for i in range(1,11): #1-10
    for i2 in range(1,11):
        print(i, " * ", i2, " = ", i*i2)
"""

"""
i = 1
i2 = 1
while i < 10:
    while i2 < 10:
        print(i, " * ", i2, " = ", i*i2)
        i += 1
        i2 += 1
        # i = i + 1
        # i2 = i2 + 1
"""


# 7. Prímek
# Írjuk ki az első 100 természetes szám közül a prímeket!
# A 2 prímszám.
# A 3 prímszám.
# ...
# A 97 prímszám.

for i in range(100):  # 0-99->
    i += 1            # 1-100
    # i = i+1
    osztó = 2
    while i % osztó != 0 and osztó < i:
        osztó += 1
        # osztó = osztó+1
    if osztó == i:
        print("A", i, "prímszám.")

"""
for i in range(1, 101):  # 1-100
    osztó = 2
    while i % osztó != 0 and osztó < i:
        osztó += 1
        # osztó = osztó+1
    if osztó == i:
        print("A", i, "prímszám.")
"""


# 8. Armstrong számok
# Írjunk egy olyan programot, amely három egymásba ágyazott ciklus segítségével az összes
# háromjegyű számot kiírja.

for i in range(1, 10):
    for i2 in range(1, 10):
        for i3 in range(1, 10):
            szám = 100 * i + 10 * i2 + i3
            print(szám)


# A programunkat fejlesszük tovább! Csak azokat a számokat írassuk ki, amelyekre az igaz, hogy
# a számjegyeik harmadik hatványának összege éppen a számmal egyenlő! (Az ilyen számokat
# Amstrong-számoknak nevezik.)
# Armstrong szám: 153 Ellenőrzés: 153 = 1 + 125 + 27

for i in range(1, 10):
    for i2 in range(1, 10):
        for i3 in range(1, 10):
            szám = 100 * i + 10 * i2 + i3
            if i**3 + i2**3 + i3**3 == szám:
                print(szám, "Ellenőrzés:", szám, "=",
                      i**3, "+", i2**3, "+", i3**3)


# 9. Érdekes számok
# Keressük meg egy program segítségével azokat a kétjegyű számokat, amelyekre igaz, hogy:
# c) a szám osztható a számjegyei összegével
# A szám osztható számjegyei összegével: 10 12 18 20 21 ...

print("A szám osztható számjegyei összegével:")
# print("A szám osztható számjegyei összegével: ", end="")
# end-el megadható milyen karakter kerüljön a kiírás végére, ezzel elkerülhető a sortörés
for i in range(1, 10):
    for i2 in range(1, 10):
        szám = 10 * i + i2
        osztó = i + i2
        if szám % osztó == 0:
            print(szám)
            # print(szám, end=" ")
# print()


# d) a szám osztható a számjegyei különbségével (figyeljünk arra, ha a különbség nulla))

print("A szám osztható számjegyei különbségével:")
# print("A szám osztható számjegyei különbségével:", end="")
for i in range(1, 10):
    for i2 in range(1, 10):
        szám = 10 * i + i2
        osztó = i - i2
        if osztó != 0 and szám % osztó == 0:
            print(szám)
            # print(szám, end=" ")
# print()


# e) a szám osztható számjegyei összegével is, különbségével is.

print("A szám osztható számjegyei összegével és különbségével:")
# print("A szám osztható számjegyei összegével és különbségével:", end="")
for i in range(1, 10):
    for i2 in range(1, 10):
        szám = 10 * i + i2
        osztó = i - i2
        osztó2 = i + i2
        if osztó != 0 and szám % osztó == 0 and szám % osztó2 == 0:
            print(szám)
            # print(szám, end=" ")
# print()


# 10. Csillagok
# Kérjünk be két különböző, 10 és 20 közé eső számot! Beolvasáskor ellenőrizzük, hogy a
# megadott tartományban legyenek a számok és ne legyenek egyenlők! Ha nem megfelelő
# számot kap a program, akkor küldjön egy figyelmeztető üzenetet és kérje be ismét!
# Írjunk ki a számokat egymás alá a megadott kisebbtől a nagyobbik felé haladva és tegyünk
# melléjük annyi csillagot, amekkora a szám nagysága!
# Kérem az egyik 10 és 20 közé eső számot: 15
# Kérem a másik 10 és 20 közé eső számot: 12
# 12:************
# 13:*************
# 14:**************
# 15:***************

egyikSzám = int(input("Kérem az egyik 10 és 20 közé eső számot: "))
while egyikSzám < 10 and egyikSzám > 20:
    print("Nem megfelelő szám!")
    egyikSzám = int(input("Kérem az egyik 10 és 20 közé eső számot: "))

másikSzám = int(input("Kérem a másik 10 és 20 közé eső számot: "))
while másikSzám < 10 and másikSzám > 20:
    print("Nem megfelelő szám!")

kezd = 0
vég = 0
# kezd = vég = 0

if egyikSzám <= másikSzám:
    kezd = egyikSzám
    vég = másikSzám
else:
    kezd = másikSzám
    vég = egyikSzám

for i in range(kezd, vég + 1):
    print(str(i) + ':' + i*'*')
    # python-ban szöveget lehetséges egy egész számmal összeszorozni,
    # így a szöveg annyiszor kerül egymás mellé amekkora számmal került szorzásra
