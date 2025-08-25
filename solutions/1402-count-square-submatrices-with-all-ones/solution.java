class Solution {
    public int countSquares(int[][] matrix) {
        int sum1=0;
        for(int i=0;i<matrix.length;i++)
        {
            for(int j=0;j<matrix[i].length;j++)
            {
                if(i>0 && j>0 && matrix[i][j]==1)
                    matrix[i][j]+=Math.min(matrix[i-1][j-1],Math.min(matrix[i-1][j],matrix[i][j-1]));
                sum1+=matrix[i][j];    
            }
        }
        return sum1;
    }
}
