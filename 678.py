# leetcode problem no. 678(Medium )
# Using two pointer technique(greedy approach ) 

class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        right = 0
        length = len(s) 

        for i in range(length):
            if s[i] == '(' or s[i] == '*':
                left += 1
            else:
                left -= 1

            if s[length - 1 - i] == ')' or s[length - 1 - i] == '*':
                right += 1
            else:
                right -= 1

            if left < 0 or right < 0:
                return False 
        return True 