class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls=[]
        for i in nums:
            count=0
            for j in nums:
                if i>j:
                    count+=1
            ls.append(count)
        return ls
