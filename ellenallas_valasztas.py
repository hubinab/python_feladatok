# Választható ellenállások:
E6 = [1, 1.5, 2.2, 3.3, 4.7, 6.8]
E12 = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]

# Teljesítmény sor
P_List = [0.125, 0.25, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Az összes E6-os ellenállás meghatározása:
E6_full = []
for i in range(4):
    for j in range(len(E6)):
        E6_full.append(round(E6[j]*10**i,1))
#print(E6_full)

# Az összes E12-es ellenállás meghatározása:
E12_full = []
for i in range(4):
    for j in range(len(E12)):
        E12_full.append(round(E12[j]*10**i,1))
#print(E12_full)

print("-"*30)
print(f"A program E6-os ellenállásból, maximum {max(E6_full)} Ohmot tud,")
print(f" míg E12-es ellenállásból, maximum {max(E12_full)} Ohmot tud.")
print("A bevitt értékeket nem ellenőrzi! A tizedest .-al kell megadni!")
print("-"*30)

# A fogyasztó feszültsége voltban
UF = float(input("A fogyasztó feszültség esése (UF) voltban: "))
# Áramerősség (áram intenzitása) mA-ban
I = float(input("Az áram intenzitása(I) mA-ben: "))
# Maximum vagy nem maximum az áram:
MAX = input("Maximum ([I]gen/[N]em):")
# A betáplált feszültség (voltban):
UT = float(input("Táp (UT) feszültség voltban: "))

if MAX == "I":
    MAX = True
else:
    MAX = False

# Keressük, hogy mekkora ellenállás (R) szükséges a fogyasztóhoz elméletileg.
# És, hogy mekkora teljesítményű (P) legyen az ellenállás Watt-ban.
R = 0
P = 0

# Kirchhoff hurok törvénye:
# Bármely zárt hurokban a feszültségek előjeles összege nulla.
# Azaz -UT + UR + UF = 0, tehát UR = UT - UF
# Azaz ekkora feszültség esés kell az ellenálláson, hogy a 
# fogyasztó elbírja
UR = UT - UF

# Ohm törvénye R = U/I, U = R * I, I = U/R
# Jelen esetben az ellenállást (R) keressük
# R = UR/I. A mA miatt be kell szorozni 1000-el a feszültséget
R = (UR*1000)/I

# Teljesítmény P=U*I (mivel mA-t kértem ezért ez itt mW lesz)
# Itt az ellenállás teljesítményét keressük ezért:
P = UR*I

print("-"*30)
print(f"Elméleti Feszültségesés az ellenálláson: {round(UR,2)} volt")
print(f"Elméletileg szükséges ellenállás: {round(R,2)} Ohm")
print(f"Elméletileg szükséges teljesítmény: {round(P,2)} mW")
print("-"*30)

# Megkeressük a teljesítmény listában, hogy melyik
# van a legközelebb, ami egyenlő vele vagy magyobb nála:
P_keres = 0
for i in range(len(P_List)):
    # A listában W-ban van, ezért 1000-el osztjuk a kiszámolt P-t
    if P_List[i] >= P/1000: 
        P_keres = P_List[i]
        break
print("Ellenállás teljesítménye legyen: ", P_keres, "W")

# Megkeressük a legkisebb és legnagyobb értékűt az E6-ban és E12-ben
# Majd kiírjuk ezeket, amelyekből lehet választani.
E6_min = 0
E6_max = 0
E12_min = 0
E12_max = 0

for i in range(len(E6_full)):
    if E6_full[i] <= R:
        E6_min = E6_full[i]
    if E6_full[i] >= R:
        E6_max = E6_full[i]
        break
        
for i in range(len(E12_full)):
    if E12_full[i] <= R:
        E12_min = E12_full[i]
    if E12_full[i] >= R:
        E12_max = E12_full[i]
        break

if not MAX:
    print(f"Az E6-os ellenállások közül a legkisebb ami még megfelel: {E6_min} Ohm.")
    print(f"Az E12-es ellenállások közül a legkisebb ami még megfelel: {E12_min} Ohm.")

print(f"Az E6-os ellenállások közül a legnagyobb ami még megfelel: {E6_max} Ohm.")
print(f"Az E12-es ellenállások közül a legnagyobb ami még megfelel: {E12_max} Ohm.")
