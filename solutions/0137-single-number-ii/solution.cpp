class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map<int,int>m;
        for(int a:nums)
            m[a]++;
        for(auto &p:m)
            if(p.second==1)
                return p.first;
        return 0;
    }
};
