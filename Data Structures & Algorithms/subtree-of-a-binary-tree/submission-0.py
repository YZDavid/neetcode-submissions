# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        found = [0]
        def dfs(root):
            if root and subRoot and root.val == subRoot.val:
                status = is_same_tree(root, subRoot)
                if status:
                    found[0] = 1
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        return found[0] == 1