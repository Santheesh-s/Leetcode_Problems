class Solution {
public:
    bool isAnagram(string s, string t) {
    int a=s.size();
    int b=t.size();
    int arr[26]={};
    if(a!=b) return false;
    for(int i=0;i<a;i++)
    {
        arr[s[i]-97]-=1;
        arr[t[i]-97]+=1;
    }
    for(int i=0;i<26;i++)
        if(arr[i]!=0)
            return false;
    return true;
    }
};
