# Hozz létre egy listát, amely tartalmazza a számjegyeket (0,1,2,…,9)!
szamjegyek = []
for i in range(10):
    szamjegyek.append(i)

# Írd ki egymás mellé vesszővel elválasztva a számokat!
for i in range(len(szamjegyek)-1):
    print(szamjegyek[i], end=", ")
print(szamjegyek[i+1])

# Írd ki egymás alá a lista elemeit!
for szam in szamjegyek:
    print(szam)

# Jelenítsd meg a lista tartalmát egymás alatt visszafele!
for szam in szamjegyek[::-1]:
    print(szam)

# Írd ki egymás mellett megjelenítve minden második elemet!
print(*szamjegyek[::2], sep="")
