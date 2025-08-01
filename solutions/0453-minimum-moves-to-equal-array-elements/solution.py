class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minElement = min(nums)
        targetSum = len(nums) * minElement
        totalSum = sum(nums)
        return totalSum-targetSum
