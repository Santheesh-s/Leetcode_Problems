class Solution {
public:
    int longestPalindromeSubseq(int m,int n,string &s,string &t,vector<vector<int>>&memo) {
        if(m==-1||n==-1)
            return 0;
        if(memo[m][n]!=-1)
            return memo[m][n];
        if(s[m]==t[n])
            return 1+longestPalindromeSubseq(m-1,n-1,s,t,memo);
        return memo[m][n]=max(longestPalindromeSubseq(m-1,n,s,t,memo),longestPalindromeSubseq(m,n-1,s,t,memo));
    }
    int longestPalindromeSubseq(string s) {
        int n=s.size();
        string t=reverse(s,n);
        vector<vector<int>>memo(n,vector<int>(n,-1));
        return longestPalindromeSubseq(n-1,n-1,s,t,memo);
    }
    string reverse(string s,int n)
    {
        int l=0,r=n-1;
        while(l<r)
        {
            char temp=s[l];
            s[l]=s[r];
            s[r]=temp;
            l++;r--;
        }
        return s;
    }
};
