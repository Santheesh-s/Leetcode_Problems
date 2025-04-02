class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[i for i in nums if i%2==0]
        b=[i for i in nums if i%2!=0]
        ls=[]
        for i,j in zip(a,b):
            ls+=[i,j]
        return ls
