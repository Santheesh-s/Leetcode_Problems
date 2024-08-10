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
        List<Integer>ls=new ArrayList<>();
        ListNode temp=head;
        while(temp!=null)
        {
            ls.add(temp.val);
            temp=temp.next;
        }
        Collections.rotate(ls,k);
        ListNode ll=new ListNode(0);
        ListNode cur=ll;
        for(int l:ls)
        {
            cur.next=new ListNode(l);
            cur=cur.next;
        }
        return ll.next;
    }
}
