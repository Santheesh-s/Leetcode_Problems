class Solution(object):
    def maximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<2:
            return 0
        prefix=[0]*n
        suffix=[0]*n
        suffix[n-1]=nums[n-1]
        prefix[0]=nums[0]

        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]
        for i in range(n-2,-1,-1):
            suffix[i]=min(suffix[i+1],nums[i])

        max_val=float('-inf')
        for i in range(n-1):
            cur=prefix[i]-suffix[i+1]
            if(cur>max_val):
                max_val=cur;
        return max_val
