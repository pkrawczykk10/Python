def wystapienie():
    tekst=input("Podaj dowolny ciag liter:")
    litera=input("Podaj litere, ktorej wystapienie chcesz policzyc:")

    licznik=0

    for znak in tekst:
        if znak==litera:
            licznik+=1

    print(f"Litera '{litera}' wystepuje {licznik} razy.")
    input("Nacisnij ENTER aby wrocic do menu")
    
if __name__=="__main__":
    wystapienie()
