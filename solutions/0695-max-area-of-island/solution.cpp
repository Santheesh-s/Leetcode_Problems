class Solution {
public:
int dfs(vector<vector<int>>&grid,int r,int c,int count)
{
    if(r<0 || c<0 || r>=grid.size()|| c>=grid[0].size())
        return count;
    if(grid[r][c]==1)
    {
        count++;
        grid[r][c]=0;
        count=dfs(grid,r,c+1,count);
        count=dfs(grid,r+1,c,count);
        count=dfs(grid,r-1,c,count);
        count=dfs(grid,r,c-1,count);
    }
    return count;
    
}
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int count=0;
        for(int r=0;r<grid.size();r++)
        {
            for(int c=0;c<grid[0].size();c++)
            {
                if(grid[r][c]==1)
                {
                    int cur=dfs(grid,r,c,0);
                    count=max(count,cur);
                }
            }
        }
        return count;
    }
};
