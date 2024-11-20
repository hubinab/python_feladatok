str_osszeg = ""
str_kulonbseg = ""
str_mindketto = ""
for i in range (1,10):
    for j in range (0,10):
        osszeg_true=False
        a=int(f"{i}{j}")
        b=i+j
        c=i-j
        if a%b == 0:
            str_osszeg=str_osszeg+ " " + str(a)
            osszeg_true=True
        if c != 0 and a%c == 0:
            str_kulonbseg=str_kulonbseg+ " " + str(a)
            if osszeg_true:
                str_mindketto=str_mindketto + " " + str(a)



print("A szám osztható számjegyei összegév:", str_osszeg)
print("A szám osztható számjegyei különbségével:", str_kulonbseg)
print("A szám osztható számjegyei összegével is, különbségével is:", str_mindketto)