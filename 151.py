# leetcode problem no. 151(Easy )

# Approach 1 
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = s.split()
        result = []

        for char in range(len(stack) + 1):
            if char:
                temp = stack.pop()
                result.append(temp)
        
        final = ' '.join(result)
        return final 
    


# Approach 2 
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        reversed_string = ''.join(words)
        return reversed_string