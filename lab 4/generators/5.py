from re import X


n=int(input())
def gen() :
    x=n
    while x>=0 :
        yield x 
        x=x-1
for item in gen() :
    print(item)