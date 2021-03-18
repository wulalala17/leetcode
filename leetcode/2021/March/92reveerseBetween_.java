/*92. 反转链表 II

反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution { // 好烦链表的操作啊
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0, head);
        ListNode l = dummy;
        for(int i = 1;i < left; i++)
            l = l.next;//left的前驱节点
        ListNode pre = new ListNode(-1);
        ListNode cur = l.next;
        for(int i = left;i <= right; i++){
            ListNode nex = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nex;
        }//1 2 null
        l.next.next = cur;//1 2 5
        l.next = pre;//1 4 3 2 5
        return dummy.next;


    }
}