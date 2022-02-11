s=input()
t=""
d=set()
r=list()
for i in range(len(s)) :
    if s[i]!=" " :
        if s[i]>='A' and s[i]<="z" :
            t=t+s[i]
    if s[i]==" " :
        d.add(t)
        t=""
    if i==len(s)-1 :
        if t!="" :
            d.add(t)
k=0
for i in d :
    r.append(i)
    k=k+1
r.sort()
print(k)
for i in r :
    print(i)