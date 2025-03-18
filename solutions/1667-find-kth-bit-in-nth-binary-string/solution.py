class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k==1:
            return '0'
        if k==2 or k==3 or k==4:
            return '1'
        def ss(s):
            ss=""
            for i in s:
                if i is '1':
                    ss+='0'
                else:
                    ss+='1'
            return (ss[::-1]).strip()
        s='0'
        for i in range(n):
            s+='1'+ss(s)
        return s[k-1]
