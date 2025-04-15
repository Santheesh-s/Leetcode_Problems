class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int n=0,j=0;
        for(int i=0;i<mat.length;i++)
        {
            List<Integer>ls=new ArrayList<>();
            for(int a:mat[i]) ls.add(a);
            int a=Collections.frequency(ls,1);
            if(a>n)
            {
                n=a;
                j=i;
            }
        }
        return new int[]{j,n};
    }
}
