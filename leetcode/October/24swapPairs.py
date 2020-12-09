# 24.
# 两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例:
# 给定
# 1->2->3->4, 你应该返回
# 2->1->4->3.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(head) -> ListNode:
        t = ListNode(-1)
        t.next = head  # 假的头结点
        pre = t
        while pre.next and pre.next.next:
            node1 = pre.next
            node2 = pre.next.next
            pre.next = node2
            node1.next = node2.next
            node2.next = node1
            pre = node1
        return t.next
            # next = cur.next
            # cur.next = pre  # 交换两个结点
            # pre.next = next  # 交换两个结点
            # pre = next
            # cur = pre.next
        #return head



        # k = head
        # while k:
        #     if k.next:
        #         a = k.next
        #     else:
        #         break
        #     k, a = a, k
        #     k = k.next.next
        # return head
