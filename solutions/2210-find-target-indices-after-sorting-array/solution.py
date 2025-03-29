class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=sorted(nums)
        return [i for i in range(len(nums)) if n[i]==target]
