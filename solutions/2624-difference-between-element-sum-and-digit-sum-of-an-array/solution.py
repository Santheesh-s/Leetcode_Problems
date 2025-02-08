class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=sum(nums)
        s=''.join(str(x) for x in nums)
        s2=(list(s))
        sum2=sum(int(x) for x in s2)
        print(sum2)
        return abs(sum1-sum2)
        
