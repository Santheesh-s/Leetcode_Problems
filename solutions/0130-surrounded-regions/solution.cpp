class Solution {
public:
    void dfs(vector<vector<char>>&board,int r,int c)
    {
        if(r<0 ||c<0|| r>=board.size() |c>=board[0].size())
            return ;
        if(board[r][c]=='O')
        {
            board[r][c]='#';
            dfs(board,r+1,c);
            dfs(board,r-1,c);
            dfs(board,r,c+1);
            dfs(board,r,c-1);
        }

    }
    void solve(vector<vector<char>>& board) {
        int m=board.size(),n=board[0].size();
        for(int r=0;r<board.size();r++)
        {
            dfs(board,r,0);
            dfs(board,r,n-1);
        } 
        for(int c=0;c<board[0].size();c++)
        {
            dfs(board,0,c);
            dfs(board,m-1,c);
        }
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
            {
                if(board[i][j]=='#')
                    board[i][j]='O';
                else if(board[i][j]=='O')
                    board[i][j]='X';
            }
    }
};
