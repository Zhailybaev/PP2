import os
path="c:\\Users\\Asus\\Desktop\\pp2\\lab 6"

print("Result:", os.access(path, os.F_OK))
print("Result:", os.access(path, os.R_OK))
print("Result:", os.access(path, os.W_OK))
print("Result:", os.access(path, os.X_OK))

