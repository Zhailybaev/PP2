import re
txt=input()
str=re.findall('[a-z]\S*_\S*[a-z]', txt)
print(str)