class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        steps=0
        median=nums[len(nums)//2]
        for i in nums:
            steps+=abs(i-median)
        return steps
