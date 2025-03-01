class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s=="".join(sorted(s))
        
