def has_33(nums) :
    for i in range(len(nums)) :
        if i<len(nums)-1 :
            if int(nums[i])==int(nums[i+1]) and int(nums[i])==3 :
                return True
    return False
    


nums=list(input().split())

has_33(nums)
if has_33(nums)==True :
    print("True")
else :
    print("False")