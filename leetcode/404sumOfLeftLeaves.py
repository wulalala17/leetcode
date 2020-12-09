# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

# Definition for a binary tree node.


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def sumOfLeftLeaves(root):
    if not root:
        return 0
    if root.left == None and root.right == None:
        return 0
    def sumofleft(root, side):  # side表示左子树还是右子树
        if not root:
            return 0
        if root.left == None and root.right == None:
            if side == 'l':
                return root.val
        s = 0
        leftsum = sumofleft(root.left, 'l')
        rightsum = sumofleft(root.right, 'r')
        s = leftsum + rightsum
        return s
    return sumofleft(root, 'l')


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e
print(sumOfLeftLeaves(a))


# def sumOfLeftLeaves(self, root):  别人写的，判断左叶子是亮点
#     """
#     :type root: TreeNode
#     :rtype: int
#     """
#     if root == None:
#         return 0
#     if root.left and root.left.left == None and root.left.right == None:
#         return root.left.val + self.sumOfLeftLeaves(root.right)
#     else:
#         return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)