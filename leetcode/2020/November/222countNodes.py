# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
# 示例:
#
# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# 输出: 6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# class Solution(object):  别人的递归写法，利用完全二叉树的性质
#     def countNodes(self, root):
#         if not root:
#             return 0
#         lh, rh = self.__getHeight(root.left), self.__getHeight(root.right)
#         if lh == rh:  # 左右子树高度相同，说明左子树必满 则节点数=左子树节点 + root节点(=1) + 递归找右子树
#             return (pow(2, lh) - 1) + 1 + self.countNodes(root.right)
#         else:  # 左子树比右子树高，说明右子树必满 同理
#             return (pow(2, rh) - 1) + 1 + self.countNodes(root.left)
#
#     def __getHeight(self, root):
#         ret = 0
#         while root:
#             ret += 1
#             root = root.left
#         return ret