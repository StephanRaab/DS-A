def searchTree(root, target):
    if not root:
        return False
    
    if target > root.val:
        searchTree(root.right, target)
    elif target < root.val:
        searchTree(root.left, target)
    else:
        return True