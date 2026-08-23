# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.max_difference = 0
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if left_height > right_height:
                difference = left_height - right_height
            else:
                difference = right_height - left_height
            self.max_difference = max(self.max_difference, difference)
            height = max(left_height, right_height) + 1
            return height

        dfs(root)
        return self.max_difference < 2
                
        