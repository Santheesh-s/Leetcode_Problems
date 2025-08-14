# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        i=0
        list3=list1
        head=0
        head2=0
        while(list1!=None):
            if i==a-1:
                head=list1
            if i==b+1:
                head2=list1
            list1=list1.next
            i+=1
        head.next=list2
        while(list2.next!=None):
            list2=list2.next
        list2.next=head2
        return list3



