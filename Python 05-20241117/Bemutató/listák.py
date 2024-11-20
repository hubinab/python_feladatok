névsor = []
névsor = ["Kis Béla", "Nagy Endre", "Közepes Irén"]


# emberAdatok = ["Nagy Endre",84,False]

print(len(névsor))

for i in range(len(névsor)):
    print(névsor[i])

for név in névsor:
    print(név)


print(névsor[::-1])
print(névsor)


szöveg = "alma"

print(szöveg[2])

névsor[0] = "Kiss Béla"
print(névsor)

# szöveg[0] = "A" # HIBA!!
print(szöveg[::-1])

névsor.append("Végső Elek")
print(névsor)

print(névsor.pop(0))

print(névsor)