import math

#1. Feladat
print("Hello, world!")

#2. Feladat
név = input("Szia, hogy hívnak? ")
print("Hello, " + név + "!")
print("Hello,", név, "!", 55)

#3. Feladat
sugár = float(input("Kérem a gömb sugarát! "))
felszín = 4 * sugár**2 * math.pi
térfogat = (4 * sugár**3 * math.pi)/3

#print("A gömb felszíne: " + str(felszín))
print("A gömb felszíne:", felszín)
print("A gömb térfogata:", térfogat)


#4. Feladat
szám = int(input("Kérek egy egész számot! "))

if szám % 2 == 0:
    print("Ez a szám páros!")
else:
    print("Ez a szám páratlan!")
"""
if szám % 2 == 0:
    print("Ez a szám páros!")
elif szám % 2 != 0:
    print("Ez a szám páratlan!")

if szám % 2 == 0:
    print("Ez a szám páros!")
else:
    if szám % 2 != 0:
        print("Ez a szám páratlan!")
"""


#5. Feladat
if szám % 3 == 0 & szám % 5 == 0:
    print("FizzBuzz")
else:
    if szám % 3 == 0:
        print("Fizz")
    else:
        if szám % 5 == 0:
            print("Buzz")
        else:
            print(szám)

"""
if szám % 3 == 0 & szám % 5 == 0:
    print("FizzBuzz")
elif szám % 3 == 0:
        print("Fizz")
elif szám % 5 == 0:
    print("Buzz")
else:
    print(szám)
"""