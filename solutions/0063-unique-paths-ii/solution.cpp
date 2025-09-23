class Solution {
public:
    int uniquePathsWithObstacles(int m,int n,vector<vector<int>>& obstacleGrid,vector<vector<int>>&memo) {
        if(memo[m][n]!=-1)
            return memo[m][n];
        if(obstacleGrid[m][n]==1)
            return memo[m][n]=0;
        else if(m==0 && n==0)
            return memo[m][n]=1;
        else if(m==0)
            return memo[m][n]=uniquePathsWithObstacles(m,n-1,obstacleGrid,memo);
        else if(n==0)
            return memo[m][n]=uniquePathsWithObstacles(m-1,n,obstacleGrid,memo);
        return memo[m][n]=uniquePathsWithObstacles(m-1,n,obstacleGrid,memo)+uniquePathsWithObstacles(m,n-1,obstacleGrid,memo);
    }
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid)
    {
        int m=obstacleGrid.size();
        int n=obstacleGrid[0].size();
        vector<vector<int>>memo(m,vector<int>(n,-1));
        return uniquePathsWithObstacles(m-1,n-1,obstacleGrid,memo);
    }
};
