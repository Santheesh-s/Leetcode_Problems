class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1=0
        sum2=0;
        for i in nums:
            if(i>9): sum1+=i;
            else: sum2+=i;
        if(sum1>sum2 or sum2>sum1): return True;
        return False;
