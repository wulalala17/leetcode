/*61. 旋转链表
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

示例 2：
输入：head = [0,1,2], k = 4
输出：[2,0,1]

提示：
    链表中节点的数目在范围 [0, 500] 内
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109*/

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
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || k == 0)
            return head;
        int lengthOfNode = 0;
        ListNode h = head;
        ListNode h1 = head;
        ListNode dummy = new ListNode(-1, head);
        ListNode pre = dummy;//前置结点
        ListNode h2 = new ListNode();
        while(h != null){//计算总长度
            lengthOfNode++;
            h = h.next;
        }
        k = k % lengthOfNode;
        if (k == 0)
            return head;
        int times = lengthOfNode - k;
        while(times > 0){
            pre = pre.next;
            h1 = h1.next;
            times--;
            if (times == 0){
                pre.next = null;
                h2 = h1;//新的头结点
                while(h1.next != null){//找到尾部
                    h1 = h1.next;
                }
                h1.next = head;
            }
        }
        return h2;
    }
}