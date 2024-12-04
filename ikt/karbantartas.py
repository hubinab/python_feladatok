import kereses

def felvitel (list):
    inp = ""
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

        i = kereses.pri_keres(nev, szev, list)
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
        list.append ({"NEV":nev, "SZEV":szev, "FIZU":fizu, "STAT":stat, "STARTEV":startev, "INAKTEV":inaktev})
        print(f"A(z) {nev} alkalmazottat sikeresen felvettük.")
        print("---------------------------------")
        kereses.lista10(list=list, karb=False, tol=len(list)-1)

def modositas (lista):
    inp = ""
    nev = ""
    szev = ""
    fizu = ""
    startev = 0
    inaktev = 0
    i = 0

    while inp != "#":
        """
        print("Kilépéshez adja meg a # karaktert.")
        print("Kérem adja meg az alábbi adatokat. Ha nem ad meg semmit, akkor az adat nem változik.")
        
        inp = input("Alkalmazott neve: ")
        if inp == "#" or inp == "":
            break
        nev = inp
        inp = input("Alkalmazott születési éve: ")
        if inp == "#" or inp == "":
            break
        szev = int(inp)
        i = kereses.pri_keres(nev, szev, list)
        if i == None:
            print("Nincs ilyen alkalmazott.")
            continue
        """
        szamok = list(range(1, len(lista)+1))
        inp = kereses.lista10(list=lista, karb=True, tol=i)
        if inp in str(szamok):
            i = int(inp)-1
        else:
            break

        print("Kilépéshez adja meg a # karaktert.")
        print("Kérem adja meg az alábbi adatokat. Ha nem ad meg semmit, akkor az adat nem változik.")
        print(f"A(z) {lista[i]['NEV']}, {lista[i]['SZEV']} alkalmazott módosítása!")
        inp = input(f"Kérem módosítsa a fizetést ({lista[i]['FIZU']}): ")
        if inp == "#":
            break
        if inp != "":
            fizu = int(inp)
        else:
            fizu = lista[i]["FIZU"]

        if lista[i]["STAT"] == "AKTÍV":
            inp = input(f"Kérem módosítsa az alkalmazott kezdőévét({lista[i]['STARTEV']}): ")
            if inp == "#":
                break
            if inp != "":
                startev = int(inp)
            else:
                startev = lista[i]["STARTEV"]
        else:
            inp = input(f"Kérem módosítsa, hogy mely évtől lett inaktív ({lista[i]['INAKTEV']}): ")
            if inp == "#":
                break
            if inp != "":
                inaktev = int(inp)
            else:
                inaktev = lista[i]["INAKTEV"]

        lista[i]["FIZU"] = fizu
        lista[i]["STARTEV"] = startev
        lista[i]["INAKTEV"] = inaktev
        print(f"A(z) {nev} alkalmazott adatai módosítva lettek.")
        
def torles (list):
    inp = ""
    nev = ""
    szev = ""
    i = 0

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
        i = kereses.pri_keres(nev, szev, list)
        if i == None:
            print("Nincs ilyen alkalmazott.")
            continue
        inp = input(f"Biztos törli a(z) {list[i]['NEV']} alkalmazottat? (IGEN/NEM): ")
        if inp == "IGEN":
            del list[i]
            print(f"A(z) {nev} alkalmazott adatai törölve.")
            
def aktinakt (list):
    inp = ""
    nev = ""
    szev = ""
    inaktev = 0
    i = 0

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
        i = kereses.pri_keres(nev, szev, list)
        if i == None:
            print("Nincs ilyen alkalmazott.")
            continue
        if list[i]["STAT"] == "AKTÍV":
            inp = input(f"Biztos inaktiválja a(z) {list[i]['NEV']} alkalmazottat? (IGEN/NEM): ")
            if inp == "IGEN":
                inp = input(f"Milyen évtől legyen inaktív (Kezdés éve: {list[i]['STARTEV']}):")
                if inp == "#":
                    break
                if int(inp) < list[i]["STARTEV"]:
                    print("Nem lehet korábbi évtől inaktív.")
                else:
                    list[i]["STAT"] = "INAKTÍV"
                    print(f"A(z) {nev} alkalmazott inaktív státuszba lett téve.")
        else:
            inp = input(f"Biztos aktiválja a(z) {list[i]['NEV']} alkalmazottat? (IGEN/NEM): ")
            if inp == "IGEN":
                    list[i]["STAT"] = "AKTÍV"
                    list[i]["INAKTEV"] = 0
                    print(f"A(z) {nev} alkalmazottat aktív státuszba helyeztük.")
                    
                                
