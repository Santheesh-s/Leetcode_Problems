class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count=0
        for i in s:
            if i in 'aeiou':
                return True
        return False
