# w3scools python dictionary

# Van egy kulcsunk és annak van egy értéke

# üres lista (lista inicializálás)
lista = []
lista = list()

# üres szótár (szótár inicializálás)
szotar = {}
szotar = dict()

szotar = {
    "név": "Gábor",
    "kor": 25,
    "hely": "Budapest",
    "owners":["Bob","Géza","Béla"]
}

# A kulccsal hivatkozunk az értékre
print (szotar["név"])
print (szotar["kor"])
print (szotar["hely"])
print (szotar["owners"][0])
print (szotar["owners"][2])

ember = {}

# itt még hibát dob:
#print(ember["kor"])

ember["név"] = "Gábor Béla"
ember["kor"] = 19
ember["házas"] = "nem"

print(ember)
print(ember["név"])
