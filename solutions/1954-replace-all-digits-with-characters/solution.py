class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss=""
        l=len(s)
        ls=[chr(i) for i in range(97,97+26)]
        for i in range(1,l,2):
            ss+=s[i-1]
            n=ls.index(s[i-1])
            ss+=ls[n+int(s[i])]
        return ss if l%2==0 else ss+s[-1]
