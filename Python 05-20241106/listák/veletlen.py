import random


#1. feladat
elemSzám=int(input("Add meg az elemszámot: "))


#2. feladat
lista=[]
for i in range(elemSzám):
    lista.append(random.randint(1,100))


#3. feladat
for i in range(len(lista)):
    print(f"{i+1}. elem: {lista[i]}")


#4. feladat
# for i in range(len(lista)):
#     print(lista[i], end=";")
# print()

print(*lista, sep=";")