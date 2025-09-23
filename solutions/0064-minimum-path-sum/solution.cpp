class Solution {
public:
    int minPathSum(int m,int n,vector<vector<int>>& grid,vector<vector<int>>& memo) {
        if(memo[m][n]!=-1)
            return memo[m][n];
        if(m==0 && n==0)
            return memo[m][n]=grid[m][n];
        else if(m==0)
            return memo[m][n]=grid[m][n]+minPathSum(m,n-1,grid,memo);
        else if(n==0)
            return memo[m][n]=grid[m][n]+minPathSum(m-1,n,grid,memo);
        return memo[m][n]=grid[m][n]+min(minPathSum(m,n-1,grid,memo),minPathSum(m-1,n,grid,memo));
    }
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        vector<vector<int>>memo(m,vector<int>(n,-1));
        return minPathSum(m-1,n-1,grid,memo);
    }
};
