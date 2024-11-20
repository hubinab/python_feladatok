napi_ertekesitesek = [3, 12, 3, 4, 7, 15, 1]


#Összegzés tétele

összeg = 0
for i in range(len(napi_ertekesitesek)): # 0, 1, 2, 3,...
    összeg += napi_ertekesitesek[i]

# összeg = 0
# for értékesítés in napi_ertekesitesek: # 3, 12, 3, 4, 7....
#     összeg += értékesítés

szöveg = "Összeg: "
print(f"{szöveg}{összeg}")

print(f"Átlag: {round(összeg/len(napi_ertekesitesek), 2)}")
print(f"Átlag: {összeg/len(napi_ertekesitesek):.2f}")


#Eldöntés tétele

i = 0
keresett = 4
while i < len(napi_ertekesitesek) and napi_ertekesitesek[i] != keresett:
    i += 1

if i < len(napi_ertekesitesek):
    print("Van ilyen elem.")
else:
    print("Nincs ilyen elem.")


#Megszámlálás tétele

hárommalOszthatóDb = 0
for i in range(len(napi_ertekesitesek)):
    if napi_ertekesitesek[i] % 3 == 0:
        hárommalOszthatóDb += 1


#Szélsőérték keresés tétele


# maxÉrték = napi_ertekesitesek[maxHely]
# for i in range(1, len(napi_ertekesitesek)):
    # if napi_ertekesitesek[i] > maxÉrték:
        # maxÉrték = napi_ertekesitesek[i]

maxHely = 0
for i in range(1, len(napi_ertekesitesek)):
    if napi_ertekesitesek[i] > napi_ertekesitesek[maxHely]:
        maxHely = i

print(f"Max: {napi_ertekesitesek[maxHely]}")


minHely = 0
for i in range(1, len(napi_ertekesitesek)):
    if napi_ertekesitesek[i] < napi_ertekesitesek[minHely]:
        minHely = i



nevek = [] #["Béla", "Éva", "Zoé"]
# nevek.append(5)
nevek.append("Béla")
nevek.append("Éva")
nevek.append("Zoé")
név = nevek[0].lower()