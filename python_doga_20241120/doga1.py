import random

nev = input("Add meg a teljes neved: ")
allat = input("Add meg a kedvenc állatod nevét: ")

vezeteknev = nev.split(" ")[0]
keresztnev = nev.split(" ")[1]
gen_szam = random.randint(1000, 9999)

jelszo1 = vezeteknev[-3:].upper()
jelszo2 = keresztnev[3:].lower()

print("Jelszó: ", jelszo1+jelszo2+str(gen_szam), end="")

for i in range(6):
    print(random.choice(allat), end="")
