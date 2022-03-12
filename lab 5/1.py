import re
txt=input()
str=re.findall("ab*", txt)
print(str)