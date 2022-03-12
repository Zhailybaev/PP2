import re
txt=input()
str=re.findall('[A-Z]+[a-z]+', txt)
print(str)