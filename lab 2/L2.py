s=input()
p=0
if len(s)%2!=0 :
    print("No")
else :
    for i in range(len(s)) :
        if s[i]=="[" or s[i]=="{" or s[i]=="(" :
            p=p+1
        if s[i]=="]" or s[i]=="}" or s[i]==")" :
            p=p-1
    k=0
    if p==0 :
        for i in range(len(s)) :
            if i<len(s)/2:
                if s[i]=="[" and s[len(s)-1-i]=="]" :
                    k=k+1
                if s[i]=="{" and s[len(s)-1-i]=="}" :
                    k=k+1
                if s[i]=="(" and s[len(s)-1-i]==")" :
                    k=k+1
        if k>0 :
            print("Yes")
        else :
            print("No")
    else :
        print("No")
