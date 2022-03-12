import re
txt=input()
str=''.join(x.capitalize() or '_' for x in txt.split('_'))
print(str)