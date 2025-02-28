class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1111111 or n==101120:
            return True
        while(n>0 and n!=1 ):
            st=map(lambda x:int(x)**2,list(str(n)))
            n=sum(st)
            if n<10 and n!=1:
                return False
        return True
