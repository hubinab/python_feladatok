import random

szo1 = input("Kérem az első szót: ")
szo2 = input("Kérem a második szót: ")

# Vizsgáld meg, hogy valamelyik szó tartalmazza-e a másikat!
if szo1 in szo2 or szo2 in szo1:
    print("A két szó tartalmazza egymást!")

# Vizsgáld meg, hogy az első szó
#  eleje a másik szóval kezdődik-e?
if szo1.startswith(szo2):
    print("Az első szó a másodikkal kezdődik!")

# vége a másik szóval kezdődik-e?
if szo1.endswith(szo2):
    print("Az első szó a másodikkal végződik!")

# Vizsgáld meg, hogy ha tartalmazza az első szó a másodikat, hányadik karaktertől
# kezdve található meg az első szóban! (itt a +1 azért kell, 
# mert a "normális" emberek nem nullától kezdenek számolni)
if szo1.find(szo2) != -1:
    print(f"A második szó az első szóban a {szo1.find(szo2) + 1} karaktertől kezdődik") 

# Írd ki az első szó minden második karakterét!
for i in range(1, len(szo1), 2):
    print(szo1[i], end="")

# Írd ki véletlenszerűen az első szó egy betűjét!
print(f"\nA \"{szo1[random.randint(0, len(szo1)-1)]}\" betűt választottam!")


