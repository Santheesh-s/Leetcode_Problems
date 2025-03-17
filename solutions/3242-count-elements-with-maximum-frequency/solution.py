class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=max([nums.count(i) for i in nums])
        ls1=len([i for i in nums if nums.count(i)==ls])
        return ls1
