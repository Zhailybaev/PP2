n=int(input())
a=[0]*n
t="@"
p=0
for i in range(n) :
    a[i]=input()
for j in range(n) :
    x=a[j].find("@gmail.com")
    for k in range(len(a[j])) :
       if a[j][k]==t :
           p=k 
    if x!=-1 :
        print(a[j][:p])
