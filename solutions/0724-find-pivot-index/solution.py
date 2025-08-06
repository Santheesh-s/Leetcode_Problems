class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=sum(nums)
        l=sum1
        r=0
        for i in range(len(nums)):
            l-=nums[i]
            if l==r:
                return i
            r+=nums[i]
        return -1
