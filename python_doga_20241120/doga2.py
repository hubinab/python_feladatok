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
db = 0
for i in range(len(telepulesek)):
    if telepulesek[i].casefold().startswith(karakterek.casefold()):
        print(f"A(z) {telepulesek[i]} a megadott({karakterek}) karaktersorozattal kezdődik")
        db += 1
print(db, "település kezdődik a megadott karakterrel.")

min = 0
for i in range(len(telepulesek)):
    if int(lakokszama[i]) < min or min == 0:
        min = int(lakokszama[i])

print("A legkevesebb lakossal rendelkező település: ", min)
