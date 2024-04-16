# leetcode problem no. 404(Easy )

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(cur, sum, is_left):
            if not cur:
                return 0

            if not cur.left and not cur.right and is_left:
                return cur.val

            return dfs(cur.left, 0, True) + dfs(cur.right, 0, False)

        return dfs(root, 0, False)