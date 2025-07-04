class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=list(str(n))
        n=list(map(int,n))
        n=sorted(n)[::-1]
        return n[0]*n[1]
        
