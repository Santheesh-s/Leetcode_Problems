class Solution {
    void dfs(int image[][],int r, int c,int old,int color)
    {
        if(r<0 || c<0 || r>=image.length || c>=image[0].length)
            return ;
        if(image[r][c]==old)
        {
            image[r][c]=color;
            dfs(image,r+1,c,old,color);
            dfs(image,r-1,c,old,color);
            dfs(image,r,c+1,old,color);
            dfs(image,r,c-1,old,color);
            return ;
        }
    }
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if(image[sr][sc]==color) return image;
        dfs(image,sr,sc,image[sr][sc],color);
        return image;
    }
}
