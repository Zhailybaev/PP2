n=int(input())
a=[[0]*n for i in range(n)]
for i in range(n) :
    for j in range(n) :
        a[0][j]=j
        a[i][0]=i
        if i==j and i!=0 :
            a[i][j]=i*j
        else : 
         a[i][j]=0
for k in range(n) :
    for l in range(n) :
        print(a[k][l], end=" ")
    print()