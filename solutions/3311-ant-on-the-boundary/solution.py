class Solution(object):
    def returnToBoundaryCount(self, nums):
        ls,n=0,0
        for i in range(len(nums)):
            n+=nums[i]
            if n==0:
                ls+=1
        return ls

