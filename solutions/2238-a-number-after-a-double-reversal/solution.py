class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s=int(str(num)[::-1])
        if len(str(s))==len(str(num)):
            return True
        return False
