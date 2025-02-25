class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ls=""
        for i in grid:
            ls+="".join(map(str,grid))
        return (ls.count("-"))/len(grid)
