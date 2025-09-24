class Solution(object):
    def maxSum(self, grid, limits, k):
        """
        :type grid: List[List[int]]
        :type limits: List[int]
        :type k: int
        :rtype: int
        """
        n=len(limits)
        ls=[]
        for i in range(n):
            if(limits[i]!=0):
                ls+=(sorted(grid[i])[-limits[i]:])
        if(k!=0):
            ls=sorted(ls)[-k:]
            return sum(ls)
        return 0
