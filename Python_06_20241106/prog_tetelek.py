# sulipy.hu -> Alapvető algoritmusok

napi_ertesitesek = [3, 12, 3, 4, 7, 15, 1]

# --------------------------------------------------------------
# Összegzés tétele (sum)
# Listában levő elemek összegét adja vissza
# --------------------------------------------------------------

osszeg = 0

for i in range(len(napi_ertesitesek)): # 0, 1, 2, 3, ...
    osszeg += napi_ertesitesek[i]

# másik módszer, itt nincs index változó, 
# az ertekesites változóban a lista elemeinek értékei jelennek meg
osszeg2 = 0
for ertekesites in napi_ertesitesek: # 3, 12, 3, 4, 7, 15, 1
    osszeg2 += ertekesites


# "f" string a {}-be bármit be lehet írni, ami ad vissza értéket
print(f"Összeg: {osszeg}")

print(f"Átlag: {osszeg/len(napi_ertesitesek)}")

# kerekítve:
print(f"Átlag: {round(osszeg/len(napi_ertesitesek), 2)}")

# Ez ugyan azt csinálja, mint a round
print(f"Átlag: {osszeg/len(napi_ertesitesek):.2f}")

# Ez ugyan azt csinálja, mint a round
print(f"Összeg2: {osszeg2}")
print(f"Átlag2: {osszeg2/len(napi_ertesitesek):.2f}")

# --------------------------------------------------------------
# Kereses listaban
# Eldontes tetele
# --------------------------------------------------------------

# Ha megtalaltam az elemet, akkor nem keresem tovább
i = 0
keresett = 4

while i < len(napi_ertesitesek) and napi_ertesitesek[i] != keresett:
    i += 1

print(i)

if i < len(napi_ertesitesek):
    print("van ilyen elem!")
else:
    print("Nincs ilyen elem!")

#----------------------------------------------------------------
# Megszamlalas tetele
#----------------------------------------------------------------
#  A keresett elem hányszor van a listában
harommaloszthatodb = 0
for i in range(len(napi_ertesitesek)):
    if napi_ertesitesek[i] % 3 == 0: #  ha a szám 3-mal osztható
        harommaloszthatodb += 1

print(f"Harommal osztható szamok a listában: {harommaloszthatodb}")

#----------------------------------------------------------------
# Szelsőérték keresés tétele
#----------------------------------------------------------------
#maxertek = napi_ertesitesek[maxhely]
#for i in range(1, len(napi_ertesitesek)):
    #if maxertek < napi_ertesitesek[i]:
#    if napi_ertesitesek[maxhely] < napi_ertesitesek[i]:
        #maxertek = napi_ertesitesek[i]


maxhely = 0
for i in range(1, len(napi_ertesitesek)):
    if napi_ertesitesek[maxhely] < napi_ertesitesek[i]:
        maxhely = i

print(f"Maximum érték: {napi_ertesitesek[maxhely]}")

# minimum eretek

minhely = 0
for i in range(1, len(napi_ertesitesek)):
    if napi_ertesitesek[minhely] > napi_ertesitesek[i]:
        minhely = i

print(f"Minimum érték: {napi_ertesitesek[minhely]}")

# utolsó minimum hely keresése
minhely = 0
for i in range(1, len(napi_ertesitesek)):
    if napi_ertesitesek[minhely] >= napi_ertesitesek[i]:
        minhely = i

print(f"Minimum érték: {napi_ertesitesek[minhely]}")

