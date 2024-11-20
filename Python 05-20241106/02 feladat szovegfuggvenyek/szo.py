szó = input("Kerem adjon meg egy szót: ")

# a
print(f"A szó hossza: {len(szó)}")

# b
print(f"A szó nagybetüsen: {szó.upper()}")

# c
print(f"A szó kisbetüsen: {szó.lower()}")

# d
print(f"A szó kis- és nagybetüsen: {szó.swapcase()}")

# e
# szóFordítva = ""

# for i in range(len(szó)):
#     szóFordítva = szó[i] + szóFordítva

# for i in range(len(szó)):
#     szóFordítva += szó[len(szó)-1-i]

# for betű in szó:
#     szóFordítva = betű + szóFordítva

# for i in range(len(szó),0,-1):
#     szóFordítva += szó[i]

szóFordítva = szó[::-1]

# f
if szó == szóFordítva:
    print("A szó palindróm szó.")
else:
    print("A szó nem palindróm szó.")
