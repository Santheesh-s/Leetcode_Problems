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
    public ListNode middleNode(ListNode head) {
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
        while(i<k)
        {
            temp=temp.next;
            i++;
        }
        return temp;
    }
}
