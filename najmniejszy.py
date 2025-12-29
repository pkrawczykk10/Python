def najmniejszy():
    liczby = []
    
    n = int(input("Ile liczb chcesz podać? "))
    
    for i in range(n):
        x = int(input("Podaj liczbę: "))
        liczby.append(x)
    
    najmniejsza = liczby[0]
    
    for liczba in liczby:
        if liczba < najmniejsza:
            najmniejsza = liczba
    
    print("Najmniejsza liczba to:", najmniejsza)
    input("Nacisnij ENTER aby wrocic do menu")
    
if __name__=='__main__':
    najmniejszy()
