class Solution {
    public void rotate(int[][] matrix) {
        int n=matrix.length;
        int[][] arr=new int[n][n];
        int a=0;
        for(int i=n-1;i>=0;i--)
        {
            for(int j=0;j<n;j++)
            {
                arr[j][a]=matrix[i][j];
            }
            a++;
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                matrix[i][j]=arr[i][j];
            }
        }       
    }
}
