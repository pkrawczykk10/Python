#Z DZIESIETNEGO NA BINARNY
x=int(input("Podaj liczbe:"))
reszty=[]

while x>0:
   if x%2==1:
    x=(x-1)/2 
    reszty.append(1)
   else:
    x=x/2
    reszty.append(0)

print(reszty[::-1])

#Z BINARNEGO NA DZIESIETNY
binarna = (input("Podaj liczbe w systemie binarnym: "))

poprawna = True
for cyfra in binarna:
    if cyfra != "0" and cyfra != "1":
        poprawna = False
        break

if poprawna:
    dziesietna = 0
    potega = 0
    
    for cyfra in binarna[::-1]:
        if cyfra == "1":
            dziesietna += 2 ** potega
        potega += 1

    print("Liczba dziesietna to:", dziesietna)
else:
    print("To nie jest poprawna liczba binarna")

#Z TROJKOWEGO NA DZIESIETNY
# trojkowa = input("Podaj liczbe trojkowa: ")

# poprawna = True
# for cyfra in trojkowa:
#     if cyfra not in ("0", "1", "2"):
#         poprawna = False
#         break

# if poprawna:
#     dziesietna = 0
#     potega = 0

#     for cyfra in trojkowa[::-1]:
#         dziesietna += int(cyfra) * (3 ** potega)
#         potega += 1

#     print("Liczba dziesietna to:", dziesietna)
# else:
#     print("To nie jest liczba trojkowa!")

