lista=[] #[0,1,2,3,4,5,6,7,8,9]

#1. feladat
for i in range(10):
    lista.append(i)


#2. feladat
# print(*lista, sep=", ")

for i in range(len(lista)):
    if i < len(lista)-1:
        print(lista[i], end=", ")
    else:
        print(lista[i])

    # if i == len(lista)-1:
    #     print(lista[i])
    # else:
    #     print(lista[i], end=", ")



#3. feladat
for szam in lista:
    print(szam)

# print(*szam, sep="\n")

#4. feladat
for szam in lista[::-1]:
    print(szam)

# print(*szam[::-1], sep="\n")


#5. feladat
# for i in range(len(lista)):
#     if i % 2 == 0:
#         print(lista[i], end="")
# print()

# for i in range(0,len(lista),2):
#     print(lista[i], end="")
# print()

print(*lista[::2], sep="")