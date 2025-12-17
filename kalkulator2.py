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
    try:
        wynik=liczba1/liczba2
    except ZeroDivisionError:
        print("Nie mozna dzielic przez 0!")
elif znak=='%':
    try:
        wynik=liczba1%liczba2
    except ZeroDivisionError:
        print("Nie mozna dzielic przez 0!")
elif znak=='**':
    wynik=liczba1**liczba2
else:
    print("nieznany typ dzialania")

print(f"wynik:{wynik}")
