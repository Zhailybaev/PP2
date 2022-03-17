def check(x) :
    l=len(x)
    for i in range(l) :
        if x[i]!=x[l-i-1] :
            return False
    return True 

x=input()
check(x)
if check(x)==False :
    print("False")
else :
    print("True")