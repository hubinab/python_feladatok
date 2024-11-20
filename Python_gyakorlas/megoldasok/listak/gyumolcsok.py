# Kérj be a felhasználótól egy elemszámot (N)!
elemszam = input("Kérek egy elemszámot(N): ")

# Kérj be a felhasználótól N darab gyümölcsöt és tárold el egy listába!
gyumolcs = []
for i in range(int(elemszam)):
    gyumolcs.append(input(f"Kérem a(z) {i+1}. gyümölcsöt: "))

# Jelenítsd meg a lista tartalmát fordított sorrendben egy sorba!
print(*gyumolcs[::-1])

# Jelenítsd meg a lista tartalmát a következő formában:
#  1. gyümölcs neve: alma, hossza: 4 karakter
#  2. gyumolcs neve: dinnye, hossza: 6 karakter

for i in range(len(gyumolcs)):
    print(f"{i+1}. gyümölcs neve: {gyumolcs[i]}, hossza: {len(gyumolcs[i])} karakter")

# Írd ki a páros karakterszámú gyümölcsök neveit egymás alá!

for i in range(len(gyumolcs)):
    if len(gyumolcs[i]) % 2 == 0:
        print(gyumolcs[i])

# Írd ki a páratlan karakterszámú gyümölcsök neveit egymás mellé pontosvesszővel
# elválasztva!
for i in range(len(gyumolcs)):
    if len(gyumolcs[i]) % 2 != 0:
        print(gyumolcs[i], end=";")
print()