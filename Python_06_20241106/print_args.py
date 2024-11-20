# Print függvény bonyolítása

# mi legyen a szöveg vége 
print("kutya", end="")
print("kutya", end="")
print("kutya", end="")
print("kutya", end="")
print("kutya", end="")

print("kutya", end=";;")
print("kutya", end=";;")
print("kutya", end=";;")
print("kutya", end=";;")
print("kutya", end=";;")

print("kutya", end=";\n")
print("kutya", end=";\n")
print("kutya", end=";\n")
print("kutya", end=";\n")
print("kutya", end=";\n")

print("kutya", end=";\n\t")
print("kutya", end=";\n")
print()

# mi legyen az elválasztás
print("alma", "körte", "meggy", sep=":")
print("alma", "körte", "meggy", sep=";\t")

print()

# Lehet variálni is
print("alma", "körte", "meggy", sep="\t", end="")
print("alma", "körte", "meggy", sep="\t", end="")
print("alma", "körte", "meggy", sep="\t", end="")
print("alma", "körte", "meggy", sep="\t")

# listáknál

nevek = ["Béla", "Éva", "Zoé"]

print(nevek)

# egymas alá
for elem in nevek:
    print(elem)

# egymas mellé ;-vel
for elem in nevek:
    print(elem, end=";")    

# ugyan az for nélkül
print()
print(nevek, sep=';')

# ez a jó
print()
# a *-al lehet csak az értékeket kiszaedni (alapból space az elválasztás)
print(*nevek)
# a sep-nek megadjuk a ;-t és kész a .csv :)
print(*nevek, sep=';')
# visszafelé
print(*nevek[::-1], sep=';')

