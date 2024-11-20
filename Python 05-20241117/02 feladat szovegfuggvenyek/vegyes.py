mondat = input("Kérem adjon meg egy mondatot: ")

print(f"A mondat {len(mondat)} karakterből áll.")


# if mondat.endswith('.'):
#     print("A mondat pontal végződik.")
# elif mondat.endswith('?'):
#     print("A mondat kérdőjellel végződik.")
# elif mondat.endswith('!'):
#     print("A mondat felkiáltójellel végződik.")

# if mondat.endswith('.'):
#     print("A mondat pontal végződik.")
# else:
#     if mondat.endswith('?'):
#         print("A mondat kérdőjellel végződik.")
#     else:
#         if mondat.endswith('!'):
#             print("A mondat felkiáltójellel végződik.")

if mondat.endswith('.') or mondat.endswith('?') or mondat.endswith('!'):
    print("A mondat tartalmaz mondat végi írásjelet.")


# mindenMásodikKarakter = ""
# for i in range(len(mondat)):
#     if i % 2 == 0:
#         # mindenMásodikKarakter = mindenMásodikKarakter + mondat[i]
#         mindenMásodikKarakter += mondat[i]

# mindenMásodikKarakter = ""
# for i in range(0,len(mondat),2):
#     # mindenMásodikKarakter = mindenMásodikKarakter + mondat[i]
#     mindenMásodikKarakter += mondat[i]

# for i in range(len(mondat)):
#     if i % 2 == 0:
#         print(mondat[i], end="")
# print()

# for i in range(0,len(mondat),2):
#     print(mondat[i], end="")
# print()

print(mondat[::2])


# mondatFordítva = ""
# for i in range(len(mondat)):
#     mondatFordítva = mondat[i] + mondatFordítva
# print(mondatFordítva)

# mondatFordítva = ""
# for i in range(len(mondat)):
#     mondatFordítva += mondat[len(mondat)-1-i]
# print(mondatFordítva)

# mondatFordítva = ""
# for betű in mondat:
#     mondatFordítva = betű + mondatFordítva
# print(mondatFordítva)

# mondatFordítva = ""
# for i in range(len(mondat),0,-1):
#     mondatFordítva += mondat[i]
# print(mondatFordítva)

# for i in range(len(mondat),0,-1):
#     print(mondat[i])
# print()

print(mondat[::-1])


szó = input("Kerem adja meg a keresett szót: ")

if szó in mondat:
    print(f"A keresett szó {mondat.count(szó)} alkalommal szerepel a mondatban.")
else:
    print("A keresett szó nem szerepel a mondatban.")