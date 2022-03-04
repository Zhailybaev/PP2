from re import X


n=int(input())
def gen() :
    x=0
    while x<n :
        yield x 
        x=x+12
for item in gen() :
    print(item)