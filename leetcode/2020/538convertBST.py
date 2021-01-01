# 给定一个二叉搜索树（Binary
# Search
# Tree），把它转换成为累加树（Greater
# Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
# 例如：
# 输入: 原始二叉搜索树:
# 5
# / \
# 2
# 13
# 输出: 转换为累加树:
# 18
# / \
# 20
# 13


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treesum(root, k):  # 计算整棵树大于k值的结点的和
    if not root:
        return 0
    s = 0
    if root.val > k:
        s = root.val
    l = treesum(root.left, k)
    r = treesum(root.right, k)
    return l + s + r

def convertBST(root):
    if not root:
        return
    s1 = treesum(root, root.val)
    newroot = root
    newroot.val += s1
    newroot.left.val += treesum(root, root.left.val)
    newroot.right.val += treesum(root, root.right.val)
    return newroot


res = []
def inorderTraversal(root):
    # res = []
    if root == None:
        return
    #if root.left and root.left.val != 'null':
    res.append(root.val)
    inorderTraversal(root.left)
    #if root.right and root.right.val != 'null':
    inorderTraversal(root.right)
    return res

a = TreeNode(2)
b = TreeNode(0)
c = TreeNode(-4)
d = TreeNode(1)
e = TreeNode(3)
a.left = b
b.right = d
b.left = c
a.right = e
ff = convertBST(a)
print(inorderTraversal(ff))


# def dfs(root: TreeNode):
#     nonlocal total
#     if root:
#         dfs(root.right)
#         total += root.val
#         root.val = total
#         dfs(root.left)
#
#
# total = 0
# dfs(root)
# return root