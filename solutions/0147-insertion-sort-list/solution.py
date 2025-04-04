# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ls=[]
        h=head
        h1=head
        while(h!=None):
            ls.append(h.val)
            h=h.next
        k=0
        ls.sort()
        while(h1!=None):
            h1.val=ls[k]
            h1=h1.next
            k+=1
        return head
