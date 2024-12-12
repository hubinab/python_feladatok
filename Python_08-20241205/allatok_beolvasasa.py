import random

allatok = []
"""
r = olvasas
w = írás
a = hozzáírás

filebe = open("allatok.txt", "r", encoding="utf-8")

# olvassuk be soronként a file-t
for i in range(21):
    #print(filebe.readline().strip(), end=";")
    # strip leveszi a white space-eket
    allatok.append(filebe.readline().strip())

# readlines ezzel az egészet be lehet olvasni ciklus nélkül
allatok = filebe.readlines()

# Fájl zárása ez fontos!!
filebe.close()

# Lista kiírása ; szeparálással
print(*allatok, sep=';')

# itt a végére is tesz pontosvesszőt!
#print(*allatok, end=';')
"""
# A with-en belül lehet a filebe változot hasznalni, 
# with után bezárja a filet
with open(".//Python_08-20241205/allatok.txt", "r", encoding="utf-8") as filebe:
    sor = filebe.readline().strip()
    #for i in range(21):
    while sor != "":
        # strip leveszi a white space-eket
        allatok.append(sor)
        sor = filebe.readline().strip()

# Lista kiírása ; szeparálással
print(*allatok, sep=';')

# File kiirasa
# k-val kezdodo allatok kiírása

"""
fileki = open("k_allatok.txt", "w", encoding="utf-8")

for i in range(len(allatok)):
    if allatok[i].startswith("k"):
        fileki.write(allatok[i] + "\n")

fileki.close()
with open("k_allatok.txt", "w", encoding="utf-8") as fileki:
    for i in range(len(allatok)):
        if allatok[i].startswith("k"):
            fileki.write(allatok[i] + "\n")
"""

# Lehet print-el is file-ba irni. 
# A "file="-vel átlehet irányítani a standard output-ot file-ba
with open(".//Python_08-20241205/k_allatok.txt", "w", encoding="utf-8") as fileki:
    for i in range(len(allatok)):
        if allatok[i].startswith("k"):
            print(allatok[i], file=fileki)

def terulet (a,b):
    return int(round(a*b/3.6, 0))

telkek = input("Adja meg a telkek számát: ")
for i in range(int(telkek)):
    a = random.randint(20,100)
    b = random.randint(20,100)
    print(a, b)
    print(terulet(a, b))
