def histogram(x) :
    for i in range(x) :
        print("*", end="")
    print()
a=list(input().split())
for i in a :
    histogram(int(i))