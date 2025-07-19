class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        adder=0;
        for i in range(len(nums)):
            adder+=nums[i];
            nums[i]=adder;
        return nums;
