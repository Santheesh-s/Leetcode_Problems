class Solution {
public:
    void backtrack(vector<int>&nums,int n,int target ,int k, vector<int>&combi,vector<vector<int>>&res,int cur)
    {
        if(combi.size()==k && target==0)
        {
            res.push_back(combi);
            return ;
        }
        if(target<0)
            return ;
        for(int i=cur;i<n;i++)
        {
            combi.push_back(nums[i]);
            backtrack(nums,n,target-nums[i],k,combi,res,i+1);
            combi.pop_back();
        }
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int>nums={1,2,3,4,5,6,7,8,9};
        vector<int>combi;
        vector<vector<int>>res;
        backtrack(nums,9,n,k,combi,res,0);
        return res;
    }
};
