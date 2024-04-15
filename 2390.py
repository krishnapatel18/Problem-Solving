# leetcode problem no. 2390(Medium )

# Brute- Force approach  
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        result = ""
        res = []

        for i in range(len(s)):
            if s[i] != '*':
                stack.append(s[i])
            elif s[i] == '*':
                stack.pop()
        
        for j in range(len(stack)):
            temp = stack.pop()
            res.append(temp)

        for j in range(len(res)):
            temp = res.pop()
            result += temp
        
        return result 

# Optimized approach 
class Solution:
    def removeStars(self, s: str) -> str:
        res = []

        for i in s:
            if i == '*':
                res.pop()
            else:
                res.append(i)
        
        return ''.join(res)