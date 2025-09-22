class Solution {
public:
    // int minCostClimbingStairs(vector<int>&cost,int i,vector<int>&memo)
    // {
    //     if(i<0)return 0;
    //     if(memo[i]!=-1)return memo[i];
    //     return memo[i]=cost[i]+min(minCostClimbingStairs(cost,i-1,memo),minCostClimbingStairs(cost,i-2,memo));
    // }
    // int minCostClimbingStairs(vector<int>& cost) {
    //     int n=cost.size();
    //     vector<int>memo(n,-1);
    //     return min(minCostClimbingStairs(cost,n-1,memo),minCostClimbingStairs(cost,n-2,memo));
    // }
    int minCostClimbingStairs(vector<int>&cost)
    {
        int n=cost.size();
        vector<int >dp(n,0);
        dp[0]=cost[0];
        dp[1]=cost[1];
        for(int i=2;i<n;i++)
            dp[i]=cost[i]+min(dp[i-1],dp[i-2]);
        return min(dp[n-1],dp[n-2]);
    }
};
