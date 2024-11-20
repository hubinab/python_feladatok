import random

szó1 = input("Kerem adja meg az első szót: ")
szó2 = input("Kerem adja meg a második szót: ")

#a
if szó1.casefold() in szó2.casefold() or szó2.casefold() in szó1.casefold():
    print("Az egyik szó tartalmazza a másikat.")
else:
    print("Egyik szó sem tartalmazza a másikat.")

#b
if szó1.casefold().startswith(szó2.casefold()):
    print("Az első szó a másodikkal kezdődik.")
if szó1.casefold().endswith(szó2.casefold()):
    print("Az első szó a másodikkal végződik.")

#c
if szó2.casefold() in szó1.casefold():
    print(f"Az első szó a(z) {szó1.casefold().find(szó2.casefold())+1}. karaktertől tartalmazza a második szót.")
else:
    print("Az első szó nem tartalmazza a másodikat.")

#d
# for i in range(len(szó1)):
#     if i % 2 == 0:
#         print(szó1[i])

# for i in range(0,len(szó1),2):
#     print(szó1[i])

print(szó1[::2])

#e
# print(szó1[random.randint(0,len(szó1)-1)])

print(random.choice(szó1))