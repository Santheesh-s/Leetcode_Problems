class Solution {
public:
    int rob(vector<int>&nums,int i,vector<int>&memo)
    {
        if(i<0) return 0;
        if(memo[i]!=-1) return memo[i];
        return memo[i]=nums[i]+max(rob(nums,i-3,memo),rob(nums,i-2,memo));
    }
    int rob(vector<int>& nums) {
        int n=nums.size();
        vector<int>memo(n,-1);
        return max(rob(nums,n-1,memo),rob(nums,n-2,memo));
    }
};
