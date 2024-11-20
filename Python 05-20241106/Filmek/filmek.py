import random


filmek = []

filmBe = "start"
while filmBe != "":
    # "Enterrel jelzi" => egy üres sort küld a felhasználó ez üres stringként jelenik meg.
    filmBe = input("Kérem adja meg a film címét: ")
    filmek.append(filmBe)


# Rendezéseket később vesszük, most használható a sorted függvény.
# Ez egy új rendezet listát ad vissza a bemeneti listát nem módosítja.
filmekRendezett = sorted(filmek)
# for i in range(len(filmekRendezett)):
#     print(filmekRendezett[i].lower())

for film in filmekRendezett:
    print(film.lower())


keresettFilm = input("Adja meg a keresett: ")
i = 0
while i < len(filmek) and not (keresettFilm in filmek[i].casefold()):
    i += 1
if i < len(filmek):
    print("Van ilyen film a listában.")
else:
    print("Nincs ilyen film a listában.")


hanyadikFilm = input("Adja meg hanyadik filmcímre kiváncsi: ")
print(f"{hanyadikFilm}. film: {filmek[hanyadikFilm-1]}")
print(f"Összesen {len(filmek[hanyadikFilm-1])} karakter.")


azDB = 0
# for i in range(len(filmek)):
#     if filmek[i].casefold().startswith("az "):
#         # "az" utáni szóközzel biztosítjuk hogy csak "az" szóval kezdődő
#         # filmeket vizsgáljuk és nem "az" karakterekkel kezdődőket
#         azDB += 1

# for i in range(len(filmek)):
#     if filmek[i].split(' ')[0].casefold() == "az":
#         # szóközök mentén feldarabolva elég csak az első elemet vizsgálni
#         azDB += 1

# for film in filmek:
#     if film.casefold().startswith("az "):
#         azDB += 1

for film in filmek:
    if film.split(' ')[0].casefold() == "az":
        azDB += 1


összKarakterSzám = 0
# for i in range(len(filmek)):
#     összKarakterSzám += len(filmek[i])

for film in filmek:
    összKarakterSzám += len(film)

# print(f"A filmek címek átlagos hossza {round(összKarakterSzám/len(filmek), 2)} karakter.")
print(f"A filmek címek átlagos hossza {összKarakterSzám/len(filmek):.2f} karakter.")


# véletlenFilm = filmek[random.randint(0, len(filmek)-1)]
véletlenFilm = random.choice(filmek)

jelszó_a = véletlenFilm[::-2].upper()
jelszó_b = véletlenFilm[:3]
jelszó_c = str(len(filmek))

jelszó = jelszó_c + jelszó_a + jelszó_b
print(jelszó)