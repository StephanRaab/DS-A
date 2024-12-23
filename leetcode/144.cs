// 144. Binary Tree Preorder Traversal

public class Solution {
    List<int> res = new List<int>();

    public IList<int> PreorderTraversal(TreeNode root) {
        if (root == null) return res;

        res.Add(root.val);
        PreorderTraversal(root.left);
        PreorderTraversal(root.right);
        return res;
    }
}