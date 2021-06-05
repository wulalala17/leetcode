/*
203. 移除链表元素
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。



示例 1：

输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：

输入：head = [], val = 1
输出：[]

示例 3：

输入：head = [7,7,7,7], val = 7
输出：[]



提示：

    列表中的节点在范围 [0, 104] 内
    1 <= Node.val <= 50
    0 <= k <= 50
*/
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
    public ListNode removeElements(ListNode head, int val) {
        if(head == null)
            return head;
        ListNode newHead = new ListNode(-1);
        ListNode h = head;
        ListNode cur = newHead;
        while(h != null){
            while (h != null && h.val == val){
                h = h.next;
            }
            if(h == null){
                cur.next = h;
                return newHead.next;
            }
            else{
                cur.next = h;
                cur = cur.next;
                h = h.next;
            }
        }
        return newHead.next;
    }
}