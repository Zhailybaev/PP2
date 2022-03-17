import os
def count(name):
    with open(name) as f:
        for i,l in enumerate(f) :
            pass
    return i+1
name="C:\\Users\\Asus\\Desktop\\pp2\\lab 6\\dir-and-files\\ex.txt"
print(count(name))
