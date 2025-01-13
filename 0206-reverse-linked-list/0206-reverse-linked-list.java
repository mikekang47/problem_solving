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
import java.util.*;

class Solution {
    public ListNode reverseList(ListNode head) {
        Stack<ListNode> st = new Stack<>();
        if (head == null) {
            return null;
        }
        while(head != null) {
            st.push(head);
            head = head.next;
        }
        ListNode temp = new ListNode();
        ListNode curr = temp;
        while(!st.isEmpty()) {
            ListNode top = st.pop();
            top.next = null;
            curr.next = top;
            curr = curr.next;
        }
        return temp.next;
    }
}