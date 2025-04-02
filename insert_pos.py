def find_index(nums,target):
    
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    else:
        nums.append(target)
    temp=sorted(nums)
        
    for j in range(len(temp)):
        if temp[j]==target:
            return j
    
    
    
    
nums=list(map(int,input().split()))
target=int(input())
print(find_index(nums,target))
        
