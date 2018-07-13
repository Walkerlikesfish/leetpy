/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param head: n
     * @return: The new head of reversed linked list.
     */
    public ListNode reverse(ListNode head) {
        if (head == null) return null;
        ListNode dummyHead = new ListNode(0);
        
        ListNode end = new ListNode(head.val);
        dummyHead.next = end;
       
/* 
        ListNode cur = head;
        ListNode curNew = end;
        while (cur != null && cur.next != null) {
            cur = cur.next;
            curNew = dummyHead.next;
            dummyHead.next = new ListNode(cur.val);
            dummyHead.next.next = curNew;
        }
*/

        ListNode cur = head.next;
        ListNode curNew = end;
        while (cur != null) {
            curNew = dummyHead.next;
            dummyHead.next = new ListNode(cur.val);
            dummyHead.next.next = curNew;
            cur = cur.next;
        }
        return dummyHead.next;
    }
}
