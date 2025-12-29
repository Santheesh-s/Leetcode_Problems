class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        sum1=0
        n=len(nums)
        for i in range(n//3,n,2):
            sum1+=nums[i]
        return sum1
