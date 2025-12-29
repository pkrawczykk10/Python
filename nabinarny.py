def nabinarny():
    liczba = int(input("Podaj liczbę dziesiętną: "))

    wynik = ""

    while liczba > 0:
        reszta = liczba % 2
        wynik = str(reszta) + wynik
        liczba = liczba // 2

    print("Liczba w systemie binarnym:", wynik)
    input("Nacisnij ENTER aby wrocic do menu")

if __name__=='__main__':
    nabinarny()
