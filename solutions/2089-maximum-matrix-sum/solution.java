class Solution {
    public long maxMatrixSum(int[][] matrix) {
        int neg=0,a;
        long sum=0,min=1000000;

        for(int i=0;i<matrix.length;i++)
        {
            for(int j=0;j<matrix[i].length;j++)
            {
                if(matrix[i][j]<0) neg++;
                a=Math.abs(matrix[i][j]);
                sum+=a;
                min=Math.min(min,a);
            }
        }
        System.out.print(sum);
        if(neg%2==0)
            return sum;
        return sum-min*2;
    }
}
