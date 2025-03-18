class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        res=0
        for i in str(x):
            res+=int(i)
        return res if x%res==0 else -1
