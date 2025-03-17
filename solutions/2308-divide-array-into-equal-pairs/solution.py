class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ls=[i for i in set(nums) if nums.count(i)%2==0]
        return set(nums)==set(ls)
