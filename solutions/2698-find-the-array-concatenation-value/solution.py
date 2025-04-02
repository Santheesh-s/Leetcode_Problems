class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        for i in range(len(nums)//2):
            s+=int(str(nums[i])+str(nums[-(i+1)]))
        if len(nums)%2!=0:
            s+=nums[len(nums)//2]
        return s
