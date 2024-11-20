import random

csomagok = []

for i in range(12):
    #csomagrandom = random.randint(0,50)
    #csomagok.append(csomagrandom)
    #print(f"{i+1}. óra: {csomagrandom}")

    csomagok.append(random.randint(0,50))
    print(f"{i+1}. óra: {csomagok[i]}")

# Hány csomagot szállított ki
# sum
csomag_osszes=0
for i in range(len(csomagok)):
    csomag_osszes += csomagok[i]

print(f"Összesen {csomag_osszes} csomagot szállított ki!")

# Átlagosan hány csomagot szállított ki óránként
print(f"Óránként átlagosan {csomag_osszes/len(csomagok):.1f} db csomagot szállított ki!")

# Hány olyan volt, mikor 3-al osztható csomagot szállított ki
harommaloszthatodb = 0
for i in range(len(csomagok)):
    if  csomagok[i] % 3 == 0:
        harommaloszthatodb += 1

print(f"Harommal osztható csomagot {harommaloszthatodb} alkalommal szálított ki!")

# borravaló
print(f"A futár {csomag_osszes*200} Ft borravalót kapott!")

# Üresjárat
#print(f"Üresjárat {csomagok.count(0)} alkalommal")
uresjaratdb = 0
for i in range(len(csomagok)):
    if  csomagok[i] == 0:
        uresjaratdb
print(f"Üresjárat {uresjaratdb} alkalommal volt")


