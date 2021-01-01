# 给定一个二叉树
# struct
# Node
# {
#     int val;
# Node * left;
# Node * right;
# Node * next;
# }
# 填充它的每个next指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将next指针设置为NULL。
# 初始状态下，所有next指针都被设置为NULL。
# 进阶：
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
# 示例：
# 输入：root = [1, 2, 3, 4, 5, null, 7]
# 输出：[1,  # ,2,3,#,4,5,7,#]解释：给定二叉树如图A所示，你的函数应该填充它的每个next指针，以指向其下一个右侧节点，如图B所示。


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):  # 层次遍历
    if not root:
        return root
    quene = [(root, 0)]
    while len(quene) != 0:
        r, l = quene.pop(0)
        if r.left:
            quene.append((r.left, l+1))
        if r.right:
            quene.append((r.right, l+1))
        if len(quene) == 0:
            break
        if l == quene[0][1]:
            r.next = quene[0][0]
    return root


a = Node(3)
b = Node(9)
c = Node(20)
d = Node(15)
e = Node(7)
a.left = b
a.right = c
c.left = d
c.right = e
print(connect(a))
