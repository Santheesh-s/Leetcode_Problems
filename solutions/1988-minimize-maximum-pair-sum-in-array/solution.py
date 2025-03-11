class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        m=len(nums)
        nums=sorted(nums)
        for i in range(m/2):
            if nums[i]+nums[m-i-1]>c:
                c=nums[i]+nums[m-i-1]
        return c
