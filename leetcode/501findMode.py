# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
# 假定 BST 有如下定义：
#
#     结点左子树中所含结点的值小于等于当前结点的值
#     结点右子树中所含结点的值大于等于当前结点的值
#     左子树和右子树都是二叉搜索树
# 例如：
# 给定 BST [1,null,2,2],
#
#    1
#     \
#      2
#     /
#    2
# 返回[2].
# 提示：如果众数超过1个，不需考虑输出顺序
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# d = {}
def findMode(root, d):
    # nonlocal d
    if not root:
        return
    i = root.val
    d[i] = d.get(i, 0) + 1
    findMode(root.left, d)
    findMode(root.right, d)
    d1 = sorted(d.items(), key=lambda item: item[1], reverse=True)  # 按照字典的value降序排序
    res = []
    for it in d1:
        if it[1] == d1[0][1]:
            res.append(it[0])
    return res

def findMode2(root):
    nowres = []
    def cnm(root):
        nonlocal nowres
        if not root:
            return
        cnm(root.left)
        nowres.append(root.val)
        cnm(root.right)

def mostfrequencynumber(l):
    if len(l) <=1 :
        return l
    realres = [l[0]]
    nowtimes = 0
    maxtimes = 1
    for i in range(1, len(l)):
        if l[i] == l[i-1]:
            nowtimes += 1
            if nowtimes > maxtimes:
                del realres[:]
                maxtimes = nowtimes
                realres.append(l[i])
            elif nowtimes == maxtimes:
                realres.append(l[i])
        else:
            nowtimes = 1
    return realres



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(3)
a.left = b
b.left = c
a.right = d
d.left = e
res2 = []
#print(findMode(a, {}))
#print(findMode2(a, [], 0, 0))
print(mostfrequencynumber([1,2,2,3,3,3]))

# class Solution:
#     def findMode(self, root: TreeNode) -> List[int]:
#         ans=[]
#         most=0
#         last=None
#         cnt=0
#
#         def inorder(node):
#             if not node: return
#             nonlocal ans,most,last,cnt
#             if node.left: inorder(node.left)
#             if node.val==last:
#                 cnt+=1
#             else: cnt=1
#             if cnt==most: ans.append(node.val)
#             elif cnt>most:
#                 most=cnt
#                 ans=[node.val]
#             last=node.val
#             if node.right: inorder(node.right)
#
#         inorder(root)
#         return ans
