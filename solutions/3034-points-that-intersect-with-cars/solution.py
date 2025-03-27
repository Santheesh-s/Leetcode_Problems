class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        ls=[i for i in range(102)]
        s=set()
        for i in nums:
            s.update([ls[i] for i in range(i[0],i[1]+1)])
        return len(s)
