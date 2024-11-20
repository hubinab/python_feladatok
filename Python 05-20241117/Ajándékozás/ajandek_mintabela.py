baratokDB = int(input("1. feladat Adja meg a barátok számát: "))


print("2. feladat")
baratokNevek = []
for i in range(baratokDB):
    baratokNevek.append(input(f"\t{i+1}. barát teljes neve: "))


print("3. feladat")
baratokÖsszegek = []
for i in range(baratokDB):
    baratokÖsszegek.append(int(input(f"\t{i+1}. ajándék összege: ")))


# összeg = 0
# for i in range(len(baratokÖsszegek)):
#     összeg += baratokÖsszegek[i]

összeg = 0
for baratÖsszeg in baratokÖsszegek:
    összeg += baratÖsszeg

print(f"4. feladat Összesen {összeg} Ft-ot költött ajándékokra.")


maxHely = 0
for i in range(len(baratokÖsszegek)):
    if baratokÖsszegek[i] > baratokÖsszegek[maxHely]:
        maxHely = i

print(
    f"5. feladat A legnagyobb ajándékot {baratokNevek[maxHely]} kapja, {baratokÖsszegek[maxHely]} Ft értékbe.")


minHely = 0
for i in range(len(baratokNevek)):
    if len(baratokNevek[i]) < len(baratokNevek[minHely]):
        minHely = i

print(
    f"6. feladat A legrövidebb nevű barát: {baratokNevek[minHely]}, {len(baratokNevek[minHely])} karakter hosszú.")


keresettNév = input("7. feladat Adja meg a keresztnevet: ")
névDB = 0
# for i in range(len(baratokNevek)):
#     # -1 az utolsó elem a listában így nem teljes név esetén is működik.
#     # 1-el a második elemet vizsgálnánk azonban ha nincs második név kiindexelünk a listából.
#     if keresettNév == baratokNevek[i].split(' ')[-1]: 
#         névDB += 1

for név in baratokNevek:
    # -1 az utolsó elem a listában így nem teljes név esetén is működik.
    # 1-el a második elemet vizsgálnánk azonban ha nincs második név kiindexelünk a listából.
    if keresettNév == név.split(' ')[-1]:
        névDB += 1

if névDB > 0:
    print(f"\t{névDB} db ilyen keresztnevű barát van.")
else:
    print("\tNincs ilyen keresztnevű barát.")


rövidNévDB = 0
# for i in range(len(baratokNevek)):
#     if len(baratokNevek[i].split(' ')) < 2:
#         rövidNévDB += 1

for név in baratokNevek:
    if len(baratokNevek[i].split(' ')) < 2:
        rövidNévDB += 1

print(f"8. feladat {rövidNévDB} barát van, akinek nem a teljes neve szerepel.")


# print(f"9. feladat Átlagosan {round(összeg/len(baratokÖsszegek),2)} Ft-ot értékben ad ajándékot.")
print(
    f"9. feladat Átlagosan {összeg/len(baratokÖsszegek):.2f} Ft-ot értékben ad ajándékot.")


print("10. feladat")
# baratokÖsszegekDupla = []
# for i in range(len(baratokÖsszegek)):
#     baratokÖsszegekDupla.append(baratokÖsszegek[i]*2)
#     print(f"\t{baratokNevek[i]} {baratokÖsszegekDupla[i]} Ft értékben kap ajándékot.")

# baratokÖsszegekDupla = []
# for i in range(len(baratokÖsszegek)):
#     baratokÖsszegekDupla.append(baratokÖsszegek[i]*2)

baratokÖsszegekDupla = []
for baratÖsszeg in baratokÖsszegek:
    baratokÖsszegekDupla.append(baratÖsszeg*2)

for i in range(len(baratokNevek)):
    print(f"\t{baratokNevek[i]} {baratokÖsszegekDupla[i]} Ft értékben kap ajándékot.")