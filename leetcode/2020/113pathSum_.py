# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
# 说明: 叶子节点是指没有子节点的节点。
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:  # 想不出怎么遍历所有和的方法 放弃了

def pathSum(root, sum):
    cur_res = []
    res = []
    s = 0
    def countsum(root, sum, cur_res):
        if not root:
            return
        cur_res.append(root.val)
        if not root.left and not root.right: # 到达叶子结点
            if root.val == sum:
                res.append(cur_res[:])

        countsum(root.left, sum-root.val, cur_res[:])
        countsum(root.right, sum-root.val, cur_res[:])
        cur_res.pop()
    countsum(root, sum, cur_res)
    return res

def shit(root, res):
    if not root:
        return
    res.append(root.val)
    shit(root.left, res)
    shit(root.right, res)
    return res


a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(8)
d = TreeNode(11)
e = TreeNode(13)
f = TreeNode(7)
g = TreeNode(2)
h = TreeNode(5)
i = TreeNode(1)
l = TreeNode(4)

a.left = b
a.right = c
b.left = d
c.left = e
c.right = l
d.left = f
d.right = g
l.left = h
l.right = i

# print(pathSum(a, 22))
print(shit(a, []))



