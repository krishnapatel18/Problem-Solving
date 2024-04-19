# leetcode problem no. 402(Medium )

# Monotonic stack(increasing order ) + greedy [Approach 1 for leading zeros(Optimized )]
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [] 

        for number in num:
            while k > 0 and stack and stack[-1] > number: 
                k -= 1
                stack.pop() 
            stack.append(number)          # 1 for leading zeros    

        stack = stack[:len(stack) - k]  # Removing last k digits 
        result = "".join(stack).lstrip("0")      # 1 for leading zeros 
        return result if result else "0"   # for empty string 



# # Monotonic stack(increasing order ) + greedy [Approach 2 for leading zeros ]
# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         stack = [] 

#         for number in num:
#             while k > 0 and stack and stack[-1] > number: 
#                 k -= 1
#                 stack.pop() 
#             if stack or number is not "0":      # 2 for leading zeros 
#                 stack.append(number)             

#         stack = stack[:len(stack) - k]  # Removing last k digits 
#         result = "".join(stack) 
#         return result if result else "0"   # for empty string 
    

# # Monotonic stack(increasing order ) + greedy [Approach 3 for leading zeros ]
# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         stack = [] 

#         for number in num:
#             while k > 0 and stack and stack[-1] > number: 
#                 k -= 1
#                 stack.pop()  

#             stack.append(number)
#         for i in range(len(stack)):
#             if stack[0] == "0":
#                 stack.pop(0)     # 3 for leading zeros 
#             i += 1

#         stack = stack[:len(stack) - k]  # Removing last k digits 
#         result = "".join(stack)
#         return result if result else "0"   # for empty string 