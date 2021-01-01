# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



def connect(root):
    def shit(front, node):
        if front:
            front.next = node

        if node.left:
            if front and front.right:
                shit(front.right, node.left)
            if not front:
                shit(None, node.left)
        if node.right:
            shit(node.left, node.right)
        return
    return shit(None, root)


# def connect(root):  别人写的 好强
#     if not root or not root.left:
#         return
#     root.left.next = root.right
#     if root.next:
#         root.right.next = root.next.left
#     connect(root.left)
#     connect(root.right)


# stack = [root] 非递归
# while stack:
#     size = len(stack)
#     for i in range(size):
#         s = stack.pop(0)
#         if i < size-1:
#             s.next = stack[0]
#         if s.left:
#             stack.append(s.left)
#         if s.right:
#             stack.append(s.right)
#     return root




