import re
txt=input()
str=re.findall("[A-Z][^A-Z]*",txt)
print(str)