str_i = ""
str_first = "    "

for i in range(1,11):
    str_first = str_first + f"{i:>4}"

print(str_first)

for i in range(1,11):
    str_j = ""
    for j in range(1,11):
        str_j = str_j + f"{j*i:>4}"
    str_i = f"{i:>3}"
    print(str_i, str_j)

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
        