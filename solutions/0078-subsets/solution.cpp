class Solution {
public:
    void backtrack(vector<int>&nums,int n,vector<int>&combi,vector<vector<int>>&res,int cur)
    {
        res.push_back(combi);
        for(int i=cur;i<n;i++)
        {
            combi.push_back(nums[i]);
            backtrack(nums,n,combi,res,i+1);
            combi.pop_back();
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        int n=nums.size();
        vector<int>combi;
        vector<vector<int>>res;
        backtrack(nums,n,combi,res,0);
        return res;
    }
};
