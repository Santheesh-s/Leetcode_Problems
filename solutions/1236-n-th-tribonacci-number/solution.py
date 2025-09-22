class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        c=1
        f=0;
        if(n==0):
            return 0;
        for i in range(n):
            f=a+b+c;
            a=b;
            b=c;
            c=f;
        return a;
        
