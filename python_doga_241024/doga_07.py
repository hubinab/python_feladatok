szelesseg = input("Kérem a téglalap szélességét (csak egész számot adhatsz meg): ")
magassag = input("Kérem a téglalap magasságát (csak egész számot adhatsz meg): ")

szelesseg = int(szelesseg)
magassag = int(magassag)

for i in range(magassag):
    print(szelesseg * "*")