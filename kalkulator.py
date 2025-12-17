print("dostepne operacje: +, -, *, /, %, **")

liczba1=float(input("Podaj pierwsza liczbe:"))
znak=input("Podaj znak dzialania:")
liczba2=float(input("Podaj druga liczbe:"))

if znak== '+':
    wynik=liczba1+liczba2
elif znak=='-':
    wynik=liczba1-liczba2
elif znak=='*':
    wynik=liczba1*liczba2
elif znak=='/':
    if liczba2==0:
        wynik="Blad:nie mozna dzielic przez 0!"
    else:
        wynik=liczba1/liczba2
elif znak=='%':
    if liczba2==0:
        wynik=("Blad:nie mozna dzielic przez0!")
    else:
        wynik=liczba1%liczba2
elif znak=='**':
    wynik=liczba1**liczba2
else:
    print("nieznany typ dzialania")

print(f"wynik:{wynik}")
