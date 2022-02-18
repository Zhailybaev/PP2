class Prime :
    def __init__(self,a) :
        self.a=a

    def filter(self) :
        Primes=list(filter(lambda x: prime(x), self.a))
        print(Primes)
def prime(x) :
    l=0
    y=int(x)
    for i in range(2,y) :
        if y%i==0 :
            l=l+1
    if l==0 :
        return y      
q=list(input().split())

w=Prime(q)
w.filter()
