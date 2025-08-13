class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        ls=[]
        m=1
        z=0
        for i in range(len(grid)):
            for j in range(0,len(grid[i])):
                grid[i][j]=grid[i][j]%12345
                if grid[i][j]!=0:
                    m*=grid[i][j]
                else:
                    z=z+1
            ls+=grid[i]
        for i in range(len(grid)):
            for j in range(0,len(grid[i])):
                if not z:
                    grid[i][j]=m/grid[i][j]
                elif grid[i][j]!=0:
                    grid[i][j]=0
                elif z>1:
                    grid[i][j]=0
                else:
                    grid[i][j]=m
                grid[i][j]=grid[i][j]%12345
        return grid



