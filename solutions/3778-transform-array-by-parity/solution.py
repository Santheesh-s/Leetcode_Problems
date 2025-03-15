class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=0
        for i in nums:
            if i%2!=0:
                c+=1
        return [0]*(len(nums)-c)+[1]*c
