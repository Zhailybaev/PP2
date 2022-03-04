n=int(input())
def gen() :
    x=1
    yield x
    while x*x<n :
        x=x+1
        yield x*x



for item in gen() :
    print(item)
