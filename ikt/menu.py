import karbantartas

def m_karbantartas (list):
    menube = ""
    while menube != "5":
        print("Alkalmazott karbantartó rendszer")
        print("Kérem válasszon az alábbi menüpontok közül!")
        print("1. Felvitel")
        print("2. Módosítás")
        print("3. Törlés")
        print("4. Aktiválás/inaktiválás")
        print("5. Vissza")
        menube = input("--> ")
        match menube:
            case "1": karbantartas.felvitel (list=list)
            case "2": karbantartas.modositas (list=list)
            case "3": karbantartas.torles (list=list)
            case "4": karbantartas.aktinakt (list=list)

def m_riportok (list):
    menube = ""
    while menube != "7":
        print("Alkalmazott karbantartó rendszer")
        print("Kérem válasszon az alábbi menüpontok közül!")
        print("1. Legidősebb alkalmazott")
        print("2. Legfiatalabb alkalmazott")
        print("3. Hány aktív alkalmazott van")
        print("4. Hány inaktív alkalmazott van")
        print("5. Havi összes kifizetés")
        print("6. Havi átlag fizetés")
        print("7. Vissza")
        menube = input("--> ")

def m_kereses (list):
    menube = ""
    while menube != "4":
        print("Alkalmazott karbantartó rendszer")
        print("Kérem válasszon az alábbi menüpontok közül!")
        print("1. Belépés éve szerinti lista")
        print("2. Kilépés éve szerinti lista")
        print("3. Fizetés szerinti lista -tól-ig")
        print("4. Vissza")
        menube = input("--> ")

def m_fomenu (list):
    menube = ""
    while menube != "4":
        print("Alkalmazott karbantartó rendszer")
        print("Kérem válasszon az alábbi menüpontok közül!")
        print("1. Adatok karbantartása")
        print("2. Riportok")
        print("3. Keresés, listázás")
        print("4. Kilépés")
        menube = input("--> ")
        match menube:
            case "1": m_karbantartas (list=list)
            case "2": m_riportok (list=list)
            case "3": m_kereses (list=list)
            case "4": print("Kilépés...")
            case _  : print("Hiba! Kérem adjon meg egy érvényes menüpontot!")
