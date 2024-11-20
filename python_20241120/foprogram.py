# w3scools-ba a python.modules-nál

# Így meg kell addni a fuggveny. -ot (ha lehet így használjuk!):
# import fuggvenyek
# Így nem kell fuggveny.teglalap stb...
# a * azt jelenti, hogy minden fuggvényt és eljárást beimportál
from fuggvenyek import *
# De fel is lehet sorolni (ez csak a Paros függvényt fogja beimportálni):
#from fuggvenyek import Paros
# De külön megadhatom a teglalapot is, így már olyan, mintha *-ot írtam volna
#from fuggvenyek import teglalap

# A beépített függvényeknél is működik
#from random import *
# Így csak ezt a kettőt tudom majd haszálni:
#from random import randint, choice

# Át lehet nevezni 
import fuggvenyek as seged

seged.teglalap(2,3)
seged.Paros(7)

print(Paros(5))
teglalap(5,4)
teglalap(5,4,"F")
teglalap(6,7,katrakter='X')
# felcserelhetok a parameterek, de akkor meg kell adni a parameter nevet
teglalap(szelesseg=int(input("Szelesseg: ")),magassag=2,katrakter='J')
# ez is működik, de zavaro:
magassag = 6
teglalap(szelesseg=2, magassag=magassag, katrakter="D")

