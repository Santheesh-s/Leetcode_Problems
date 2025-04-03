class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b=""
        for i in bin(num)[2:]:
            if i=='0':
                b+='1'
            else:
                b+='0'
        return int(b,2)
