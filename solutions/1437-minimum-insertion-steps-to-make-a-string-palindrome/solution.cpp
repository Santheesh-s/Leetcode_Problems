class Solution {
public:
    int minInsertions(int m,int n,string &s,vector<vector<int>>&memo) {
        if(m==n)
            return 0;
        if(m>n) return 0;
        if(memo[m][n]!=-1)
            return memo[m][n];
        if(s[m]==s[n])
            return memo[m][n]=minInsertions(m+1,n-1,s,memo);
        return memo[m][n]=1+min(minInsertions(m+1,n,s,memo),minInsertions(m,n-1,s,memo));
    }
    int minInsertions(string s) {
        int m=s.size();
        vector<vector<int>>memo(m,vector<int>(m,-1));
        return minInsertions(0,m-1,s,memo);
    }
};
