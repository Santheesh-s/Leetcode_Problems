class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        z=s.count('1')
        o=s.count('0')
        return '1'*(z-1)+'0'*o+'1'
