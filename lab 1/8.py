s=str(input())
t=str(input())
p=0
for i in range(len(s)) :
    if t==s[i]:
        p=p+1

if p>1 :
 print(s.index(t), end=" ")
 print(s.rindex(t))
else :
    print(s.index(t), end=" ")