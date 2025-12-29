def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n - 1)

def silniarekurencja():
    n = int(input("Podaj n: "))
    print("Silnia:", silnia(n))
    input("Nacisnij ENTER aby wrocic do menu")

if __name__ == "__main__":
    silniarekurencja()
