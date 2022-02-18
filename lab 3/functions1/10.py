def check(a) :
    k=len(a)

    for i in range(0,k,1) :
        if int(a[i])==int(a[i+1]) and i!=k-1 :
            a.pop(i)
            k=k-1
    print(a)
                
a=list(input().split())
a.sort()
print(a)
check(a)

        