n=int(input())
a=[[0]*n for i in range(n)]
if n%2==0 :
    for i in range(n) :
        for j in range(n) :
            if i<j :
                a[i][j]="."
            if i>=j :
                a[i][j]="#"
if n%2!=0 :
    for i in range(n) :
        for j in range(n) :
            if i<n-j-1 :
                a[i][j]="."
            if i>=n-j-1 :
                a[i][j]="#"
for k in range(n) :
    for l in range(n) :
        print(a[k][l], end="")  
    print()  
        