class Solution {
public:
    int mr=0,mc=0;
    void dfs(vector<vector<int>>&land,int r,int c)
    {
        if(r<0 || c<0 || r>=land.size() || c>=land[0].size())
            return ;
        if(land[r][c]==1)
        {
            if(r>mr) mr=r;
            if(c>mc) mc=c;
            land[r][c]=0;
            dfs(land,r+1,c);
            dfs(land,r-1,c);
            dfs(land,r,c+1);
            dfs(land,r,c-1);
        }
    }
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        vector<vector<int>>res;
        for(int r=0;r<land.size();r++)
            for(int c=0;c<land[0].size();c++)
                if(land[r][c]==1)
                {
                    mr=0;mc=0;
                    dfs(land,r,c);
                    res.push_back({r,c,mr,mc});
                }
        return res;
    }
};
