# Készítsen  programot  a  karácsonyi  kiadásokról!   programban  a  barátok  ajándékaira  szánt 
# összegek, illetve a barátok nevei külön-külön listában szerepelnek. 
# A  kiírásoknál  kövesse  a  lenti  mintát,  figyeljen  rá,  hogy  a  feladat  sorszáma  jelenjen  meg  a 
# megoldás előtt! 




# Kérje be a felhasználótól a barátok számát!
barátok_száma = int(input("Kérlek add meg a barátok számát: "))

# Kérje be a barátok teljes nevét (vezeték- és keresztnév) és tárolja el egy listába!
barátok_nevei = []
for i in range(barátok_száma):
    barátok_nevei.append(input(f"Kérlek add meg a {i+1} barát nevét"))

# Kérje be és egy tárolja el másik listába az ajándékra szánt összegeket!
ajándék_összegek = []
for i in range(barátok_száma):
    ajándék_összegek.append(int(input(f"Kérlek add meg az {i+1} barát ajándékára szánt összeget:")))

# írja ki a képernyőre, mennyi pénzt költ a felhasználó összesen ajándékokra?
összes_költség = sum(ajándék_összegek)
print(f"Összesen {összes_költség} Ft-t költöttek el")

# Írja ki a képernyőre, ki kapja a legnagyobb összegű ajándékot és hány Ft értékben!
max_ajándék = max(ajándék_összegek)
print(f"A legnagyobb összegű ajándékot {barátok_nevei.index(max_ajándék)} adta")

# Kinek van a legrövidebb neve és hány betű!
min_nev = min(barátok_nevei, key=len(barátok_nevei))
min_nev_index = barátok_nevei.index(min_nev)


