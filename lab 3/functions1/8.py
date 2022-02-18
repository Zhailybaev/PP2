from re import A


a=list()
def spy_game(nums) :

    for i in range(len(nums)) :
        if nums[i]=="0" or nums[i]=="7" :
            a.append(nums[i])
    return a 

nums=list(input().split())
spy_game(nums)
if a[0]=="0" and a[1]=="0" and a[2]=="7" :
    print("True")
else :
    print("False")