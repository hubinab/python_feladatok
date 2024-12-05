import karbantartas

def m_karbantartas (szotar_lista):
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
            case "1": karbantartas.felvitel (szotar_lista)
            case "2": karbantartas.modositas (szotar_lista)
            case "3": karbantartas.torles (szotar_lista)
            case "4": karbantartas.aktinakt (szotar_lista)

def m_riportok (szotar_lista):
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

def m_kereses (szotar_lista):
    menube = ""
    while menube != "4":
        print("Alkalmazott karbantartó rendszer")
        print("Kérem válasszon az alábbi menüpontok közül!")
        print("1. Belépés éve szerinti lista")
        print("2. Kilépés éve szerinti lista")
        print("3. Fizetés szerinti lista -tól-ig")
        print("4. Vissza")
        menube = input("--> ")

def m_fomenu (szotar_lista):
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
            case "1": m_karbantartas (szotar_lista)
            case "2": m_riportok (szotar_lista)
            case "3": m_kereses (szotar_lista)
            case "4": print("Kilépés...")
            case _  : print("Hiba! Kérem adjon meg egy érvényes menüpontot!")
