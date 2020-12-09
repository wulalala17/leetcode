# 1038.
# 从二叉搜索树到更大和树
# 给出二叉搜索树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点node的新值等于原树中大于或等于node.val的值之和。
# 提醒一下，二叉搜索树满足下列约束条件：
# 节点的左子树仅包含键小于节点键的节点。节点的右子树仅包含键大于节点键的节点。左右子树也必须是二叉搜索树。
# 示例：
#
# 输入：[4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]
# 输出：[30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8]
# 提示：
# 树中的节点数介于 1和100之间。每个节点的值介于0和100之间。给定的树为二叉搜索树。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def bstToGst(TreeNode):
    def dfs(root):
        nonlocal res
        if root:
            dfs(root.right)
            res += root.val
            root.val = res
            dfs(root.left)
    res = 0
    dfs(TreeNode)
    return TreeNode

a = TreeNode(2)
b = TreeNode(0)
c = TreeNode(-4)
d = TreeNode(1)
e = TreeNode(3)
a.left = b
b.right = d
b.left = c
a.right = e
bstToGst(a)
print(a.val)
print(b.val)
print(c.val)
print(d.val)
print(e.val)

