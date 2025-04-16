class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<9:
            return num
        return 9 if num%9==0 else num%9
