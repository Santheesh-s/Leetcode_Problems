class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num<0:
            mask = (1 << 32) - 1
            num=(abs(num) ^ mask) + 1
        return str(hex(num))[2:]
