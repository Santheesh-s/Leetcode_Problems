class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ls=[]
        for i in range(n):
            ls.append(nums[i])
            ls.append(nums[i+n])
        return ls
