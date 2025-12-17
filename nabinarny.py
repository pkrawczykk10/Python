def nabinarny():
    x=int(input("Podaj liczbe:"))
    reszty=[]

    while x>0:
        if x%2==1:
            x=(x-1)/2 
        reszty.append(1)
    else:
        x=x/2
        reszty.append(0)

    print(reszty[::-1])

if __name__=='__main__':
    nabinarny()