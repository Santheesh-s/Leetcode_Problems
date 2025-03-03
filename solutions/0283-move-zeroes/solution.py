class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=[i for i in nums if i!=0]
        n=n+[0]*(len(nums)-len(n))
        for i in range(0,len(nums)):
            nums[i]=n[i]
