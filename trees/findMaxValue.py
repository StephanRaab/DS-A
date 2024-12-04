def findMax(root):
    curr = root

    while root and curr.right:
        curr = curr.right
    return curr