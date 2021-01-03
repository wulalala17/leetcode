# 86.分隔链表
#
# 给你一个链表和一个特定值x ，请你对链表进行分隔，使得所有小于x的节点都出现在大于或等于x的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。
# 示例：
# 输入：head = 1->4->3->2->5->2, x = 3
# 输出：1->2->2->4->3->5


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    if not head:  # 只会用数组写，用链表写半天还是错的
        return
    li = []
    k = 0
    while head:
        if head.val >= x:
            li.append(head.val)
        else:
            li.insert(k, head.val)
            k += 1
        head = head.next
    h = ListNode(li[0])
    h0 = h
    for i in range(1, len(li)):
        k = ListNode(li[i])
        h.next = k
        h = h.next
    return h0


    # if not head:
    #     return
    # h0 = head
    # h1 = head.next
    # pre = head
    # while h1:
    #     if h1.val < x:
    #         if pre == h0:
    #             h1 = h1.next
    #             continue
    #         pre.next = h1.next
    #         h1.next = h0.next
    #         h0.next = h1
    #         h0 = h0.next
    #         h1 = pre.next
    #     else:
    #         pre = pre.next
    #         h1 = h1.next
    # return head

h = ListNode(1)
h1 = ListNode(1)
h.next = h1
print(partition(h, 2))

# class Solution(object):  # 我怎么就想不到要用两个新链表
#     def partition(self, head, x):
#         """
#         :type head: ListNode
#         :type x: int
#         :rtype: ListNode
#         """
#         if not head:
#             return head
#         small=ListNode(-1)
#         big=ListNode(-1)
#         pre1=small
#         pre2=big
#         while head:
#             if head.val<x:
#                 small.next=head
#                 small=small.next
#             else:
#                 big.next=head
#                 big=big.next
#             head=head.next
#         small.next=pre2.next
#         big.next=None
#         return pre1.next




