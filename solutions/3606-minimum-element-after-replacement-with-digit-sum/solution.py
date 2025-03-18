class Solution(object):
    def minElement(self, nums):
        n=len(nums)
        for i in range(n):
            res=0
            for j in str(nums[i]):
                res+=int(j)
            nums[i]=res
        return min(nums)
