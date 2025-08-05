class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        while(True):
            if original not in nums:
                return original
            else:
                original*=2
