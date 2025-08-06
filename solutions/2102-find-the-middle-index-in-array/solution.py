class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=sum(nums)
        right=0
        for i in range(len(nums)):
            left-=nums[i]
            if left==right:
                return i
            right+=nums[i]
        return -1
