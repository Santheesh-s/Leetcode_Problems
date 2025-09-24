class Solution {
public:
    void backtrack(vector<int>&candidates,int n,int target,vector<int>&combi,vector<vector<int>>&res,int cur)
    {
        if(target==0)
        {
            res.push_back(combi);
            return ;
        }
        if(target<0)
            return ;
        for(int i=cur;i<n;i++)
        {
            combi.push_back(candidates[i]);
            backtrack(candidates,n,target-candidates[i],combi,res,i);
            combi.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        int n=candidates.size();
        int sum=candidates[0];
        vector<int>combi;
        vector<vector<int>>res;
        backtrack(candidates,n,target,combi,res,0);
        return res;
    }
};
