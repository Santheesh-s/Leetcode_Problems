class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        while(n>0):
            n=n-i
            i+=1
        if(n==0):
            return i-1
        else:
            return i-2
        
