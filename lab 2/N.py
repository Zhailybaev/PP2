a=[]
x=1
while x!=0 :
    x=int(input())
    a.append(x)
a.remove(0)
for i in range(len(a)) :
    if len(a)%2==0 and i<len(a)/2 :
        sum=a[i]+a[len(a)-1-i]
        print(sum, end=" ")
    if len(a)%2!=0 and i==(len(a)-1)/2 :
        sum=a[i]
        print(sum, end=" ")
    if len(a)%2!=0 and i<(len(a)-1)/2 :
        sum=a[i]+a[len(a)-1-i]
        print(sum, end=" ")
    
