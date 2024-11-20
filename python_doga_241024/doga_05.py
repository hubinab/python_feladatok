gondolt_szam = 78
szam = 0

while szam != gondolt_szam:
    szam = int(input("Kérek egy számot 1-100-ig: "))

    if szam < 1:
        print("Túl kis számot adtál meg!")
    
    if szam > 100:
        print("Túl nagy számot adtál meg!")

    if szam > gondolt_szam:
        print("Kisebb számot adj meg")

    if szam <  gondolt_szam:
        print("Nagyobb számot adj meg")

print("Kitaláltad! Nagyon ügyes vagy!")
