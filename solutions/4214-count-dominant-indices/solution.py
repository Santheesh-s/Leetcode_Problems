class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=1:
            return 0
        count=0;
        suff=nums[-1]
        ele=1
        for i in range(n-2,-1,-1):
            if nums[i]*ele>suff:
                count+=1
            suff+=nums[i]
            ele+=1
        return count
