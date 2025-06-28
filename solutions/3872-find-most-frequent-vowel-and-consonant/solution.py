class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=0
        b=0
        for i in s:
            if i in "aeiou":
                a=max(a,s.count(i))
            else:
                b=max(b,s.count(i))
        return a+b
