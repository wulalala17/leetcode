# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
# 示例 1:
#
# 输入:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# 输出:
# 合并后的树:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mergeTrees(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1
    def merge(t1, t2): # 错误做法
        t1.val += t2.val
        print('当前的值：', t1.val)

        if not t1.left and t2.left:  # t1没有左子树，但是t2有
            print('当前t1的值:%d t2的值:%d'%(t1.val, t2.val))
            t1.left = t2.left
            print('当前t1左子树的值%d t2左子树的值%d' % (t1.left.val, t2.left.val))
            return
        if t1.left and t2.left:  # t1有左子树，t2也有
            merge(t1.left, t2.left)

        if not t1.right and t2.right:  # t1没有右子树，但是t2有
            print('当前t1的值:%d t2的值:%d' % (t1.val, t2.val))
            t1.right = t2.right
            print('当前t1右子树的值%d t2右子树的值%d' % (t1.right.val, t2.right.val))
            return
        if t1.right and t2.right:  # t1有右子树，t2也有
            merge(t1.right, t2.right)
        inorder(t1)
        return t1
    merge(t1, t2)

def inorder(t1):
    if not t1:
        return
    inorder(t1.left)
    print('中序遍历：', t1.val)
    inorder(t1.right)


a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(2)
d = TreeNode(5)
a.left = b
a.right = c
b.left = d

a1 = TreeNode(2)
b1 = TreeNode(1)
c1 = TreeNode(3)
d1 = TreeNode(4)
e1 = TreeNode(7)
a1.left = b1
a1.right = c1
b1.right = d1
c1.right = e1

mergeTrees(a, a1)
# inorder(a)



class Solution: # 别人的正确做法
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        # if not t1 or not t2: 更简洁
        #     return t1 or t2
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


# class Solution: 官方题解
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         if not t1:
#             return t2
#         if not t2:
#             return t1
# 
#         merged = TreeNode(t1.val + t2.val)
#         merged.left = self.mergeTrees(t1.left, t2.left)
#         merged.right = self.mergeTrees(t1.right, t2.right)
#         return merged
