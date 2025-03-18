class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=[i for i in set(nums) if -i in nums]
        return max(ls) if len(ls) else -1
