class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls=[i for i in nums if i>0]
        ls1=[i for i in nums if i<0]
        ls2=[]
        n=len(ls)
        for i in range(n):
            ls2.append(ls[i])
            ls2.append(ls1[i])
        return ls2
