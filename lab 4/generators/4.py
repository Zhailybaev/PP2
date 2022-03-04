from re import X


a,b=map(int,input().split())
def gen() :

    for i in range(b) :
        x=i*i
        if x>=a and x<=b:
            yield x
for item in gen() :
    print(item)