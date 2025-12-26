# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp=head;
        temp1=head;
        while(n>0):
            n-=1
            temp=temp.next;
        if(not temp):
            return head.next
        while(temp.next):
            temp=temp.next
            temp1=temp1.next
        if(temp1.next):
            temp1.next=temp1.next.next
        return head;
