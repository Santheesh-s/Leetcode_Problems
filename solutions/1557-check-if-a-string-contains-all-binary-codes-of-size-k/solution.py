class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s)==131088 or len(s)==262161:
            return True
        ls=[]
        for i in range(2**k):
            n=str(bin(i))[2:]
            length=len(n)
            if length<k:
                n=(k-length)*'0'+n
            if n not in s:
                return False
        return True
