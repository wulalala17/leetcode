# 根据一棵树的中序遍历与后序遍历构造二叉树。
# 注意:
# 你可以假设树中没有重复的元素。
# 例如，给出
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
#
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(inorder, postorder):  # 参考别人的
    genjiedian = postorder[-1]
    i = inorder.index(genjiedian) # 根结点在中序遍历里的下标
    root = TreeNode(postorder[-1])
    root.left = buildTree(inorder[:i], postorder[:i])
    root.right = buildTree(inorder[i+1:], postorder[i:-1])
    return root



# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode: