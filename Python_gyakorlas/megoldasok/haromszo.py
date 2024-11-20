# Kérj be a felhasználótól három szöveget/szót!
szo1 = input("Kérem az első szöveget/szót: ")
szo2 = input("Kérem a második szöveget/szót: ")
szo3 = input("Kérem a harmadik szöveget/szót: ")

# Vizsgáld meg, hogy az első szövegben benne van-e a második szó! 
# Ha igen, akkor cseréld le a második szót a harmadik szóra az első szövegben! 
# Akkor is tájékoztasd a felhasználót, ha nincs benne!

if szo2 in szo1:
    print("A második szó benne van az első szövegben")
    print("Ezért lecserélem az első szövegben a második szöveget a harmadik szövegre!")
    print(szo1.replace(szo2, szo3))
else:
    print("A második szó nincs benne az első szövegben")


# Ugyanezt vizsgáld meg, csak úgy hogy az első szövegben benne van-e a harmadik szó
# és ha igen, cseréld le a második szóra!
if szo3 in szo1:
    print("A harmadik szó benne van az első szövegben")
    print("Ezért lecserélem az első szövegben a második szöveget a harmadik szövegre")
    print(szo1.replace(szo3, szo2))
else:
    print("A harmadik szó nincs benne az első szövegben")

