class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i] in t:
                t=t.replace(s[i],'',1)
        return len(t)
