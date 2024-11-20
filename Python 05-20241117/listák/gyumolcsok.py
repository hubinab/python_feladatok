#1. feladat
N=int(input("Add meg az elemszámot: "))


#2. feladat
gyümölcsök = []

for i in range(N):
    gyümölcsök.append(input(f"{i+1}. gyümölcs neve: "))


#3. feladat
print(*gyümölcsök[::-1])

# for i in range(len(gyümölcsök),0,-1):
#     print(gyümölcsök[i], end=" ")
# print()

# for gyümölcs in gyümölcsök[::-1]:
#     print(gyümölcs, end=" ")
# print()


#4. feladat
for i in range(len(gyümölcsök)):
    print(f"{i+1}. gyümölcs neve: {gyümölcsök[i]}, hossza: {len(gyümölcsök[i])} karakter")


#5. feladat
for i in range(len(gyümölcsök)):
    if len(gyümölcsök[i]) % 2 == 0:
        print(gyümölcsök[i])


#6. feladat
for i in range(len(gyümölcsök)):
    # if len(gyümölcsök[i]) % 2 == 1:
    # if not len(gyümölcsök[i]) % 2 == 0:
    if len(gyümölcsök[i]) % 2 != 0:
        print(gyümölcsök[i], end=";")
        
