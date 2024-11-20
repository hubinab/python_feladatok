# Teszt progi

Kor = 0
while Kor != 999:
    Kor = int(input("Hányéves vagy? "))
    if Kor == 999:
        print("Szia!")
        break
    if Kor >= 21:
        print("USA-ban is szavazhatsz")
    elif Kor >= 18:
        print("Szavaszhatsz")
    else:
        print("Nem szavazhatsz")
        