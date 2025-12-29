def ciagiteracja():
    n = int(input("Ile wyrazów? "))
    
    a = 0
    b = 1
    
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c
        
    input("Nacisnij ENTER aby wrocic do menu")
        
if __name__ == "__main__":
    ciagiteracja()
