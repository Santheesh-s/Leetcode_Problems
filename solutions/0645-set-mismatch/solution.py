class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls=[]
        n=sum(list(set(nums)))
        ls.append(sum(nums)-n)
        x=(len(nums)*(len(nums)+1))/2
        ls.append(x-n)
        return ls

