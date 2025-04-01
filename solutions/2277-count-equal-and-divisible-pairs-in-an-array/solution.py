class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c,n=0,len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    if (i*j)%k==0:
                        c+=1
        return c
