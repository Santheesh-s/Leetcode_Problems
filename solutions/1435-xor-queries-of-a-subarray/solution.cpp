class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int>pre;
        int a=0;
        for(int i=0;i<arr.size();i++)
        {
            a=a^arr[i];
            pre.push_back(a);
        }
        vector<int>res;
        for(int i=0;i<queries.size();i++)
        {
            int l=queries[i][0];
            int r=queries[i][1];
            if(l==0) 
                res.push_back(pre[r]);
            else
                res.push_back(pre[r]^pre[l-1]);
        }
        return res;
    }
};
