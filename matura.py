# with open ("/Users/e-krawczyk/Desktop/Python/Python/liczby.txt", "r") as file:
#     content = file.readlines()

# licznik=(0)

# for i in content:
#     if i.count("0")>i.count("1"):
#         licznik=licznik+1

# print(licznik)

with open ("/Users/e-krawczyk/Desktop/Python/Python/liczby.txt", "r") as file:
    content = file.readlines()

licznik2=(0)
licznik8=(0)

for i in content:
    if i[-2]=="0":
        licznik2=licznik2+1

    if i[-2]=="0" and i[-3]=="0" and i[-4]=="0":
        licznik8=licznik8+1

print(licznik2, licznik8)
