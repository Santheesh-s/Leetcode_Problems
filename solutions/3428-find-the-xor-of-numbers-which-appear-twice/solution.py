class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=[i for i in set(nums) if nums.count(i)>1]
        l=0
        if len(ls)==0:
            return 0
        elif len(ls)==1:
            return ls[0]
        else:
            for i in ls:
                l^=i
        return l

