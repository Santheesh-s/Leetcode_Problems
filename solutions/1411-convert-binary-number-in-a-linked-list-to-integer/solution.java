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
    public int getDecimalValue(ListNode head) {
        StringBuilder s = new StringBuilder(); // Initialize StringBuilder
        ListNode temp = head;
        
        // Traverse the linked list and build the binary string
        while (temp != null) {
            s.append(temp.val); // Append the current node's value
            temp = temp.next;  // Move to the next node
        }
        
        // Convert the binary string to a decimal integer
        return Integer.parseInt(s.toString(), 2);
    }
}
