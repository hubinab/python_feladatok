# Elsődleges kulcs szerinti keresés
def pri_keres (nev, szev, list):
    search_nev = nev
    search_szev = szev
    for i in range(len(list)):
        if list[i]["NEV"].casefold() == search_nev.casefold() and list[i]["SZEV"] == search_szev:
            return i
    return None

# Összes rekord listázása név szerint rendezve
def lista (list, tol=None, ig=None):

    if tol == None:
        tol = 0
    if ig == None:
        ig = len(list)

    # Rendezés
    sort_list = sorted(list, key=lambda x: x["NEV"])

    # Fejléc
    print(f"{"#":<3} {"Név":<40} {"Sz.év":>5} {"Fizetés":>15} {"Státusz":<7} {"St.év":>5} {"In.év":5}")
    print("-"*86)

    # Elemek kiírása
    for i in range(tol, ig):
        fizu = f"{sort_list[i]['FIZU']:,}"
        print(f"{i+1:<3} {sort_list[i]["NEV"]:<40} {sort_list[i]["SZEV"]:>5} {fizu:>15} {sort_list[i]["STAT"]:<7} {sort_list[i]["STARTEV"]:>5} {sort_list[i]["INAKTEV"]:>5}")

# Összes rekord listázása 10-esével
def lista10 (list):
    inp = ""
    i = 0
    while inp != "#":
        j = i+9
        if j >= len(list):
            j = len(list)

        lista(list, i, j)
        i = j
        if i >= len(list):
            break
        
        inp = input("Tovább=Enter, Kilépés=# -->")

        
