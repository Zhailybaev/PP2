def mult(a):
    s=1
    for i in  range(len(a)):
        if a[i]!=" ":
            x=int(a[i])
            s=s*x
    return s


a=input()

print(mult(a))
