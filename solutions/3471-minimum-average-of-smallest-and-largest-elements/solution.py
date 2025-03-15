class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        ls=[]
        while(len(nums)):
            if len(nums):
                ls.append(float(max(nums)+min(nums))/2)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return min(ls)
