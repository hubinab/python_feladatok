import random


csomagok = []

for i in range(12):
    csomagok.append(random.randint(0,50))
    # print(f"{i+1}. óra: {csomagok[i]} db csomag")

for i in range(len(csomagok)):
    print(f"{i+1}. óra: {csomagok[i]} db csomag")


#2. feladat

összeg=0
for i in range(len(csomagok)): #i = 0,1,2,3,4...
    összeg += csomagok[i]

# for óra in csomagok: #óra = csomagok[0],csomagok[1]....
#     összeg += óra

print(f"A futár összesen {összeg} db csomagot szállított ki.")


#3. feladat

print(f"Átlagosan óránként {összeg/len(csomagok):.1f} db csomagot szállított ki.")
# print(f"Átlagosan óránként {round(összeg/len(csomagok),1)} db csomagot szállított ki.")


#4. feladat

hárommalOszthatóDarab=0
for i in range(len(csomagok)):
    if csomagok[i] % 3 == 0:
        hárommalOszthatóDarab += 1

print(f"{hárommalOszthatóDarab} órában volt hárommal osztható csomag mennyiség.")


#5. feladat

print(f"{összeg*200} borravalót kapott.")


#6. feladat

üresjáratDarab=0
for i in range(len(csomagok)):
    if csomagok[i] == 0:
        üresjáratDarab += 1

if üresjáratDarab > 0:
    print(f"{üresjáratDarab} órában nem sikerült csomagot kiszállítani.")
else:
    print("Minden órában sikerült kiszálítani csomagot.")