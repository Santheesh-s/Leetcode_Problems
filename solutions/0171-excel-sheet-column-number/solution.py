class Solution(object):
    def titleToNumber(self, c):
        """
        :type columnTitle: str
        :rtype: int
        """
        result=0
        for i in c:
            result = result * 26 + (ord(i) - 64)
        return result
