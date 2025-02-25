class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=filter(lambda x:x%3==0 and x%2==0,nums)
        if sum(nums)==0: return 0
        return sum(nums)/len(nums)
