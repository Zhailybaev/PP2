n,k=map(int,input().split())
p=0
l=0
if n<500 :
 for i in range(2,n):
     if n%i==0 :
         l=l+1
 if l==0 :
     if k%2==0 :
         print("Good job!")
     else :
         print("Try next time!")
 else : 
    print("Try next time!")
else : 
    print("Try next time!")