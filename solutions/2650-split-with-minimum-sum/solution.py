class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        n=sorted(list(str(num)))
        a=""
        b=""
        for i in range(0,len(n),2):
            a+=n[i]
        for i in range(1,len(n),2):
            b+=n[i]
        return int(a)+int(b)

