# leetcode problem no. 392(Easy )

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t):     # base case 
            return False 
        if s == "":     # base case 
            return True 

        i = 0 
        for j in t:
            if i < len(s) and j == s[i]:
                i += 1
        
        if i == len(s):
            return True 
        return False 


# Need modifications 
# def isSubsequence(s, t):
#     visited = []
#     extra = []
    
#     for i in range(len(s)):
#         for j in range(len(t)): 
#             if s[i] == t[j]: 
#                 visited.append(s[i]) 
#             extra.append(t[j])
#         i += 1 
    
#     if ''.join(visited) == s: 
#         return True 
#     return False 

# s = "acb" 
# t = "ahbgdc"
# print(isSubsequence(s, t))