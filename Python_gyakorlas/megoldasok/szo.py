szo = input("Írj be egy szót: ")
# ird ki a szo hosszat
print(len(szo))

# ird ki nagybetűsen
print(szo.upper())

# ird ki kisbetűsen
print(szo.lower())

# írd ki úgy, hogy ami kisbetű volt az most nagybetűsen jelenjen meg, ami pedig nagybetűsen volt az kisbetűsen jelenjen meg!
print(szo.swapcase())

# szó fordított alakját mentsd el egy segéd változóba és írd ki a változó értékét! 
szo_ford = szo[::-1]
print(szo_ford)

# vizsgáld meg hogy palindrom szó-e
if szo == szo_ford:
    print("A szó palindrom!")
else:
    print("A szó nem palindrom!")
