s=str(input())
x=0
y=len(s)
for i in range(y) :
    if s[i]=="1" :
        x=x+pow(2,len(s)-i-1)

print(x)
