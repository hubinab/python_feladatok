szöveg1 = input("Kérem adjon meg az első szövegeet: ")
szó2 = input("Kerem adja meg az harmadik szót: ")
szó3 = input("Kerem adja meg a második szót: ")

if szó2 in szöveg1:
    print("A második szó megtalálható az első szövegben.")
    print(szöveg1.replace(szó2, szó3))
else:
    print("A második szó nem megtalálható az első szövegben.")

if szó3 in szöveg1:
    print("A harmadik szó megtalálható az első szövegben.")
    print(szöveg1.replace(szó3, szó2))
else:
    print("A harmadik szó nem megtalálható az első szövegben.")