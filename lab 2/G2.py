n=int(input())
a=dict()
w=1
for i in range(n) :
    x=input().split()
    z=x[1]
    a[z]=a.get(z,0)+w
k=int(input())
for i in range(k) :
    y=input().split()
    if y[1] in a :
        a[y[1]]=int(a[y[1]])-int(y[2])
d=0
for i in a.values() :
    if int(i)>0 :
        d=d+int(i)
print("Demons left:", d)
