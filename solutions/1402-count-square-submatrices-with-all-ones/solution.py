class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        sum1=0;
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(i>0 and j>0 and matrix[i][j]==1):
                    matrix[i][j]+=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])
                sum1+=matrix[i][j];    
        return sum1;
