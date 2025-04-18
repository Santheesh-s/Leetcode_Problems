class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n>=1):
            if((n&(n-1))==0):
                return True;
        return False;
