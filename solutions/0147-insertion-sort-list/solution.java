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
    public ListNode insertionSortList(ListNode head) {
        List<Integer>ls=new ArrayList<>();
        ListNode h=head;
        ListNode h1=head;
        while(h!=null){
            ls.add(h.val);
            h=h.next;
        }
        int k=0;
        Collections.sort(ls);
        while(h1!=null){
            h1.val=ls.get(k);
            h1=h1.next;
            k+=1;
        }
        return head;
    }
}
