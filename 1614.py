# leetcode problem no. 1614(Easy )

class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        openBrackets = 0

        # for character c in string s
        for c in s:
            if c == '(':
                openBrackets += 1
            elif c == ')':
                openBrackets -= 1
            
            ans = max(ans, openBrackets)
        
        return ans