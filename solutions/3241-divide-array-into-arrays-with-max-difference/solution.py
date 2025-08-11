class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        ls=[]
        for i in range(0,len(nums),3):
            if nums[i+2]-nums[i]>k:
                return []
            ls.append(nums[i:i+3])
        return ls
