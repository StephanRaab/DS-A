// 112. Path Sum

public class Solution {
    public bool HasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;

        targetSum -= root.val;

        if (root.left == null && root.right == null){
            // this is a treenode
            return targetSum == 0;
        }

        return HasPathSum(root.left, targetSum) || HasPathSum(root.right, targetSum);
    }
}