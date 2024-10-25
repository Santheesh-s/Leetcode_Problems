class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        List<Integer>ls=new ArrayList<>();
        for(int i=0;i<matrix.length;i++)
            for(int j=0;j<matrix[i].length;j++)
                ls.add(matrix[i][j]);
        Collections.sort(ls);
        return ls.get(k-1);
    }
}
