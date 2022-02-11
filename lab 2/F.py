n=int(input())
d={}
for i in range(n) :
    s,x=input().split()
    d[s]=d.get(s,0)+int(x)
y=0
for s,x in sorted(d.items()) :
    if d[s]>y :
        y=d[s]
for s,x in sorted(d.items()) :
    x=y-d[s]
    if x==0 :
        print(s,"is lucky!")
    else :
        print(s,"has to receive" ,x,"tenge")
