import re
txt=input()
str=re.findall("[A-Z][^A-Z]*",txt)
for i in str :
    print(i, end=" ")