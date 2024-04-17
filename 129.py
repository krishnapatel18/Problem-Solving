# leetcode problem no. 129(Medium )

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(cur, sum):
            if not cur:
                return 0
            
            sum = sum * 10 + cur.val
            if not cur.left and not cur.right:
                return sum 
            return dfs(cur.left, sum) + dfs(cur.right, sum)
        
        return dfs(root, 0)