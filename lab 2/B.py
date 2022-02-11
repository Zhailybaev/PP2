n = int(input())
b = list(map(int, input().split(maxsplit = n)))
a=[0]*n
for i in range(n) :
    a[i]=int(b[i])
a.sort()
x=int(a[n-2])
y=int(a[n-1])
print(x*y)