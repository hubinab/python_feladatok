Szam = int(input("Kérek egy egész számot: "))

Maradek_3 = Szam % 3
Maradek_5 = Szam % 5

if Maradek_3 == 0 and Maradek_5 == 0:
    print("FizzBuzz")
elif Maradek_3 == 0:
    print("Fizz")
elif Maradek_5 == 0:
    print("Buzz")
else:
    print(str(Szam))

