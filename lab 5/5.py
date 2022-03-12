import re
txt=input()
str=re.findall('a.*?b$',txt)
print(str)