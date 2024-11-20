import random


név = input("Kérem adja meg a teljes nevét: ")
kedvencÁllat = input("Kérem adja meg a kedvenc állatának nevét: ")
születésiÉv = input("Kérem adja meg a születési évét: ")
# születésiÉvint = int(születésiÉv)

vezetékNév = név.split(' ')[0]
keresztNév = név.split(' ')[1]

közép = (len(kedvencÁllat)-1)//2

jelszó1 = vezetékNév[-3:]
jelszó2 = keresztNév[::-2]
jelszó3 = str(random.randint(50, 99))
jelszó4 = (kedvencÁllat[:közép] + kedvencÁllat[közép + 2:]).upper()
jelszó5 = születésiÉv[:2]
# jelszó5 = str(születésiÉvint // 100)

print(jelszó1 + jelszó2 + jelszó3 + jelszó4 + jelszó5)
