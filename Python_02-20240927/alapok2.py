print("Gondoltam egy szóra.")
gondolttSzó = "szél"

bekeértSzó = input()
'''
if gondolttSzó == bekeértSzó:
    print("Eltaláltad!")
else:
    print("Nem találtad el!")



while gondolttSzó != bekeértSzó:
    bekeértSzó = input()
    if gondolttSzó == bekeértSzó:
        print("Eltaláltad!")
    else:
        print("Nem találtad el!")
'''


while gondolttSzó != bekeértSzó:
    print("Nem találtad el!")
    bekeértSzó = input()


print("Eltaláltad!")