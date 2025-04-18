class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count=n&1;
        n>>=1;
        while(n>0):
            if((n&1)==count):
                return False;
            count=(n&1);
            n>>=1;
        return True;   
