/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    /*
    // solution 1
    // cur2 starts at head.next
    public ListNode swapPairs(ListNode head) {
        ListNode cur1, cur2, dummy, prev;
        if (head == null || head.next == null) return head;
        cur1 = head;
        cur2 = head.next;
        dummy = new ListNode(-1);
        dummy.next = cur1;
        prev = dummy;
        while(cur2 !=null && cur2.next != null) {
            System.out.println("@ " + prev.next.val + prev.next.next.val); 
            System.out.println("- " + cur1.val + cur2.val);           
            ListNode tmp = cur2.next;
            prev.next = cur2;
            cur2.next = cur1;
            cur1.next = tmp;
            System.out.println("- " + prev.next.val + prev.next.next.val); 
            prev = cur1;
            
            // next pair
            cur1 = tmp;
            cur2 = cur1.next;
            System.out.println("next");
            System.out.print(" " + cur1.val);
            if (cur2 != null) System.out.println("" + cur2.val);
        }
        
        if (cur1 != null) {
            if (cur2 == null) {
                prev.next = cur1;
            } else {
                prev.next = cur2;
                cur2.next = cur1;
                cur1.next = null;
                System.out.println(" " + cur2.val + cur1.val);
            }
                
        }

        return dummy.next;
    }
    */
    
    // solution 2, clean loop with one more pointer & dummy
    // cur2 starts at Head, so it goes cur2, cur1 : cur2 is the start of the next pair
    // but cur1, cur2 sequence for each loop's initial assignment
    // tangled
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode cur1, cur2, dummy, prev1, prev2;
        
        cur2 = head;
        dummy = new ListNode(-1);
        dummy.next = cur2;
        prev1 = dummy;
        prev2 = dummy.next;
        
        while (prev2 !=null && prev2.next != null) {  
            
            cur1 = cur2.next;
            cur2 = cur2.next.next;
            
            prev1.next = cur1;
            cur1.next = prev2;
            prev2.next = cur2;
            
            prev1 = prev2;
            prev2 = cur2;
        }

        return dummy.next;
    }
}
