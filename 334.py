# leetcode problem no. 334(Medium )

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums: 
            # if num in nums is smaller than infinity, first = num 
            if num <= first:
                first = num
            #  if num is not smallest, but small than second = num 
            elif num <= second:
                second = num
            # otherwise it is greater than both first and second 
            else:
                return True 
        
        return False