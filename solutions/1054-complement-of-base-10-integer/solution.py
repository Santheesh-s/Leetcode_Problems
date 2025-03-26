class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=""
        for i in bin(n)[2:]:
            if i=='0':
                s+='1'
            else:
                s+='0'
        return int(s,2)
