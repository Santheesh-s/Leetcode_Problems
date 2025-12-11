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
    public int numComponents(ListNode head, int[] nums) {
        Map<Integer,Integer>map=new HashMap<>();
        for(int a:nums)
            map.put(a,1);
        int count=0;
        while(head.next!=null)
        {
            if(map.containsKey(head.val))
                count+=(map.containsKey(head.next.val)?1:0);
            head=head.next;
        }
        return count+nums.length-2*count;
    }
}
