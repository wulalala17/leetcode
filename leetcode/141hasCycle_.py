# 141.环形链表
# 给定一个链表，判断链表中是否有环。如果链表中有某个节点，可以通过连续跟踪next指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数pos
# 来表示链表尾连接到链表中的位置（索引从0开始）。 如果pos是 - 1，则在该链表中没有环。注意：pos不作为参数进行传递，仅仅是为了标识链表的实际情况。如果链表中存在环，则返回true 。 否则，返回
# false 。
# 进阶：
# 你能用O(1)（即，常量）内存解决此问题吗？
#
# 示例
# 1：
# 输入：head = [3, 2, 0, -4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 示例
# 2：
# 输入：head = [1, 2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 示例
# 3：
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
# 提示：
# 链表中节点的数目范围是[0, 104]
# -105 <= Node.val <= 105pos为 - 1或者链表中的一个有效索引。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head): # 为什么想不到
    while head:
        if head.val == 'visit':
            return True
        else:
            head.val = 'visit'
        head = head.next
    return False

