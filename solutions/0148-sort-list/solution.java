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
    public ListNode sortList(ListNode head) {
        List<Integer>ls=new ArrayList<>();
        ListNode temp=head;
        while(temp!=null)
        {
            ls.add(temp.val);
            temp=temp.next;
        }
        Collections.sort(ls);
        ListNode dummy=new ListNode(-1);
        ListNode cur=dummy;
        for(int n:ls)
        {
            cur.next=new ListNode(n);
            cur=cur.next;
        }
        return dummy.next;
    }
}
