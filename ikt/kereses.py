
def pri_keres (nev, szev, list):
    search_nev = nev
    search_szev = szev
    for i in range(len(list)):
        if list[i]["NEV"].casefold() == search_nev.casefold() and list[i]["SZEV"] == search_szev:
            return i
    return None

def lista (list):
    print(f"{"#":<3} {"Név":<40} {"Sz.év":>5} {"Fizetés":>10} {"Státusz":<7} {"St.év":>5} {"In.év":5}")
    print("-"*81)
    for i in range(len(list)):
        print(f"{i+1:<3} {list[i]["NEV"]:<40} {list[i]["SZEV"]:>5} {list[i]['FIZU']:>10} {list[i]["STAT"]:<7} {list[i]["STARTEV"]:>5} {list[i]["INAKTEV"]:>5}")