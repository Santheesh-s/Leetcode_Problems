class Solution {
public:
    int longestCommonSubsequence(int m,int n,string &text1, string &text2,vector<vector<int>>&memo) {
        
        if(m==-1||n==-1)
            return 0;
        if(memo[m][n]!=-1)
            return memo[m][n];
        else if(text1[m]==text2[n])
            return memo[m][n]=1+longestCommonSubsequence(m-1,n-1,text1,text2,memo);
        return memo[m][n]=max(longestCommonSubsequence(m,n-1,text1,text2,memo),longestCommonSubsequence(m-1,n,text1,text2,memo));

    }
    int longestCommonSubsequence(string text1, string text2)
    {
        int m=text1.size();
        int n=text2.size();
        vector<vector<int>>memo(m,vector<int>(n,-1));
        return longestCommonSubsequence(m-1,n-1,text1,text2,memo);
    }
};
