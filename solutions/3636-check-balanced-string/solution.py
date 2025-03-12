class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n=len(num)
        a,b=0,0
        for i in range(0,n,2):
            a+=int(num[i])
        for i in range(1,n,2):
            b+=int(num[i])
        return a==b
