def ciagiteracja():
    n = int(input("Podaj ile elementów ciągu Fibonacciego: "))

    a = 0
    b = 1

    for i in range(n):
        print(a)
        a, b = b, a + b
        
if __name__ == "__main__":
    ciagiteracja()
