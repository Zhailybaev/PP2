n=int(input())
a=dict()
b=dict()
m=1
for i in range(n) :
    x=input().split()
    r=x[1]
    a[r]=a.get(r,0)+m
k=int(input())
for i in range(k) :
    y=input().split()
    z=y[1]
    w=int(y[2])
    b[z]=b.get(z,0)+w
p=0
l=0
for r,m in sorted(a.items()) :
    for z,w  in sorted(b.items()) :
        if r==z :
            p=w-m
            if p<0 :
                l=l+1
    if r not in b.keys() :
        l=l+1
print("Demons left:",l)