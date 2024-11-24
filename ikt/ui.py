t_alkalmazottak = []

def p_prompt ():
    menu = input("--> ")
    return menu

def p_focim ():
    print("Alkalmazott karbantartó rendszer")

def p_choise ():
    print("Kérem válasszon az alábbi menüpontok közül!")

def p_kilep ():
    print("Kilépés...")

def p_vissza ():
    print("Vissza a főmenübe...")

def p_hiba ():
    print("Hiba! Kérem adjon meg egy érvényes menüpontot!")

def p_karbantartas ():
    print("1. Felvitel")
    print("2. Módosítás")
    print("3. Törlés")
    print("4. Aktiválás/inaktiválás")
    print("5. Vissza")

def p_riportok ():
    print("1. Legidősebb alkalmazott")
    print("2. Legfiatalabb alkalmazott")
    print("3. Hány aktív alkalmazott van")
    print("4. Hány inaktív alkalmazott van")
    print("5. Havi összes kifizetés")
    print("6. Havi átlag fizetés")
    print("7. Vissza")

def p_kereses ():
    print("1. Belépés éve szerinti lista")
    print("2. Kilépés éve szerinti lista")
    print("3. Fizetés szerinti lista -tól-ig")
    print("4. Vissza")

def p_fomenu ():
    print("1. Adatok karbantartása")
    print("2. Riportok")
    print("3. Keresés, listázás")
    print("4. Kilépés")
