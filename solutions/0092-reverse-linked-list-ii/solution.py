# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        h=head;
        l,a,h1,k=[],0,head,-1
        while(h!=None):
            a+=1;
            if a>=left and a<=right:
                l.append(h.val);
            h=h.next;
        a=0
        while(h1!=None):
            a+=1
            if a>=left and a<=right:
                h1.val=l[k]
                k-=1;
            
            h1=h1.next;
        return head;
