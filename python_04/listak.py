# változók gyűjteménye más néven tömb csak ez dinamikusan változik,
# itt nincs is fix tömb csak ez
# típusok változhatnak
nevsor = ["Kis Béla", "Nagy Endre", "Varga Géza"]

# üres lista
nevsor2 = []

ember = ["Nagy Endre", 84, False]  # típusok változhatnak

# egyenlőre mi ne keverjük

# érték kiolvasása 0-val kezdődik

print(nevsor[0], nevsor[2])

# Ha nincs olyan index, akkor hibát dob!

# mindenki kiírása a len visszaadja, hogy milyenhosszú a lista (itt 3)

for i in range(len(nevsor)):
    print(nevsor[i])

# (for each) itt a nev felveszi egymas utan az elemeket egy listából
# itt az indexet nem tudjuk
for nev in nevsor:
    print(nev)

# alul zárt felül nyitott intervallumot lehet megadni
# Ha elhagyom a második számot, akkor az első számtól mindent kiír
# listát ad vissza
print(nevsor[0:2]) # első kettőt
print(nevsor[1:2]) # csak a másodikat
print(nevsor[1:]) # második és harmadikat írja ki

# hármat is meg lehet adni, mint a range-nél
print(nevsor[::2]) # minden másodikat ír ki (0-tól)

# negatív számot is megadhatunk, akkor a végétől kezdve számol
print(nevsor[-1]) # ez a legutolsó elem
print(nevsor[-2]) # ez a utolsó előtti és így tovább
print(nevsor[-2:]) # utolsó kettőt
print(nevsor[::-2]) # Visszafelé minden másodikat
print(nevsor[::-1]) # visszafelé mindent

# Az AI adta ezt ------->
# listában a legnagyobb elemet keresi
print(max(nevsor))
# listában a legkisebb elemet keresi
print(min(nevsor))
# listában a legnagyobb elem indexét keresi
print(nevsor.index(max(nevsor)))
# listában a legkisebb elem indexét keresi
print(nevsor.index(min(nevsor)))
#<------ idáig az AI ajánlotta fel, ezeket nem tanította

# trükkös, a szöveg karakterek tömbje!
# így minden fenti művelet ezeken elvégehető
szoveg = "Alma"
print(szoveg[2])

nevsor[0] = "Kiss Béla" # dupla s
print(nevsor) # a lista módosult

# ezt a fentit a sima szöveg nem támogatja (azt a replace függvénnyel lehet)
#szoveg [2] = "x" # ez nem működik!

# fordítva írja ki a szoveg-et
print(szoveg[::-1])

# új elem hozzáadása
nevsor.append("Vég Béla")
print(nevsor)

nevsor.pop(1)
print(nevsor) # a második elemet törli

print(nevsor.pop(0)) # visszaadja azt az elemet, amit kivesz!
print(nevsor) #  a lista módosult



