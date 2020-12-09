# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    if l1 == None or l2 ==None:
        return l1 or l2
    res = []
    remainder = 0
    while l1 and l2:
        sum0 = l1.val + l2.val + remainder
        res.append(sum0 % 10)
        remainder = sum0 // 10
        l1 = l1.next
        l2 = l2.next
    if l1:
        while l1:
            sum0 = l1.val + remainder
            res.append(sum0 % 10)
            remainder = sum0 // 10
            l1 = l1.next
    if l2:
        while l2:
            sum0 = l2.val + remainder
            res.append(sum0 % 10)
            remainder = sum0 // 10
            l2 = l2.next

    if remainder>0:
        res.append(remainder)
    r = ListNode(res[0])
    p = r
    for i in range(1, len(res)): # 数组转换成链表
        # print('res:', res[i])
        p.next = ListNode(res[i])
        p = p.next
        # r.next = ListNode(res[i])
    while r:
        print('结果：', r.val)
        r = r.next
    return r

a=ListNode(2)
b=ListNode(4)
c=ListNode(3)
d=ListNode(5)
e=ListNode(6)
f=ListNode(4)
a.next = b
b.next = c
d.next = e
e.next = f
print(addTwoNumbers(a, d))

# class Solution:  别人的写法
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         re = ListNode(0)
#         r=re
#         carry=0
#         while(l1 or l2):
#             x= l1.val if l1 else 0
#             y= l2.val if l2 else 0
#             s=carry+x+y
#             carry=s//10
#             r.next=ListNode(s%10)
#             r=r.next
#             if(l1!=None):l1=l1.next
#             if(l2!=None):l2=l2.next
#         if(carry>0):
#             r.next=ListNode(1)
#         return re.next



