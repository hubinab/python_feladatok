import random

# Kérj be egy felhasználótól a teljes nevet (feltételezheted, hogy a felhasználónak csak egy
# keresztneve van), kedvenc állatának nevét és születési évet! 
nev = input("Kérem a teljes nevét (csak egy keresztnevet kérek): ")
allat = input("Kérem a kedvenc állatának nevét: ")
szuletes_ev = input("Kérem az állat születési évét (ÉÉÉÉ formában): ")

# Generálj a felhasználónak egy jelszót a következő 
# szabályok alapján és írd ki a jelszót a képernyőre!
# Szabályok:
# - vezetéknévből vágd ki az utolsó 3 karaktert.
# - keresztnévből minden páratlan karaktert fűzd össze jobbról (azaz visszafele)
# - generálj egy véletlenszámot 50 és 99 között
# - kedvenc állatnévből töröld ki a középső két karaktert 
# és alakítsd nagybetűssé a maradék betűket
# - évszámból vágd ki az első két karaktert

nevek = nev.split(" ")
vezeteknev = nevek[0]
keresztnev = nevek[1]

# vezetéknévből vágd ki az utolsó 3 karaktert.
print(vezeteknev[-3:],end="")

# keresztnévből minden páratlan karaktert fűzd össze jobbról (azaz visszafele)
if len(keresztnev) % 2 == 0:
    print(keresztnev[0:len(keresztnev)-1][::-2],end="")
else:
    print(keresztnev[::-2],end="")

# generálj egy véletlenszámot 50 és 99 között
print(random.randint(50,99),end="")

# kedvenc állatnévből töröld ki a középső két karaktert
# és alakítsd nagybetűssé a maradék betűket
print(allat[0:len(allat)//2 - 1].upper() + allat[len(allat)//2 + 1:len(allat)].upper(),end="")

# - évszámból vágd ki az első két karaktert
print(szuletes_ev[0:2])
