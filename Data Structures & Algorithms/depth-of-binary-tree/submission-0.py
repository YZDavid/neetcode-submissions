# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def dfs(node, depth):
            if not node:
                return depth
            depth += 1
            left_depth, right_depth = 0, 0
            if node.left:
                left_depth = dfs(node.left, depth)
            if node.right:
                right_depth = dfs(node.right, depth)
            depth = max(depth, left_depth, right_depth)
            return depth
        
        max_depth = dfs(root, max_depth)
        return max_depth