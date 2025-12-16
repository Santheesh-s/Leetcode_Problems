class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=bin(n)
        ma=0
        ls=[]
        for i in range(len(a)):
            if a[i]=='1':
                ls.append(i)
        for i in range(1,len(ls)):
            ma=max(ma,abs(ls[i]-ls[i-1]))
        return ma
