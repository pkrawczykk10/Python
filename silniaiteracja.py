def silniaiteracja():
    liczba=int(input("Podaj liczbe calkowita nieujemna:"))
    if liczba<=0:
        print("Silnia nie jest zdefiniowana dla liczb ujemnych.")
    else:
        silnia = 1
        for i in range(1, liczba + 1):
            silnia = silnia * i
        print(f"{liczba}! = {silnia}")

if __name__=='__main__':
    silniaiteracja()