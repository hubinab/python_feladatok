print('"Gondoltam" egy számra 1 és 100 között!')
gondolttSzám = 66

bekeértSzám = int(input("\t"))

if gondolttSzám == bekeértSzám:
    print("Eltaláltad!")
else:
    if gondolttSzám < bekeértSzám:
        print("Túl nagy!")
    else:
        print("Túl kicsi!")



while gondolttSzám != bekeértSzám:
    bekeértSzám = int(input())
    if gondolttSzám == bekeértSzám:
        print("Eltaláltad!")
    elif gondolttSzám < bekeértSzám:
        print("Túl nagy!")
    else:
        print("Túl kicsi!")
