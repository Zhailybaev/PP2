import math
z=dict()
n,k=map(int,input().split())
q=int(input())
p=0
a=list()
b=list()
for i in range(q) :
    w=input().split()
    x=int(w[0])
    y=int(w[1])
    r=(x-n)**2+(y-k)**2
    d=math.sqrt(r)
    z[d]=w
    a.append(d)
a.sort()
for i in a:
    for j in z.keys() :
        if i==j :
            b.append(z[j]) 
for i in b :
    print(i[0], i[1])

