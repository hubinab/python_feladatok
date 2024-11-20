# Olvass be egy mondatot!
mondat = input("Írj be egy mondatot: ")
szo = input("Kérek egy szót: ")

# Hány karakterből áll a mondat?
print("A mondat ", len(mondat)+1, " karakterből áll.")

# Vizsgáld meg, hogy van-e a mondat végén pont, vagy kérdőjel, vagy felkiáltójel!
if mondat[-1] in ['.', '?', '!']:
    print("A mondat végén van pont, kérdőjel vagy felkiáltó jel!")

# Írd ki a mondat minden második karakterét összefűzve!
print("A mondat minden második karaktere: ", mondat[::2])

# Írd ki a mondatot visszafele!
print("A mondat visszafelé: ", mondat[::-1])

# Kérj be egy szót és vizsgáld, hogy szerepel-e a mondatban? Ha igen, akkor írd ki,
# hogy hányszor szerepel!
if szo in mondat:
    print(f"A szó {mondat.count(szo)} alkalommal szerepel.")
