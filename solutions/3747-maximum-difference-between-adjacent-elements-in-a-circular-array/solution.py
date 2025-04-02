class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=0
        for i in range(len(nums)-1):
            n=abs(nums[i]-nums[i+1])
            if n>ls:
                ls=n
        n=abs(nums[0]-nums[-1])
        return n if n>ls else ls
