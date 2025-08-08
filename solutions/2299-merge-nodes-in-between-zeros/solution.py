# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1=temp=ListNode(0)
        sum1=0
        while(head!=None):
            if head.val==0:
                head=head.next
                temp.next=ListNode(sum1)
                sum1=0
                temp=temp.next
            else:
                sum1+=head.val
                head=head.next
        return head1.next.next
