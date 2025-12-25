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
        res=ListNode()
        cur=res
        carry=0
        while(l1 and l2):
            sum_val=l1.val+l2.val+carry
            carry=sum_val//10
            cur.next=ListNode(sum_val%10)
            l1=l1.next
            l2=l2.next
            cur=cur.next
        while(l1):
            sum_val=carry+l1.val
            carry=sum_val//10
            cur.next=ListNode(sum_val%10)
            l1=l1.next
            cur=cur.next
        while(l2):
            sum_val=carry+l2.val
            carry=sum_val//10
            cur.next=ListNode(sum_val%10)
            l2=l2.next
            cur=cur.next
        if carry > 0:
            cur.next = ListNode(carry)
        return res.next

