# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。
# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。
# 例如,
#
# 给定二叉搜索树:
# 4
# / \
#     2
# 7
# / \
#     1
# 3 和插入的值: 5
# 你可以返回这个二叉搜索树:
#
# 4
# / \
#     2
# 7
# /  \ /
# 1
# 3
# 5
#
# 或者这个树也是有效的:
# 5
# / \
#     2
# 7
# / \
#     1
# 3
# \
# 4
# 提示：
# 给定的树上的节点数介于0和10 ^ 4之间,每个节点都有一个唯一整数值，取值范围从0到10 ^    -10 ^ 8 <= val <= 10 ^ 8
# 新值和原始二叉搜索树中的任意节点值都不同


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if val > root.val:  # 比当前结点的值大就往右子树走
            if root.right:
                self.insertIntoBST(root.right, val)
            else:  # 没有右子树则直接插入
                root.right = TreeNode(val)
        if val < root.val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        return root

# class Solution:  迭代法
#     def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#         if not root:
#             return TreeNode(val)
#         node, prev = root, None
#         while node:
#             prev = node
#             node = node.left if val < node.val else node.right
#         if val < prev.val:
#             prev.left = TreeNode(val)
#         else:
#             prev.right = TreeNode(val)
#         return root
#
# 作者：flyhigher139
# 链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/solution/di-gui-fa-by-flyhigher139/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
