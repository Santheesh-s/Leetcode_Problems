class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls=[chr(i) for i in range(97,97+26)][::-1]
        sum=0
        for i in range(len(s)):
            sum+=(ls.index(s[i])+1)*(i+1)
        return sum
