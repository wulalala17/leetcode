# 给定一个二叉树，返回它的 后序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [3,2,1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):  # 后序遍历非递归
        if not root:
            return
        res = []
        l = [root]  # 用栈保存
        while l:
            l0 = l.pop(0)
            if isinstance(l0, TreeNode):  # 是结点说明没访问过，加入子树，注意与出栈顺序相反
                l.append(l0.val)
                if l0.right:
                    l.append(l0.right)
                if l0.left:
                    l.append(l0.left)
            if isinstance(l0, int):  # 是数说明访问过，直接加到结果列表
                res.append(l0)
        return res
