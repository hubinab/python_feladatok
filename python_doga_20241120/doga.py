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
#-----------------------------------------------------------------------
telepulesek = []

telepules = " "
while telepules != "":
    telepules = input("Kérem adja meg a település nevét: ")
    if telepules != "":
        telepulesek.append(telepules)

lakokszama = []
for i in range(len(telepulesek)):
    lakokszama.append(input(f"Adja meg a(z) {telepulesek[i]} településen élők számát: "))

sum = 0
for i in range(len(telepulesek)):
    sum += int(lakokszama[i])

print("A településeken lakók száma összesen: ", sum)

torpefalu = 100
for i in range(len(telepulesek)):
    if int(lakokszama[i]) < torpefalu:
        print(f"A(z) {telepulesek[i]} törpefalu")

karakterek = input("Adj be egy karaktersorozatot: ")
for i in range(len(telepulesek)):
    if karakterek.casefold() in telepulesek[i].casefold():
        print(f"A(z) {telepulesek[i]} a megadott({karakterek}) karaktersorozattal kezdődik")

min = 0
for i in range(len(telepulesek)):
    if int(lakokszama[i]) < min or min == 0:
        min = int(lakokszama[i])

print("A legkevesebb lakossal rendelkező település: ", min)
