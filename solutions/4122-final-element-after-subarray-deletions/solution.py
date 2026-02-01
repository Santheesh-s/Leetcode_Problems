class Solution(object):
    def finalElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max1=nums.index(max(nums))
        # n=len(nums)
        # if max1==0 or max1==n-1:
        #     return nums[max1]
        # return nums[n-1]
        return max(nums[0],nums[-1])
