def findMinNode(root):
    curr = root
    
    while root and curr.left: #while root and left node aren't null
        curr = curr.left
    
    return curr