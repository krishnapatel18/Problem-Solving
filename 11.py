# leetcode problem no. 11(Medium )

# # Brute Force approach 
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         result = 0 

#         for left in range(len(height)):
#             for right in range(len(height)):
#                 area = (right - left) * min(height[left], height[right]) 
#                 result = max(result, area)  
            
#         return result  


# Optimized approach 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0  
        left, right = 0, len(height) - 1 

        while left < right:
            area = (right - left) * min(height[left], height[right]) 
            result = max(result, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1 

        return result 