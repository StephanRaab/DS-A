def searchTree(root, target):
    # no valid node, so it must be false
    if not root:
        return False

    # valid node, so decide which way to go
    if target > root.val:
        searchTree(root.right, target)
    elif target < root.val:
        searchTree(root.left, target)
    else:
        return True