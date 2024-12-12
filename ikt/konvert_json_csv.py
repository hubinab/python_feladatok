import json

fileki = open("alkalmazottak.csv", "w", encoding="utf-8")
filename = "alkalmazottak.json"
# JSON fájl beolvasása
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
    

t_alkalmazottak = load_json ("alkalmazottak.json")

for i in range(len(t_alkalmazottak)):
    fileki.write(t_alkalmazottak[i]["NEV"] + ";" + str(t_alkalmazottak[i]["SZEV"]) + ";" + str(t_alkalmazottak[i]["FIZU"]) + ";" + t_alkalmazottak[i]["STAT"] + ";" + str(t_alkalmazottak[i]["STARTEV"]) + ";" + str(t_alkalmazottak[i]["INAKTEV"]) + "\n")

fileki.close()

