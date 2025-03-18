class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                m+=i
        return m
