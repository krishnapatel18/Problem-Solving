# leetcode problem no. 394(Medium )

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] 

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                sub_str = ""   # string to store characters 
                while stack[-1] != '[':
                    sub_str = stack.pop() + sub_str     # pop characters till top of the stack != [ 
                stack.pop()     # pop opening bracket 

                num = ""    # string to store digits 
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num    # pop digits till top of the stack == digit 
                stack.append(int(num) * sub_str) 
            
        return "".join(stack) 