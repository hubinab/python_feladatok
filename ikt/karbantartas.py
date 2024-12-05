import kereses

def felvitel (szotar_lista):
    inp = ""
    i = 0
    nev = ""
    szev = ""
    fizu = ""
    stat = ""
    startev = 0
    inaktev = 0
    
    while inp != "#":
        print("Kilépéshez adja meg a # karaktert.")
        print("Kérem adja meg az alábbi adatokat.")
        inp = input("Alkalmazott neve: ")
        if inp == "#":
            break
        nev = inp
        inp = input("Alkalmazott születési éve: ")
        if inp == "#":
            break
        szev = int(inp)

        i = kereses.pri_keres(nev, szev, szotar_lista)
        if i != None:
            print("Már van ilyen alkalmazott.")
            continue

        inp = input("Alkalmazott fizetése: ")
        if inp == "#":
            break
        fizu = int(inp)
        stat = "AKTÍV"
        inp = input("Alkalmazott kezdő éve: ")
        if inp == "#":
            break
        startev = int(inp)
        szotar_lista.append ({"NEV":nev, "SZEV":szev, "FIZU":fizu, "STAT":stat, "STARTEV":startev, "INAKTEV":inaktev})
        print(f"A(z) {nev} alkalmazottat sikeresen felvettük.")
        print("---------------------------------")
        kereses.lista10(szotar_lista, False, len(szotar_lista)-1)

def modositas (szotar_lista):
    inp = ""
    i = 0
    fizu = ""
    startev = 0
    inaktev = 0

    while inp != "#":

        # A szamok-ba betesszuk a jelenlegi 
        # rekordok szamsorait listában
        # [1,2,3,4,5,...,1000,...]
        szamok = list(range(1, len(szotar_lista)+1))
        inp = kereses.lista10(szotar_lista, True, i)
        # ha benne van a szam amit megadott, 
        # akkor az lesz a kivalasztott rekord,
        # egyébként kilépünk (vagy #-et adott, vagy 
        # olyan számot amivel nem létezik rekord).
        # Azért kell a -1, mert 1-től listáztunk
        if inp in str(szamok):
            i = int(inp)-1
        else:
            break

        print("Kilépéshez adja meg a # karaktert.")
        print("Kérem adja meg az alábbi adatokat. Ha nem ad meg semmit, akkor az adat nem változik.")
        print(f"A(z) {szotar_lista[i]['NEV']}, {szotar_lista[i]['SZEV']} alkalmazott módosítása!")

        inp = input(f"Kérem módosítsa a fizetést ({szotar_lista[i]['FIZU']}): ")
        if inp == "#":
            break
        if inp != "":
            fizu = int(inp)
        else:
            fizu = szotar_lista[i]["FIZU"]

        if szotar_lista[i]["STAT"] == "AKTÍV":
            inp = input(f"Kérem módosítsa az alkalmazott kezdőévét({szotar_lista[i]['STARTEV']}): ")
            if inp == "#":
                break
            if inp != "":
                startev = int(inp)
            else:
                startev = szotar_lista[i]["STARTEV"]
        else:
            inp = input(f"Kérem módosítsa, hogy mely évtől lett inaktív ({szotar_lista[i]['INAKTEV']}): ")
            if inp == "#":
                break
            if inp != "":
                inaktev = int(inp)
            else:
                inaktev = szotar_lista[i]["INAKTEV"]

        szotar_lista[i]["FIZU"] = fizu
        szotar_lista[i]["STARTEV"] = startev
        szotar_lista[i]["INAKTEV"] = inaktev
        print(f"A(z) {szotar_lista[i]['NEV']} alkalmazott adatai módosítva lettek.")
        print("---------------------------------")
        
def torles (szotar_lista):
    inp = ""
    i = 0
    nev = ""

    while inp != "#":
        print("Kilépéshez adja meg a # karaktert.")

        # A szamokba betesszuk a jelenlegi 
        # rekordok szamsorait listában
        # [1,2,3,4,5,...,1000,...]
        szamok = list(range(1, len(szotar_lista)+1))
        inp = kereses.lista10(szotar_lista, True, i)
        # ha benne van a szam amit megadott, 
        # akkor az lesz a kivalasztott rekord,
        # egyébként kilépünk (vagy #-et adott, vagy 
        # olyan számot amivel nem létezik rekord)
        # azért kell a -1, mert 1-től listáztunk
        if inp in str(szamok):
            i = int(inp)-1
        else:
            break

        nev = szotar_lista[i]["NEV"]
        inp = input(f"Biztos törli a(z) {szotar_lista[i]['NEV']} alkalmazottat? (IGEN/NEM): ")
        if inp == "IGEN":
            del szotar_lista[i]
            print(f"A(z) {nev} alkalmazott adatai törölve.")
            print("---------------------------------")

def aktinakt (szotar_lista):
    inp = ""
    i = 0

    while inp != "#":
        print("Kilépéshez adja meg a # karaktert.")
        # A szamokba betesszuk a jelenlegi 
        # rekordok szamsorait listában
        # [1,2,3,4,5,...,1000,...]
        szamok = list(range(1, len(szotar_lista)+1))
        inp = kereses.lista10(szotar_lista, True, i)
        # ha benne van a szam amit megadott, 
        # akkor az lesz a kivalasztott rekord,
        # egyébként kilépünk (vagy #-et adott, vagy 
        # olyan számot amivel nem létezik rekord)
        # azért kell a -1, mert 1-től listáztunk
        if inp in str(szamok):
            i = int(inp)-1
        else:
            break

        if szotar_lista[i]["STAT"] == "AKTÍV":
            inp = input(f"Biztos inaktiválja a(z) {szotar_lista[i]['NEV']} alkalmazottat? (IGEN/NEM): ")
            if inp == "IGEN":
                inp = input(f"Milyen évtől legyen inaktív (Kezdés éve: {szotar_lista[i]['STARTEV']}):")
                if inp == "#":
                    break
                if int(inp) < szotar_lista[i]["STARTEV"]:
                    print("Nem lehet korábbi évtől inaktív.")
                else:
                    szotar_lista[i]["STAT"] = "INAKTÍV"
                    szotar_lista[i]["INAKTEV"] = int(inp)
                    print(f"A(z) {szotar_lista[i]['NEV']} alkalmazott inaktív státuszba lett téve.")
                    print("---------------------------------")
        else:
            inp = input(f"Biztos aktiválja a(z) {szotar_lista[i]['NEV']} alkalmazottat? (IGEN/NEM): ")
            if inp == "IGEN":
                    szotar_lista[i]["STAT"] = "AKTÍV"
                    szotar_lista[i]["INAKTEV"] = 0
                    print(f"A(z) {szotar_lista[i]['NEV']} alkalmazottat aktív státuszba helyeztük.")
                    print("---------------------------------")
