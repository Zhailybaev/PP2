s=str(input())
p=0
t=""
for i in range(len(s)) :
    if s[i]!=" " :
        p=p+1
        t=t+s[i]
    if s[i]==" " :
        p=0
        t=""
    if p>=3 :
        if i!=len(s)-1 and s[i+1]==" ":
            print(t,end=" ")
        if i==len(s)-1:
            print(t)
            