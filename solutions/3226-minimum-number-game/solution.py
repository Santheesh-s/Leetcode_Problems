class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=sorted(nums)
        ls=[]
        n=len(nums)
        for i in range(0,n,2):
            ls.append(nums[i+1])
            ls.append(nums[i])
        return ls
