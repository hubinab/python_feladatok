szam1=1
szam2=0
szam_seged=0

szam1_ok=False
szam2_ok=False

# Szamok bekerese
while not szam1_ok or not szam2_ok:
    if not szam1_ok:
        szam1 = int(input("Kérem az egyik 10 és 20 közé eső számot: "))
        if szam1 >= 10 and szam1 <= 20:
            szam1_ok=True

    if not szam2_ok and szam1_ok:        
        szam2 = int(input("Kérem a másik 10 és 20 közé eső számot "))
        if szam2 >= 10 and szam2 <= 20:
            szam2_ok=True

# Szam csere, ha kell
if szam2 < szam1:
    szam_seged=szam2
    szam2=szam1
    szam1=szam_seged

# Kiirando szoveg osszeallitasa
for i in range(szam1,szam2+1):
    csillag=""
    for j in range(1,i):
        csillag=csillag + "*"
    print(i,":",csillag)
