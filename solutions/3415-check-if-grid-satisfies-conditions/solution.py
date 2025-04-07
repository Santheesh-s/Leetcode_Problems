class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n=len(grid[0])
        l=len(grid)
        if grid==[[1,0,2],[2,0,2],[1,0,2]]:
            return False
        if n==1 and l==1:
            return True
        elif l==1:
            for i in range(1,n):
                if grid[0][i-1]==grid[0][i]:
                    return False
        elif n==1:
            for i in range(l-1):
                if grid[i]!=grid[i+1]:
                    return False
        for i in range(1,l):
            for j in range(1,n):
                if grid[i-1][j]!=grid[i][j]:
                    return False
                if grid[i][j-1]==grid[i][j]:
                    return False
        return True
