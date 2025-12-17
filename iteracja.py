liczby=[123,43,73,-17,-98,657,832,4,0,10]
najmniejsza=liczby[0]

for liczba in liczby:
    if liczba<najmniejsza:
        najmniejsza=liczba

print("Najmniejsza wartosc w liscie to:", najmniejsza)



# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



liczba=int(input("Podaj liczbe calkowita nieujemna:"))
if liczba<=0:
    print("Silnia nie jest zdefiniowana dla liczb ujemnych.")
else:
    silnia = 1
    for i in range(1, liczba + 1):
        silnia = silnia * i
    print(f"{liczba}! = {silnia}")


# try:
#     wysokosc= int(input("Podaj wysokosc trojkata:"))
#     if wysokosc <=0:
#         print("Wysokosc musi byc liczba dodatnia wieksza od zera.")
#     else:
#         for i in range(wysokosc):
#             spacje=i
#             gwiazdki=2*(wysokosc - i) - 1
#             print(" "*spacje+ "*" *gwiazdki)

# except ValueError:
#     print("Blad: Prosze wpisac liczbe calkowita.")


tekst=input("Podaj dowolny ciag liter:")
litera=input("Podaj litere, ktorej wystapienie chcesz policzyc:")

licznik=0

for znak in tekst:
    if znak==litera:
        licznik+=1

print(f"Litera '{litera}' wystepuje {licznik} razy.")


tekst=input("Podaj ciag znakow:")
odwrocony=""

for i in tekst:
    odwrocony=i+odwrocony

print(f"{odwrocony}")

# bok1=int(input("Podaj liczbe calkowita: "))
# bok2=int(input("Podaj liczbe calkowita:"))

# for i in range(bok1):
#     for j in range(bok2):
#         if(i+j)%2==0:
#             print("O", end="")
#         else:
#             print("X", end="")

#     print()


def wypisz_rosnaco(n, i=1):
    if i>n:
        return
    print(i)
    wypisz_rosnaco(n, i+1)

n=int(input("Podaj liczbe:"))
wypisz_rosnaco(n)



