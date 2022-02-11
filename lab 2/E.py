n=input().split()

if len(n)==1 :
    y=int(input())
    x=int(n[0])
else :
    x=int(n[0])
    y=int(n[1])
a=[0]*x
b=0
for i in range(x) :
    a[i]=y+2*i
for j in range(x) :
    b=b^a[j]
print(b)
