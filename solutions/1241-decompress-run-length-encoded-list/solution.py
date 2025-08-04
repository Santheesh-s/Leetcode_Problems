class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls=[]
        for i in range(0,len(nums),2):
            ls+=[nums[i+1]]*nums[i]
        return ls
