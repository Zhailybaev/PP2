n=int(input())
a=list()
set=set()
b=list()
for i in range(n) :
    x=input()
    a.append(x)
for s in a :
    p=0
    k=0
    l=0
    for j in range(len(s)) :
        if s[j]>="A" and s[j]<="Z" :
            p=p+1
        if s[j]>="a" and s[j]<="z" :
            k=k+1
        if s[j]>="0"  and s[j]<="9":
            l=l+1
    if p>0 and k>0 and l>0:
        set.add(s)
t=0
for i in set :
    t=t+1
    b.append(i)
b.sort()
print(t)
for i in b :
    print(i)