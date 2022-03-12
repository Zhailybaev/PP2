import re
txt=input()
str=re.sub("[ ,.]", ":",txt)
print(str)