def sito():
    def sitoEratostenesa(n):
        if n<2:
            return[]
        
        sito=[True]*(n+1)

        sito[0], sito[1]=False, False
        
        for i in range (2, n+1):
            if sito[i]: #to znaczy ze sprawdzamy czy to jest prawdziwe
                j=i+i
                while j<=n:
                    sito[j]=False
                    j+=i
        
        return sito

    sito=sitoEratostenesa(483920)

    for i in range(len(sito)):
        if sito[i]:
            print(i)

if __name__=='__main__':
    sito()