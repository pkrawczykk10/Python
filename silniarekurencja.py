def silniarekurencja():
    def silnia(n):
        if n == 0:
            return 1
        return n * silnia(n - 1)

    n = int(input("Podaj liczbę: "))
    print(silnia(n))

if __name__=='__main__':
    silniarekurencja()