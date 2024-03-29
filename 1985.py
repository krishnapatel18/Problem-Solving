# # leetcode problem no. 1985(medium )

import heapq
from heapq import heapify

def kthLargestNumber(nums, k):
    heapq.heapify(nums)

    for i in range(k-1):
        nums.pop()
    
    return nums.pop()




# def kthLargestNumber(nums, k):
    # n = len(nums)

    # nums.sort()            

    # for i in range(k-1):
    #     nums.pop()
    
    # return nums.pop()


nums = [3, 6, 7, 10]
k = 4   # fourth largest number == 3
print(kthLargestNumber(nums, k)) 


nums = [2, 21, 12, 1]
k = 3   # third largest number == 2
print(kthLargestNumber(nums, k))


# nums = [0, 0]
# k = 2   # second largest number == 0
# print(kthLargestNumber(nums, k))