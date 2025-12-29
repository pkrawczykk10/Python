def odwrocony():
    tekst=input("Podaj ciag znakow:")
    odwrocony=""

    for i in tekst:
        odwrocony=i+odwrocony

    print(f"{odwrocony}")
    input("Nacisnij ENTER aby wrocic do menu")

if __name__=='__main__':
    odwrocony()
