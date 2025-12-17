def najmniejszy():
    liczby=[123,43,73,-17,-98,657,832,4,0,10]
    najmniejsza=liczby[0]

    for liczba in liczby:
        if liczba<najmniejsza:
            najmniejsza=liczba

    print("Najmniejsza wartosc w liscie to:", najmniejsza)

if __name__=='__main__':
    najmniejszy()