# Készítsen  programot  a  karácsonyi  kiadásokról!   programban  a  barátok  ajándékaira  szánt 
# összegek, illetve a barátok nevei külön-külön listában szerepelnek. 
# A  kiírásoknál  kövesse  a  lenti  mintát,  figyeljen  rá,  hogy  a  feladat  sorszáma  jelenjen  meg  a 
# megoldás előtt! 

# Kérje be a felhasználótól a barátok számát!
baratok_szama = int(input("1. feladat Add meg a barátok számát: "))

# Kérje be a barátok teljes nevét (vezeték- és keresztnév) és tárolja el egy listába!
print ("2. feladat")
baratok_nevei = []
for i in range(baratok_szama):
    baratok_nevei.append(input(f"\t{i+1}. barát teljes neve: "))

# Kérje be és egy tárolja el másik listába az ajándékra szánt összegeket!
print ("3. feladat")
ajandek_osszegek = []
for i in range(baratok_szama):
    ajandek_osszegek.append(int(input(f"\t{i+1}. barát ajándékára szánt összege:")))

# írja ki a képernyőre, mennyi pénzt költ a felhasználó összesen ajándékokra?
print(f"4. feladat Összesen {sum(ajandek_osszegek)} Ft-t költöttek el.")

# Írja ki a képernyőre, ki kapja a legnagyobb összegű ajándékot és hány Ft értékben!
for i in range(baratok_szama):
    if ajandek_osszegek[i] == max(ajandek_osszegek):
        print(f"5. feladat A legnagyobb ajándékot {baratok_nevei[i]} kapja, {ajandek_osszegek[i]} Ft értékben.")

# Kinek van a legrövidebb neve és hány betű!
sh_nev = len(baratok_nevei[0])
sh_ind = 0
for i in range(1, baratok_szama):
    if len(baratok_nevei[i]) < sh_nev:
        sh_nev = len(baratok_nevei[i])
        sh_ind = i

print(f"6. feladat A legrövidebb nevű barát: {baratok_nevei[sh_ind]}, {len(baratok_nevei[sh_ind])} karakter hosszú.")

# Kérjen be egy keresztnevet és írja ki hány ilyen keresztnevű barátja van!
keresztnev = input("7. feladat Adj meg egy keresztnevet: ")

db1 = 0
db2 = 0
for i in range(baratok_szama):
    if len(baratok_nevei[i].split(" ")) == 1:
        db2 += 1
    else:
        if baratok_nevei[i].split(" ")[1] == keresztnev:
            db1 += 1


if db1 > 0:
    print(f"\t{db1} barátja van ezzel a keresztnévvel: {keresztnev}.")
else:
    print(f"\tNincs barátja ezzel a keresztnévvel: {keresztnev}.")

# Írja ki, hányan vannak, akiknek nem a teljes neve szerepel listában!
print(f"8. feladat {db2} barátja van, akinek nem a teljes neve szerepel a listában.")

# Írja ki, hogy átlagosan hány forintot szán az ajándékozásra egy barátnak! 
print(f"9. feladat Átlagosan {round(sum(ajandek_osszegek)/baratok_szama,2)} Ft-ot szán az ajándékozásra egy barátnak.")

# A karácsonyi ajándékra szánt összegeket növelje meg kétszeresére és az eredményt új listába tárolja!
# Végül jelenítse meg, ki milyen összegben kap ajándékot!
print("10. feladat")
uj_ajandek_osszegek = []
for i in range(baratok_szama):
    uj_ajandek_osszegek.append(ajandek_osszegek[i]*2)
    print(f"\t{baratok_nevei[i]} barát ajándékára szánt összege: {uj_ajandek_osszegek[i]} Ft")
