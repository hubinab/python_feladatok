import random
# Kérje be egyesével a felhasználótól a kedvenc filmjeinek címét és tárolja el listában!
# A felhasználó Enterrel jelzi, ha már nem akar több címet megadni!

film = ""
filmek = []
while True:
    film = input("Kérem adja meg a kedvenc filmjét: ")
    if film == "":
        break
    filmek.append(film)

# Írja ki a képernyőre a filmcímeket ábécé sorrendben, kisbetűs formában úgy, hogy az
# eredeti lista ne módosuljon!
filmek_kisbetu = sorted(filmek, key=str.lower)
for film in filmek_kisbetu:
    print(film.lower())

# Kérjen be a felhasználótól egy filmcímet és vizsgálja meg, hogy benne van-e a
# listában! Mindkét esetben tájékoztassa a felhasználót!
film = input("Kérem adjon meg egy film címet: ")
if film in filmek:
    print("A lista tartalmazza a film címét!")
else:
    print("A lista nem tartalmazza a film címét!")

# Kérje be felhasználótól, hogy hányadik filmcímre kíváncsi!
# Írja ki a kiválasztott címet és hogy hány karakterből áll!
filmkeres = int(input("Hányadik film címre kíváncsi? ")) - 1

if filmkeres < len(filmek):
    print(filmek[filmkeres])
    print(f"A film címe {len(filmek[filmkeres])} karakterből áll.")
else:
    print("Nincs ilyen film a listában!")

# Számolja meg, hány cím kezdődik az „az” szóval!
#azfilmek = [film for film in filmek if film.lower().startswith("az")]
azFilmek = 0
for film in filmek:
    if film.casefold().startswith("az"):
        azFilmek += 1

print(f"A listában {azFilmek} film címe kezdődik \"az\"-al")

# Számolja ki a címek átlagos hosszúságát és írja ki két tizedesjegy pontossággal!
atlagos_hossz = 0
for film in filmek:
    atlagos_hossz += len(film)

print(f"A film címek átlagos hossza {round(atlagos_hossz/len(filmek),2)}")

# Generáljon egy jelszót a következők alapján:
# A listából válasszon ki véletlenszerűen egy címet! Hátulról kezdve minden
# második karaktert fűzze össze és legyen az eredmény nagybetűs!
# Fűzze a végéhez a cím első három karakterét!
# A jelszó elejére pedig fűzze hozzá a filmcímek számát!
# Jelenítse meg a jelszót a képernyőn!

rand_film = random.choice(filmek)
print(f"{len(filmek)}{rand_film[::-2].upper()}{rand_film[:3]}")
