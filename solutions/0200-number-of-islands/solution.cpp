class Solution {
public:
    void dfs(vector<vector<char>>&grid,int r,int c)
    {
        if(r<0 || c<0 || r>=grid.size() || c>=grid[0].size())
            return ;
        if(grid[r][c]=='1')
        {
            grid[r][c]='0';
            dfs(grid,r-1,c); //up
            dfs(grid,r+1,c); //down
            dfs(grid,r,c-1); //left
            dfs(grid,r,c+1); //right

        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int count=0;
        for(int row=0;row<grid.size();row++)
            for(int col=0;col<grid[0].size();col++)
                if(grid[row][col]=='1')
                {
                    count++;
                    dfs(grid,row,col);
                }
        return count;
    }

};
