class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        n=0;
        for i in range(1,b+1):
            if(a%i==0 and b%i==0):
                n+=1;
        return n;
