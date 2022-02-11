def function(array):
    p=0
    m=0
    while p< len(array):
        if p> m :
            return False
        if p+array[p] > m:
            m= p+array[p]
        if m>= len(array) - 1:
            return True
        p=p+1
a = [int(i) for i in input().split()]
if(function(a)==True):
    print(1)
else:
    print(0)
