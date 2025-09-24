class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums=sorted(set(nums))
        if(len(nums)<k):
            return nums[::-1]
        else:
            return nums[-k:][::-1]
