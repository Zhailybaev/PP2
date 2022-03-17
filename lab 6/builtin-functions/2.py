def qwe(s) :
    p=0
    for i in range (len(s)) :     
        if s[i]>='A' and s[i]<='Z' :
            p=p+1
    return p   
def rty(s) :
    k=0
    for i in range (len(s)) :
        if s[i]>='a' and s[i]<='z' :
            k=k+1
    return k

    
s=input()
print(qwe(s))
print(rty(s))