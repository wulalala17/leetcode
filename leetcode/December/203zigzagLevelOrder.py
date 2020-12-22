# 103. 二叉树的锯齿形层序遍历
#
# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 返回锯齿形层序遍历如下：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zigzagLevelOrder(root):  # 就是普通左往右层次遍历，利用insert，在每次需要右往左遍历的时候把数据加到数组第一个位置
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    quene = [root]
    flag = 0
    res = []
    while quene:
        l = len(quene)
        layer = []
        if flag == 0:  # 左往右
            flag = 1
            while l > 0:
                q = quene.pop(0)
                l -= 1
                layer.append(q.val)
                if q.left:
                    quene.append(q.left)
                if q.right:
                    quene.append(q.right)
            res.append(layer)
        else:  # 右往左
            flag = 0
            while l > 0:
                q = quene.pop(0)
                l -= 1
                layer.insert(0, q.val)
                if q.left:
                    quene.append(q.left)
                if q.right:
                    quene.append(q.right)
            res.append(layer)
    return res