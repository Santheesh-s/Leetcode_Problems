class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        j=nums.index(m)
        for i in range(0,len(nums)):
            if nums[i]!=m: nums[i]*=2   
        if m==max(nums): return j
        else: return -1
            
