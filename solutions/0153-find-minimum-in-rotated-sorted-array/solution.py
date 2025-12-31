class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,len(nums)-1
        if nums[l]<nums[r]: return nums[l];
        m=nums[0]
        while(l<=r):
            m=min(m,nums[l],nums[r])
            l+=1
            r-=1
        return m
