class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        # """
        nums.sort()
        i = 0
        n=len(nums)
        for j in range(n):
            if nums[j] > nums[i] * k:
                i += 1
        return n - (j - i + 1)
