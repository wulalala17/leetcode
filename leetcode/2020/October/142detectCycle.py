# 142.环形链表II
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回null。
# 为了表示给定链表中的环，我们使用整数pos来表示链表尾连接到链表中的位置（索引从0开始）。 如果pos是 - 1，则在该链表中没有环。
# 说明：不允许修改给定的链表。
# 示例
# 1：
# 输入：head = [3, 2, 0, -4], pos = 1
# 输出：tail connects to node index1
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 示例
# 2：
# 输入：head = [1, 2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 示例
# 3：
# 输入：head = [1], pos = -1
# 输出：no
# cycle
# 解释：链表中没有环。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head):
    p = head
    q = head
    while p and q:
        p = p.next
        q = q.next.next
        if p == q:
            return True
    return False
# class Solution(object):  真正的双指针法
#     def detectCycle(self, head):
#         fast, slow = head, head
#         while True:
#             if not (fast and fast.next): return
#             fast, slow = fast.next.next, slow.next
#             if fast == slow: break
#         fast = head
#         while fast != slow:
#             fast, slow = fast.next, slow.next
#         return fast
#
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。