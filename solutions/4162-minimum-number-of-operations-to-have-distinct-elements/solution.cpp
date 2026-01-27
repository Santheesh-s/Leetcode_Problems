class Solution {
public:
    int minOperations(vector<int>& nums) {
        map<int,int>m;
        for(int i=nums.size()-1;i>=0;i--)
        {
            if(m.contains(nums[i]))
                return (i+3)/3;
            m[nums[i]]=1;
        }
        return 0;
    }
};
