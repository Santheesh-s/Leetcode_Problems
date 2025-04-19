class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0;
        for i in nums:
            count^=i
        return count;
        
