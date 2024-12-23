// 94. Binary Tree Inorder Traversal

public class Solution {
    List<int> res = new List<int>();

    public IList<int> InorderTraversal(TreeNode root) {
        if (root == null)
            return res;
        
        InorderTraversal(root.left);
        res.Add(root.val);
        InorderTraversal(root.right);
        return res;
    }
}