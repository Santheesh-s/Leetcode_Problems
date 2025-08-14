# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1=head
        ls=0
        while(head1!=None):
            ls=ls*10+head1.val
            head1=head1.next
        ls=ls*2
        s=str(ls)
        n=len(s)
        head2=ListNode(int(s[0]))
        head=head2
        i=1
        while(n!=1):
            n-=1
            head2.next=ListNode(int(s[i]))
            head2=head2.next
            i+=1
        return head
