import math

Sugar = float(input ("Kérem a gömb sugarát: "))

Felszine = 4 * math.pi * Sugar ** 2
Terfogata = (4 * math.pi * Sugar ** 3) / 3

# Atalakitjuk str fuggvennyel
print("Térfogata: " + str(Terfogata))
print("Felszíne: " + str(Felszine))

# Felsorolas, ide nem kell space,
# mert alapbol tesz
print("Térfogata:", Terfogata)
print("Felszíne:", Felszine)

# AI altali 2-re kerekites
print(f"Térfogata: {Terfogata:.2f}")
print(f"Felszíne: {Felszine:.2f}")
