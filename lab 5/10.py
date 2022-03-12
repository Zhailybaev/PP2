import re
txt=input()
t=re.findall("[a-z]+", txt)
str=re.findall("[A-Z]+[a-z]+",txt)
for j in t:
    print(j, end="")
    break
for i in str :
    print("_" , end="")
    print(i.lower(),end="")

