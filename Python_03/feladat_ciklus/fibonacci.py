szam = int(input("Adj meg egy számot, 3 és 30 között: "))

b = 0
a = 1
i = 0
print(0)
while i < szam-1:
    print(b+a)
    b = b + a
    a = b - a
    i += 1
