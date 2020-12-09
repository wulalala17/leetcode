# 328. 奇偶链表
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
# 示例 1:
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 示例 2:
# 输入: 2->1->3->5->6->4->7->NULL
2315647
2361547
# 输出: 2->3->6->7->1->5->4->NULL
# 说明:
#     应当保持奇数节点和偶数节点的相对顺序。
#     链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution: 正确的不用额外空间的版本
#    def oddEvenList(self, head: ListNode) -> ListNode:
#        if head == None: return head
#        point1, point2 = head, head.next
#        p1, p2 = point1, point2
#        while p2 != None and p2.next:
#            p1.next = p1.next.next
#            p2.next = p2.next.next
#            p1 = p1.next
#            p2 = p2.next
#        p1.next = point2
#        return point1
def oddEvenList(head):
    def insert(p, pre, cur):  # cur插入p后面，pre是cur前面的结点 pre->cur
        if not cur:
            return
        ne = p.next
        pre.next = cur.next
        p.next = cur
        cur.next = ne
    def traversalNode(node):
        while node:
            print(node.val, end='->')
            node = node.next


    p = head
    pre = head.next
    cur = head.next.next
    stack = []
    while pre:
        stack.append([pre, pre.next])
        pre = pre.next.next

    while stack:
        print('当前链表情况：')
        traversalNode(head)
        s = stack.pop(0)
        insert(p, s[0], s[1])
        p = p.next
    return p
a = ListNode(2)
b = ListNode(1)
c = ListNode(3)
d = ListNode(5)
e = ListNode(6)
f = ListNode(4)
g = ListNode(7)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
print(oddEvenList(a))



