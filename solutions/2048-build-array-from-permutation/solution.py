class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1=[0]*len(nums)
        for i in range(len(nums)):
            nums1[i]=nums[nums[i]]
        return nums1
