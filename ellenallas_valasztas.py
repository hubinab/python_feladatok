E6 = [1, 1.5, 2.2, 3.3, 4.7, 6.8]
E12 = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
P_List = [0.125, 0.25, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

E6_full = []
for i in range(4):
    for j in range(len(E6)):
        E6_full.append(round(E6[j]*10**i,1))

print(E6_full)

E12_full = []
for i in range(4):
    for j in range(len(E12)):
        E12_full.append(round(E12[j]*10**i,1))

print(E12_full)


U = float(input("Feszültség(U) voltban: "))
I = float(input("Intenzitás(I) mA-ben: "))
MAX = input("Maximum ([I]gen/[N]em):")
UT = float(input("Táp(UT) feszültség voltban: "))

if MAX == "I":
    MAX = True
else:
    MAX = False

# Kirchhoff hurok UT = UR + UF (UR = UT - UF)
UR = UT - U

# R = UR/I Ohm törvénye. mA miatt be kell szorozni 1000-el a feszültséget
R = (UR*1000)/I

# Teljesítmény P=U*I (mivel mA-t kértem ezért ez itt mW lesz)
P = UR*I

P_keres = 0
for i in range(len(P_List)):
    if P_List[i] <= P:
        P_keres = P_List[i]
        break

hol_talalt=""
R_keres = 0
E6_keres = 0
for i in range(len(E6_full)):
    if R <= E6_full[i] and MAX:
        E6_keres = E6_full[i]
        hol_talalt = "E6"
        break

R_keres = E6_keres

print("MAX =",MAX)
print("UR =",UR)
print("R =",R)
print("P =",P)
print("Ellenállás teljesítménye legyen: ", P_keres, "W")
print(f"Ellenállás értéke legyen, a(z) {hol_talalt} sorból {R_keres} Ohm")
