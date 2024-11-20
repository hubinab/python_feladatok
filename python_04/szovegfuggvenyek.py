szoveg = "aLma"
szoveg2 = "alma körte banán"
szoveg3 = "kutya,macska,egér"
szoveg4 = "   sajt  "
szoveg5 = "Géza"
szoveg6 = "kuTYa"
szoveg7 = "almA"

print(szoveg6.lower()) # csupa kisbetűssé alakítja
print(szoveg6.casefold()) # okosabb, mint a lower
print(szoveg6.upper()) # Nagybetűssé teszi
print(szoveg6.capitalize()) # Az első betű nagy lesz

print(szoveg.endswith("a")) # akkor ad igazat, ha arra végződik
print(szoveg.startswith("a")) # ugyan az, csak az elejére
print(szoveg2.split(" ")) # listába teszi a space mentén, de a space helyett lehet más is
print(szoveg3.split(",")) # listába teszi a space mentén, de a space helyett lehet más is

print(szoveg4.split()) # lecsapja  white space-eket
print(szoveg5.swapcase()) # ami nagybetűs, az kisbetűs lesz és fordítva

print(szoveg.casefold() == szoveg7.casefold()) # így össze lehet hasonlítani
