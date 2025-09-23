class Solution {
public:
    int minDistance(int m, int n,string &word1, string &word2,vector<vector<int>>&memo) {
        if(m<0) return n+1;
        if(n<0) return m+1;
        if(memo[m][n]!=-1) return memo[m][n];
        if(word1[m]==word2[n])
            return memo[m][n]=minDistance(m-1,n-1,word1,word2,memo);
        return memo[m][n]=1+min(minDistance(m,n-1,word1,word2,memo),min(minDistance(m-1,n,word1,word2,memo),minDistance(m-1,n-1,word1,word2,memo)));
    }
    int minDistance(string word1, string word2) {
        int m=word1.size();
        int n=word2.size();
        vector<vector<int>>memo(m,vector<int>(n,-1));
        return minDistance(m-1,n-1,word1,word2,memo);
    }
};
