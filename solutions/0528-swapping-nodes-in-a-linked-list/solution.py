# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        h,h1=head,head
        l,n,a=1,1,0
        while(h!=None):
            if l==k:
                a=h
            l+=1
            h=h.next
        while(h1!=None):
            if l-k==n:
                break
            n+=1
            h1=h1.next
        a.val,h1.val=h1.val,a.val
        return head
