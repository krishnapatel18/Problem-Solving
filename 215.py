# leetcode problem no. 215(medium )

import heapq
from heapq import heapify

def findKthLargest(nums, k):
    n = len(nums)
    pq = []
    heapq.heapify(pq)

    for i in range(n):
        heapq.heappush(pq, nums[i])

        if len(pq) > k:
            heapq.heappop(pq)
 
    print(pq[0])

nums = [3,2,1,5,6,4]
k = 2
findKthLargest(nums, k)