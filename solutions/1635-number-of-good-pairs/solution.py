class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        count=0
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    count+=1
        return count
