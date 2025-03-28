class Solution(object):
    def sumOfSquares(self, nums):
        a=len(nums)
        s=0
        for i in range(1,a+1):
            if a%i==0:
                s+=nums[i-1]**2
        return s
