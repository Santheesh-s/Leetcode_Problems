class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=s[:len(s)/2]
        b=s[len(s)/2:]
        a1=0
        b1=0
        c="aeiouAEIOU"
        for i in c:
            a1+=a.count(i)
        for i in c:
            b1+=b.count(i)
        return a1==b1
