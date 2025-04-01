class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls=[]
        for i in range(1,len(nums)+1):
            ls.append(len(set(nums[:i]))-len(set(nums[i:])))
        return ls
            
