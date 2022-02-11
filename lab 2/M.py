x=[]
y=input()
while y!="0" :
    z=[str(a) for a in y.split()]
    z.reverse()
    x.append(z)
    y=input()
x.sort()
for i in x :
    i=i.reverse()
for i in x :
    p=0
    for j in i :
        p=p+1
        if p==3 :
            print(j)
        else :
            print(j,end=" ")
