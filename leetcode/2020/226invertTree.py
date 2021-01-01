class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invertTree(root):
    if root == None:
        return root
    f = root.right
    root.right = root.left
    root.left = f
    root.left = invertTree(root.left)
    root.right = invertTree(root.right)
    return root

