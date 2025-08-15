# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        ls=[]
        while(head!=None):
            ls.append(head.val)
            head=head.next
        ls1=[]
        n=len(ls)
        for i in range(0,n-(n%k),k):
            ls1+=ls[i:i+k][::-1]
        ls1+=ls[n-(n%k):]
        res=ListNode(ls1[0])
        head=res
        n=n-1
        i=1
        while(n):
            res.next=ListNode(ls1[i])
            res=res.next
            i+=1
            n-=1
        return head
