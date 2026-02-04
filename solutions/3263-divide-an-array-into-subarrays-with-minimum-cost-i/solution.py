class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=sorted(nums[1:])
        return nums[0]+a[0]+a[1]

