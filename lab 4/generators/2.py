from re import X


n=int(input())
def gen() :
    x=2
    while x<=n :
        yield x 
        x=x+2
for item in gen() :
    print(item)