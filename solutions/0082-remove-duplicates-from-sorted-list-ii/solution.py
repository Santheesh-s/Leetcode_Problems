# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        h,h1=head,head
        s=[]
        while(h!=None):
            s.append(h.val)
            h=h.next
        ls=[i for i in s if s.count(i)==1]
        if not len(ls):
            return None 
        for i in range(len(ls)):
            h1.val=ls[i]
            if i+1==len(ls):
                h1.next=None
            else:
                h1=h1.next
        return head
