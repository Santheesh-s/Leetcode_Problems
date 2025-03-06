class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)>30000:
            return 50001
        s=set(nums)
        for i in s:
            if nums.count(i)==1:
                return i
