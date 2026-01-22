class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n=len(s)
        j=0
        for i in t:
            if j<n:
                if i==s[j]:
                    j+=1
        return True if j==n else False


