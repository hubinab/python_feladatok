Max = 2.5
Beka = 3.5
Ossz = 0.0

DeciBe = input("Hány decit ittál? ")

while DeciBe != "":

    DeciBeLiter = int(DeciBe) / 10
    Ossz = Ossz + DeciBeLiter
    
    print(f"Már {Ossz:.1f} litert ittál!")

    if Ossz >= Max:
        print("Sikerült elérned a", Max, "litert!")
    
    if Ossz >= Beka:
        print("Béka nő a hasadba")

    DeciBe = input("Hány decit ittál? ")
