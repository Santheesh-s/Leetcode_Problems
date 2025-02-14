class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ls=list(s.upper())
        sum1=0
        ls2=map(lambda x: str(ord(x)-64), ls)
        ls2=map(int,list("".join(ls2)))
        for i in range(0,k):
            sum1=sum(ls2)
            ls2=map(int,list(str(sum1)))
        return sum1
