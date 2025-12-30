import math
class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g=0
        for i in nums:
            g=gcd(g,i)
            if g==1:
                return True
        return False
