# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
# 示例
# 1
# 输入：
# 3
# / \
#     9
# 20
# / \
#     15
# 7
# 输出：[3, 14.5, 11]
# 解释：
# 第
# 0
# 层的平均值是
# 3, 第1层是
# 14.5, 第2层是
# 11 。因此返回[3, 14.5, 11] 。
# 提示：
#
# 节点值的范围在32位有符号整数范围内。
#
# 来源：力扣（LeetCode）
# 链接：https: // leetcode - cn.com / problems / average - of - levels - in -binary - tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def levelorder(root):
    quene = [root]
    res = []
    while quene:
        n = len(quene)  #每一层结点个数
        s = 0  # 计算每一层的和
        for i in range(n):
            print('现在结点：%d 队列长度：'%i, n)
            r = quene.pop(0)
            s += r.val
            print(r.val)
            if r.left:
                quene.append(r.left)
            if r.right:
                quene.append(r.right)
        res.append(float(s/n))
    return res

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e
print(levelorder(a))
