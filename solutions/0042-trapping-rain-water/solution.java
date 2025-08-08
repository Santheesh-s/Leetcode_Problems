class Solution {
    public int trap(int[] height) {
        int n=height.length;
        int[] left=new int[n];
        int[] right=new int[n];
        int max=0,max1=0,total=0;
        int h=n-1;
        for(int i=0;i<n;i++)
        {
            if(max<height[i])
                max=height[i];
            left[i]=max;

            if(max1<height[h])
                max1=height[h];
            right[h]=max1;
            h--;
        }
        for(int i=0;i<n;i++)
            total+=Math.min(right[i],left[i])-height[i];
        return total;
    }
}
