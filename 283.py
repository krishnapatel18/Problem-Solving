# leetcode problem no. 283(Easy )

# Brute Force approach 
def moveZeroes(nums):
    l = len(nums)
    count = 0
    for i in range(l):
        if nums[i] != 0:
            nums.append(nums[i])
            count += 1
            
    zeros = l - count
    for i in range(zeros):
        nums.append(0)
    
    for i in range(l):
        nums.pop(0)

    return nums

nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))


# An optimized approach  
def moveZeroes(nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1 