class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        i = 0

        while i+1 < n and nums[i] < nums[i+1]:
            i += 1
        p = i

        while i+1 < n and nums[i] > nums[i+1]:
            i += 1
        q = i

        while i+1 < n and nums[i] < nums[i+1]:
            i += 1
        flag = i 

        return p != 0 and q != p and flag == n - 1 and flag != q
