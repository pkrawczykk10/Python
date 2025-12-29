import sito
import ciagiteracja
import ciagrekurencja
import silniaiteracja
import silniarekurencja
import rozklad
import nabinarny
import nadziesietny
import najmniejszy
import porownywanie
import odwrocony
import wystapienie

while True:
    print("\nMENU")
    print("1. Sito Eratostenesa")
    print("2. Fibonacci iteracyjnie")
    print("3. Fibonacci rekurencyjnie")
    print("4. Silnia iteracyjnie")
    print("5. Silnia rekurencyjnie")
    print("6. Rozkład na czynniki pierwsze")
    print("7. Dziesiętna na binarną")
    print("8. Binarna na dziesiętną")
    print("9. Najmniejszy element w liscie")
    print("10. Porównywanie tekstów")
    print("11. Odwracanie wyrazu")
    print("12. Zliczanie znaku")
    print("0. Wyjście")
    
    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        sito.sito()
    elif wybor == "2":
        ciagiteracja.ciagiteracja()
    elif wybor == "3":
        ciagrekurencja.ciagrekurencja()
    elif wybor == "4":
        silniaiteracja.silniaiteracja()
    elif wybor == "5":
        silniarekurencja.silniarekurencja()
    elif wybor == "6":
        rozklad.rozklad()
    elif wybor == "7":
        nabinarny.nabinarny()
    elif wybor == "8":
        nadziesietny.nadziesietny()
    elif wybor == "9":
        najmniejszy.najmniejszy()
    elif wybor == "10":
        porownywanie.porownywanie()
    elif wybor == "11":
        odwrocony.odwrocony()
    elif wybor == "12":
        wystapienie.wystapienie()
    elif wybor == "0":
        print("Koniec")
        break
    else:
        print("Zły wybór")
