# EZ
# is target smaller than root?
# yes, then go to the left and continue until
# is target == root?
# is the val.left/val.right child null?
# Yes? then we're dealing with 0/1 child removal
# return opposite child (this could be a value, or null either way works)
# if it's not null, then we check the opposite side.
# if they're both not null, then we're dealing with a more difficult removal

# HARD
# target for removal has two children
# we check right node, and it's not null
# we check left node, and it's also not null
# we now need to replace the target with the smallest child node, ideally a leaf node
# then recursively call the remove function on the replaced node


# actual implementation now
# start by finding min node helper
def findMinNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

# then we can use it in the remove def
def remove(root, target):
    if not root:
        return None

    if target > root.val:
        root.right = remove(root.right, val)
    elif target < root.val:
        root.left = remove(root.left, val)
    else: # else, we've found the node, so we now check the children
        if not root.left: # ez
            return root.right
        elif not root.right: # ez
            return root.left
        else: # hard
            minNode = findMinNode(root.right)
            root.val = minNode.val # here, we're updating the main root.val with the min node we've just found
            root.right = remove(root.right, minNode.val) # because we copied that value, we now have to go remove the old copy, plus we know this is the smallest value, so the recursive case will be EZ as there's only a max of 1 child node
    return root