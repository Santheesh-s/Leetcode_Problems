class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=[]
        for i in set(nums):
            n=nums.count(i)
            if n>=2:
                for j in range(2,n):
                    nums.remove(i)
        return len(nums)

