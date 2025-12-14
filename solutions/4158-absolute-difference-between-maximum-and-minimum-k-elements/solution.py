class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        nums=sorted(nums)
        sum1=sum(nums[-k:])
        sum2=sum(nums[:k])
        return abs(sum2-sum1)
