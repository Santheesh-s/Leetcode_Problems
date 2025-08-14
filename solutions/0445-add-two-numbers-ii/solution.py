# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n,n1=0,0
        while(l1!=None):
            n=n*10+l1.val
            l1=l1.next
        while(l2!=None):
            n1=n1*10+l2.val
            l2=l2.next
        s=str(n+n1)
        n=len(s)
        i=1
        n2=ListNode(int(s[0]))
        res=n2
        while(n!=1):
            n2.next=ListNode(int(s[i]))
            n2=n2.next
            i+=1
            n-=1
        return res
        
