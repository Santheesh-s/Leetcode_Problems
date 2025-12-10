class Solution {
public:
    bool checkInclusion(string s1, string s2) 
    {
        if (s1.size() > s2.size()) return false;
        map<char,int>mp1,mp2;
        int count=0;
        int k=s1.size();
        for(int i=0;i<k;i++) mp1[s1[i]]++;
        for(int left=0,right=0;right<s2.size();right++)
        {
            mp2[s2[right]]++;
            if(right-left+1==k)
            {
                if(mp1==mp2) return true;
                mp2[s2[left]]--;
                if(mp2[s2[left]]==0)
                    mp2.erase(s2[left]);
                left++;
            }
        }
        return false;
    }
};
