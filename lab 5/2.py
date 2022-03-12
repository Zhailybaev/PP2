import re
txt=input()
str=re.search("ab{2,3}", txt)
print(str.string)