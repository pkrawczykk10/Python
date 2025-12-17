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

def main():
    while True:
        print("=== BIBLIOTEKA PROGRAMÓW W PYTHONIE ===")
        print("11 - Sito Eratostenesa")
        print("10 - Generowanie wyrazow ciagu Fibonacciego iteracyjnie")
        print("9 - Generowanie wyrazow ciagu Fibonacciego rekurencyjnie")
        print("8 - Obliczanie silni iteracyjnie")
        print("7 - Obliczanie silni rekurencyjnie")
        print("6 - Rozklad na czynniki pierwsze")
        print("5 - Zamiana liczby dziesietnej na binarna")
        print("4 - Zamiana liczby binarnej na dziesietna")
        print("3 - Szukanie najmniejszego elementu w liscie")
        print("2 - Porownywanie tekstow")
        print("1 - Odwracanie kolejnosci liter w podanym wyrazie")
        print("0 - Zliczanie wystapien podanego znaku w tekscie")

        try:
            wybor = int(input("Wybierz opcje: "))
        except ValueError:
            print("Podaj poprawny numer!")
            continue

        if wybor == 11:
           sito.sito()
        elif wybor == 10:
            ciagiteracja.ciagiteracja()
        elif wybor == 9:
            ciagrekurencja.ciagrekurencja()
        elif wybor == 8:
            silniaiteracja.silniaiteracja()
        elif wybor == 7:
            silniarekurencja.silniarekurencja()
        elif wybor ==6:
            rozklad.rozklad()
        elif wybor ==5:
            nabinarny.nabinarny()
        elif wybor == 4:
            nadziesietny.nadziesietny()
        elif wybor == 3:
            najmniejszy.najmniejszy()
        elif wybor ==2:
            porownywanie.porownywanie()
        elif wybor ==1:
            odwrocony.odwrocony()
        elif wybor ==0:
            wystapienie.wystapienie()
    
            
            print("Koniec programu. Do zobaczenia!")
            break
        else:
            print("Nie ma takiej opcji!")

if __name__ == "__main_.":
    main()