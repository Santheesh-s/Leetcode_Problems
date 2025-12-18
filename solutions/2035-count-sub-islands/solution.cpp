class Solution {
public:
    bool sub=true;
    void dfs(vector<vector<int>>&grid1,vector<vector<int>>&grid2,int r,int c)
    {
        if(r<0 || c<0 || r>=grid2.size() || c>=grid2[0].size() || grid2[r][c]==0)
            return ;
        if(grid1[r][c]==0 && grid2[r][c]==1) sub=false;

        grid2[r][c]=0;
        dfs(grid1,grid2,r+1,c);
        dfs(grid1,grid2,r-1,c);
        dfs(grid1,grid2,r,c+1);
        dfs(grid1,grid2,r,c-1);
    }
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int res=0;
        for(int r=0;r<grid2.size();r++)
            for(int c=0;c<grid2[0].size();c++)
                if(grid2[r][c]==1)
                {
                    sub=true;
                    dfs(grid1,grid2,r,c);
                    if(sub==true) res++;
                }
        return res;
    }
};
