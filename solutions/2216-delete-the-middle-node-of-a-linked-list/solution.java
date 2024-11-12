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
    public ListNode deleteMiddle(ListNode head) {
        if(head==null || head.next==null)
            return null;
        ListNode temp=head;
        int len=1,i=1,k;
        while(temp!=null)
        {
            len++;
            temp=temp.next;
        }
        if(len%2!=0)
            k=len/2+1;
        else
            k=len/2;
        temp=head;
        while(i<k-1)
        {
            temp=temp.next;
            i++;
        }
        temp.next=temp.next.next;
        return head;
    }
}
