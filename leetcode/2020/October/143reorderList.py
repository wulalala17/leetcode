# 143. 重排链表
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 示例 1:
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        leng = 1
        h = head
        l1 = [h]
        while h.next:
            h = h.next
            l1.append(h)
            leng += 1
        if leng == 1:
            return head
        l2 = l1[::-1]  # 反转
        i = 0
        while i <= leng//2-1:
            l2[i].next = l1[i].next
            l1[i].next = l2[i]
            if i == leng//2-1:
                if leng % 2 == 0:
                    l2[i].next = None
                    break
                else:
                    l1[i+1].next = None
                    break
            i += 1

        return head

    # def reorderList(self, head: ListNode) -> None: 官方题解
    #     if not head:
    #         return
    #
    #     vec = list()
    #     node = head
    #     while node:
    #         vec.append(node)
    #         node = node.next
    #
    #     i, j = 0, len(vec) - 1
    #     while i < j:
    #         vec[i].next = vec[j]
    #         i += 1
    #         if i == j:
    #             break
    #         vec[j].next = vec[i]
    #         j -= 1
    #
    #     vec[i].next = None

print(7//2-1)





