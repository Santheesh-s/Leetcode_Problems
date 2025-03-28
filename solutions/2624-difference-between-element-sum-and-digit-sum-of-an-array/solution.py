class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=sum(nums)
        s=""
        for i in nums:
            s+=str(i)
        n=0
        for i in s:
            n+=int(i)
        return abs(ls-n)
