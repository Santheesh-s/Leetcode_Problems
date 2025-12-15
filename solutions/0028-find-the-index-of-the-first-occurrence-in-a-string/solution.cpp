class Solution {
public:
    int strStr(string haystack, string needle) {
        int n1=haystack.size(),n2=needle.size();
        int a=0;
        for(int i=0;i<n1;i++)
        {
            if(haystack[i]==needle[a])
            {
                a++;
                if(a==n2)
                    return i-n2+1;
            }
            else
            {
                i = i - a;
                a=0;
            }
        }
        return -1;
    }
};
