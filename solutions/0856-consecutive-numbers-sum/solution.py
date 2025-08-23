class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        count,i=0,1;
        while(n>0):
            n=n-i;
            if(n%i==0):
                count+=1;
            i+=1;
        return count;
