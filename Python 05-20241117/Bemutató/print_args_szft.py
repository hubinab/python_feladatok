print("asdasasd", end="")
print("asdasasd", end=";")
print("asdasasd", end=";\n")
print("asdasasd", end=";\n\t")
print()


print("alma", "körte", "meggy", sep="")
print("alma", "körte", "meggy", sep=" ")
print("alma", "körte", "meggy", sep=";")
print("alma", "körte", "meggy", sep="\t")



print("alma", "körte", "meggy", sep="\t", end="")
print("alma", "körte", "meggy", sep="\t", end="")
print("alma", "körte", "meggy", sep="\t", end="")
print("alma", "körte", "meggy", sep="\t")


nevek = ["Béla", "Éva", "Zoé"]

for i in range(len(nevek)):
    print(nevek[i], end=';')
print()

print(*nevek, sep=';')
print(*nevek[::-1], sep=';')