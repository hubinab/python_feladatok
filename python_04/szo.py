szo = input("Adj meg egy szót: ")

print(len(szo))
print(szo.upper())
print(szo.casefold())
print(szo.swapcase())

tmp = szo[::-1]
print(tmp)

if tmp == szo:
    print("Ez egy palindrom szó!")
else:
    print("Ez nem palindrom szó!")


