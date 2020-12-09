
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root):
    # res = []
    if root == None:
        return
    #if root.left and root.left.val != 'null':
    inorderTraversal(root.left)
    res.append(root.val)
    #if root.right and root.right.val != 'null':
    inorderTraversal(root.right)
    return res

    # l = inorderTraversal(root.left)
    # r = inorderTraversal(root.right)
    # return l + [root.val] + r

def inorder2(root): #非递归
    res2 = []
    stack = []
    r = root
    while stack or r:
        if r:  #走到最左边
            stack.append(r)
            r = r.left
        else:
            r = stack.pop()
            res2.append(r.val)
            r = r.right
    return res2
# class Solution: # 太强了 颜色标记法  https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         stack,rst = [root],[]
#         while stack:
#             i = stack.pop()
#             if isinstance(i,TreeNode): # 是结点表示还没访问过
#                 stack.extend([i.right,i.val,i.left])  # 中序遍历 栈是先进后出，入栈顺序要反过来
#             elif isinstance(i,int): # 是数字（结点的值）表示访问过，
#                 rst.append(i)
#         return rst

a = TreeNode(1)
c = TreeNode(2)
d = TreeNode(3)
a.right = c
c.left = d
res = []
print(inorderTraversal(a))
print(inorder2(a))