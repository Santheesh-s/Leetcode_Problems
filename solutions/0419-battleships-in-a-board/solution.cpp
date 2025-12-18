class Solution {
public:
    int count=0;
    void dfs(vector<vector<char>>&board,int r, int c)
    {
        if(r<0 || c<0 || r>=board.size()||c>=board[0].size())
            return ;
        if(board[r][c]=='X')
        {
            board[r][c]='.';
            dfs(board,r+1,c);
            dfs(board,r-1,c);
            dfs(board,r,c+1);
            dfs(board,r,c-1);
        }
    }
    int countBattleships(vector<vector<char>>& board) {
        int count=0;
        for(int r=0;r<board.size();r++)
            for(int c=0;c<board[0].size();c++)
                if(board[r][c]=='X')
                {
                    count++;
                    dfs(board,r,c);
                }
        return count;
    }
};
