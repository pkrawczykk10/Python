def sito():
    n = int(input("Podaj n: "))
    pierwsze = [True] * (n + 1)
    pierwsze[0] = pierwsze[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if pierwsze[i]:
            for j in range(i * i, n + 1, i):
                pierwsze[j] = False

    print("Liczby pierwsze:")
    for i in range(2, n + 1):
        if pierwsze[i]:
            print(i, end=" ")
            
    input("Nacisnij ENTER aby wrocic do menu")

if __name__=='__main__':
    sito()
