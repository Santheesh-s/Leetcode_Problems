class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=n*(n+1)/2
        right=0
        for i in range(1,n+1):
            left-=i
            if left==right:
                return i
            right+=i
        return -1
