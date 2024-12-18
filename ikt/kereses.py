# Elsődleges kulcs szerinti keresés
def pri_keres (nev, szev, szotar_lista):
    search_nev = nev
    search_szev = szev
    for i in range(len(szotar_lista)):
        if szotar_lista[i]["NEV"].casefold() == search_nev.casefold() and szotar_lista[i]["SZEV"] == search_szev:
            return i
    return None

def fej_iras ():
    # Fejléc
    print(f"{'#':<3} {'Név':<40} {'Sz.év':>5} {'Fizetés':>15} {'Státusz':<7} {'St.év':>5} {'In.év':>5}")
    print("-"*86)

def egy_sor_iras (sor, sorszam=None):
    # Egy sor kiírása
    fizu = f"{sor['FIZU']:,}"
    print(f"{sorszam:<3} {sor['NEV']:<40} {sor['SZEV']:>5} {fizu:>15} {sor['STAT']:<7} {sor['STARTEV']:>5} {sor['INAKTEV']:>5}")

# Összes rekord listázása 
# (név szerint rendezve - ezt kivetem mert nem tanultuk)
def lista (szotar_lista, tol=None, ig=None):
    if tol == None:
        tol = 0
    if ig == None:
        ig = len(szotar_lista)

    # Rendezés
    #sort_list = sorted(szotar_lista, key=lambda x: x["NEV"])
    sort_list = szotar_lista

    # fejléc
    fej_iras()

    # Elemek kiírása
    for i in range(tol, ig):
        egy_sor_iras(sort_list[i], i+1)

# Összes rekord listázása 10-esével
def lista10 (szotar_lista, karb=False, tol=None):
    inp = ""
    if tol == None:
        tol = 0
    else:
        i = tol
    
    while inp != "#":
        j = i+10
        if j >= len(szotar_lista):
            j = len(szotar_lista)

        lista(szotar_lista, i, j)
        i = j
        if i >= len(szotar_lista):
            i = 0
        
        if karb:
            print("Tovább=Enter, Kilépés=#")
            inp = input("Vagy adja meg a rekord sorszámát: --> ")
            if inp != "":
                return inp
        else:
            inp = input("Tovább=Enter, Kilépés=# --> ")
                
