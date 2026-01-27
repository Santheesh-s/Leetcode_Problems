class Solution {
    void dfs(int [][]board,int r,int c)
    {
        if(r<0 ||c<0|| r>=board.length ||c>=board[0].length)
            return ;
        if(board[r][c]==1)
        {
            board[r][c]=0;
            dfs(board,r+1,c);
            dfs(board,r-1,c);
            dfs(board,r,c+1);
            dfs(board,r,c-1);
        }

    }
    public int numEnclaves(int[][] board) {
        int m=board.length,n=board[0].length,count=0;
        for(int r=0;r<board.length;r++)
        {
            dfs(board,r,0);
            dfs(board,r,n-1);
        } 
        for(int c=0;c<board[0].length;c++)
        {
            dfs(board,0,c);
            dfs(board,m-1,c);
        }
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                if(board[i][j]==1)
                    count++;
        return count;
    }
}
