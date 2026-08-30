/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxDiameter;

    public int diameterOfBinaryTree(TreeNode root) {
        this.maxDiameter = 0;
        dfs(root);
        return this.maxDiameter;
    }

    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = this.dfs(root.left);
        int right = this.dfs(root.right);
        this.maxDiameter = Math.max(this.maxDiameter, left + right);
        return 1 + Math.max(left, right);
    }
}
