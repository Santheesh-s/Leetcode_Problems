class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if bin(nums[i]|nums[j])[-1]=='0':
                    return True
        return False
