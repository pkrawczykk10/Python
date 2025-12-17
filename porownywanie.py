def porownywanie():
    tekst1=input("Podaj tekst:")
    tekst2=input("Podaj drugi tekst:")

    if tekst1==tekst2:
        print("Teksty sa takie same")
    else:
        print("Teksty sa rozne")

if __name__=='__main__':
    porownywanie()