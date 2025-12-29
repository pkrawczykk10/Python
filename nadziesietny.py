def nadziesietny():
    binarna = (input("Podaj liczbe w systemie binarnym: "))

    poprawna = True
    for cyfra in binarna:
        if cyfra != "0" and cyfra != "1":
            poprawna = False
            break

    if poprawna:
        dziesietna = 0
        potega = 0
        
        for cyfra in binarna[::-1]:
            if cyfra == "1":
                dziesietna += 2 ** potega
            potega += 1

        print("Liczba dziesietna to:", dziesietna)
    else:
        print("To nie jest poprawna liczba binarna")
    input("Nacisnij ENTER aby wrocic do menu")

if __name__=='__main__':
    nadziesietny()
    nadziesietny()
