# O(n)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

# sorting in descending or reversed order from inorder
def descending(root):
    if not root:
        return
    descending(root.right)
    print(root.val)
    descending(root.left)