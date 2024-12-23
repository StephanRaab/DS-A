// 145. Binary Tree Postorder Traversal

public class Solution {
    List<int> res = new List<int>();
    public IList<int> PostorderTraversal(TreeNode root) {
        if (root == null) return res;

        PostorderTraversal(root.left);
        PostorderTraversal(root.right);
        res.Add(root.val);

        return res;
    }
}