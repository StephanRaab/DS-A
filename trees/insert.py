def insert(root, val):
    if not root:
        return TreeNode(val)

    if val > root.right:
        root.right = insert(root.right, val)
    elif val < root.left:
        root.left = insert(root.left, val)
    
    return root
