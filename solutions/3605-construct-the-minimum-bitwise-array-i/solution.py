class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def find(n):
            for i in range(n):
                if i|(i+1)==n:
                    return i
        for i in range(len(nums)):
            if(nums[i]==2):
                nums[i]=-1
                continue
            nums[i]=find(nums[i])
        return nums
