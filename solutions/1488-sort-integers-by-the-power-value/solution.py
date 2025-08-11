class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        def c(n):
            if n==1: return 0
            elif n&1: return c(3*n+1)+1
            else: return c(n/2)+1
        ls=[]
        for i in range(lo,hi+1): ls.append( (c(i),i) )
        ls=sorted(ls)
        return ls[k-1][1]
