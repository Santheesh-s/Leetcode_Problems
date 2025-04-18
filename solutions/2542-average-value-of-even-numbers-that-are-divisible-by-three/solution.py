class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        n=0
        for i in nums:
            if i%6==0:
                count+=i
                n+=1;
        if(n>0):
            return count//n
        return 0
