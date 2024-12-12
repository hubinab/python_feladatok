#fájl tartalmát szótár típusú listában tároljuk (a listába szótár típusú elemek lesznek)
#a fájl első sorában most fejléc van

verseny_lista=[]

with open("edesseg.csv","r", encoding="utf-8") as f:
    sorok=f.read().splitlines()
    for sor in sorok[1::]: #a 0. indexen lévő sort kihagyjuk
        adat=sor.strip().split(";")
        
        szotar={}
        szotar["nev"]=adat[0]
        szotar["db"]=int(adat[1])
        szotar["tipus"]=adat[2]
        verseny_lista.append(szotar)

print(verseny_lista)