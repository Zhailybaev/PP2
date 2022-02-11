x=input()
sum=0
for i in range(len(x)):
 sum=sum+ord(x[i])
if sum>300:
 print("It is tasty!")
else: print("Oh, no!")