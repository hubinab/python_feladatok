import random

# Kérd be a felhasználótól a lista elemszámát!
szam = int(input("Adj meg egy számot: "))

# Töltsd fel a listát 1 és 100 közötti véletlen számmal!
lista = []
for i in range(szam):
    lista.append(random.randint(1, 100))

# Írd ki a lista elemeit a következő formában!
# 1. elem: 23
# 2. elem: 12
for i in range(szam):
    print(f"{i+1}. elem: {lista[i]}")

# Írd ki a lista elemeit pontosvesszővel elválasztva egymás mellé.
print(*lista, sep=";")

