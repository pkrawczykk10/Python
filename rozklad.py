def rozklad():
    n=int(input("Podaj liczbe:"))
    dzielnik=2
    czynniki=[]
    while n!=1:
        if n % dzielnik==0:
            n=n/dzielnik
            czynniki.append(dzielnik)
        else:
            dzielnik=dzielnik+1

    print(f"Rozklad tej liczby na czynniki pierwsze to:{czynniki}")

if __name__=='__main__':
    rozklad()




