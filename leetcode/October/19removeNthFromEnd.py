# 19. 删除链表的倒数第N个节点
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
# 给定的 n 保证是有效的。
# 进阶：
# 你能尝试使用一趟扫描实现吗？
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head.next:
            return None
        # if not head.next.next:
        #     if n == 1:
        #         head.next = None
        #         return head
        #     if n == 2:
        #         return head.next
        h1 = head
        h2 = head
        k = 1
        while k!=n: # 走到倒数第n个结点
            h1 = h1.next
            k += 1
        if not h1.next:  # 说明要删除正数第一个结点
            return head.next
        while h1.next:
            pre = h2
            h2 = h2.next
            h1 = h1.next
        pre.next = h2.next
        return head


# class Solution: 递归写法 不明觉厉
#     def removeNthFromEnd(self, head, n):
#         global i
#         if head is None:
#             i=0
#             return None
#         head.next = self.removeNthFromEnd(head.next,n)
#         i+=1
#         return head.next if i==n else head
#
# 作者：adamch0u
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/python-di-gui-by-adamch0u/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。