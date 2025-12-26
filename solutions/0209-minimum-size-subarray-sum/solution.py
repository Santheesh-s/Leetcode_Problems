class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        m=2147483647
        s=0
        n=len(nums)
        left,right=0,0
        while(right<n):
            s+=nums[right];
            while(s>=target):
                m=min(m,right-left+1)
                s-=nums[left]
                left+=1
            right+=1
        return 0 if m==2147483647 else m

