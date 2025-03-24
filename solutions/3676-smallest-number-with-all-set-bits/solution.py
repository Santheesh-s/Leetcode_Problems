class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=len(bin(n)[2:])
        return int('1'*s,2)
