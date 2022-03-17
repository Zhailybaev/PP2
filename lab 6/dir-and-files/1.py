#f=open(r"c:\Users\Asus\Desktop\pp2\lab 6\dir-and-files\ex.txt","a")
#print(f.read())
#f.write('\nnew line')
#f.close()
import os
def qwe(item):
    if os.path.isdir(item):
        print(os.listdir(item))

print(os.listdir())
for item in os.listdir(".") :
    qwe(item)