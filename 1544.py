# leetcode problem no. 1544(Easy )

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        # for character c in string s
        for c in s:
            # The ord() function returns the number representing the unicode code of a specified character.
            # The abs() function returns the absolute value of the specified number.
            # In unicode code difference between uppercase letters and lowercase letters is “32”.
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
            
        return ''.join(stack)