
n=int(input())
a=[0]*n
for i in range(n) :
    a[i]=int(input())
for j in range(n) :
    if a[j]<10 or a[j]==10 :
        print("Go to work!")
    if a[j]>10 and a[j]<25 or a[j]==25 :
        print("You are weak")
    if a[j]>25 and a[j]<45 or a[j]==45 :
        print("Okay, fine")
    if a[j]>45 :
        print("Burn! Burn! Burn Young!")