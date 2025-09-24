class Solution {
public:
    void backtrack(vector<int>&candidates,int n,int target,vector<int>&combi,vector<vector<int>> &res,int cur )
    {
        if(target<0)
            return ;
        if(target==0)
        {
            res.push_back(combi);
            return ;
        }
        for(int i=cur;i<n;i++)
        {
            if(i>cur && candidates[i]==candidates[i-1])
                continue;
            combi.push_back(candidates[i]);
            backtrack(candidates,n,target-candidates[i],combi,res,i+1);
            combi.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        int n=candidates.size();
        vector<int>combi;
        vector<vector<int>>res;
        sort(candidates.begin(),candidates.end());
        backtrack(candidates,n,target,combi,res,0);
        return res;
    }
};
