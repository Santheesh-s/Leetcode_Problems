class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=0
        max1=nums[0];
        for i in range(len(nums)):
            if(sum1<0):
                sum1=0;
            sum1+=nums[i];
            if(max1<sum1):
                max1=sum1;
        return max1;
