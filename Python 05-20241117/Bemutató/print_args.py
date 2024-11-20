# lista = ["alma","körte","zsömle"]

# print("alma","körte","zsömle", sep=";\n")

# for i in range(10):
#     print(i, end=", ")
# print()

# print(*lista, sep=";")

# kor = 74
# print(f"Pisi {kor} éves.")


napi_ertekesitesek = [3, 12, 3, 4, 7, 15, 1]

#Összegzés tétele
összeg=0
for i in range(len(napi_ertekesitesek)):
    # összeg = összeg + napi_ertekesitesek[i]
    összeg += napi_ertekesitesek[i]
print(összeg)


összeg=0
for érték in napi_ertekesitesek:
    # összeg = összeg + napi_ertekesitesek[i]
    összeg += érték
print(összeg)

print(f"A számok átlaga: {round(összeg/len(napi_ertekesitesek),2)}")
print(f"A számok átlaga: {összeg/len(napi_ertekesitesek):.2f}")


#Eldöntés tétele
#Van-e benne hárommal osztható szám?

index=0
találat=False

while index < len(napi_ertekesitesek) and not találat:
    if napi_ertekesitesek[index] % 3 == 0:
        találat=True
    index += 1

if találat:
    print("Volt benne hárommal osztható!")
else:
    print("Nem volt benne hárommal osztható!")


# index=0
# while index < len(napi_ertekesitesek) and napi_ertekesitesek[index] % 3 != 0:
#     index += 1

# if index < len(napi_ertekesitesek):
#     print("Volt benne hárommal osztható!")
# else:
#     print("Nem volt benne hárommal osztható!")


#Szélsőérték kiválasztás tétele



minh=0
min=napi_ertekesitesek[minh]
for i in range(len(napi_ertekesitesek)):
    if napi_ertekesitesek[i] <= min:
        min = napi_ertekesitesek[i]
        minh = i
print(min)


min=napi_ertekesitesek[0]
for érték in napi_ertekesitesek:
    if érték < min:
        min = érték
print(min)





max=napi_ertekesitesek[0]
for i in range(len(napi_ertekesitesek)):
    if napi_ertekesitesek[i] > max:
        max = napi_ertekesitesek[i]
print(max)


max=napi_ertekesitesek[0]
for érték in napi_ertekesitesek:
    if érték > max:
        max = érték
print(max)



