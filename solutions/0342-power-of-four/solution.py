class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==1):
            return True;
        count=0;
        if(n>0 and (n&(n-1))==0):
            while(n>0):
                if((n&1)==0):
                    count+=1;
                n>>=1;
        if(count!=0 and (count&1)==0):
            return True;
        return False;
        
