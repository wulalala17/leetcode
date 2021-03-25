/*82. 删除排序链表中的重复元素 II

存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
返回同样按升序排列的结果链表。

示例 1：
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

示例 2：
输入：head = [1,1,1,2,3]
输出：[2,3]

提示：

    链表中节点数目在范围 [0, 300] 内
    -100 <= Node.val <= 100
    题目数据保证链表已经按升序排列

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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null)//空节点退出
            return head;
        ListNode dummy = new ListNode(-1, head);
        ListNode pre = dummy;
        ListNode cur = head;
        ListNode ne = cur.next;
        if (ne == null)//只有一个结点
            return head;
        int v = cur.val;
        int flag = 0;
        /*if (ne.next == null){//只有两个结点
            if (cur.val == ne.val)
                return null;
            else return head;
        }*/
        while(ne != null){
            v = cur.val;
            flag = 0;
            while(ne != null && ne.val == v){
                flag = 1;//说明有重复的
                ne = ne.next;
            }
            if(flag == 1){
                pre.next = ne;//有重复的直接跳过cur
                cur = ne;
                if(ne == null)
                    break;
                ne = ne.next;
            }
            else{//无重复则往后走
                pre = cur;
                cur = ne;
                ne = ne.next;
            }
        }
        return dummy.next;

    }
}

class Solution { //官方题解，有点绕
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }

        ListNode dummy = new ListNode(0, head);

        ListNode cur = dummy;
        while (cur.next != null && cur.next.next != null) {
            if (cur.next.val == cur.next.next.val) {
                int x = cur.next.val;
                while (cur.next != null && cur.next.val == x) {
                    cur.next = cur.next.next;
                }
            } else {
                cur = cur.next;
            }
        }

        return dummy.next;
    }
}

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/solution/shan-chu-pai-xu-lian-biao-zhong-de-zhong-oayn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。