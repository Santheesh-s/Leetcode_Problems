class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ls=[math.pow(3,i) for i in range(0,32) if math.pow(3,i)<=n][::-1]
        for p in ls:
            if p <= n:
                n -= p
            if n == 0:
                return True
        return n == 0
