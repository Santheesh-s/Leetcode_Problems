class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int m=nums[0],k=0;
        for(int i=0;i<nums.size();i++)
            if(m<nums[i])
            {
                m=nums[i];
                k=i;
            }
        return k;
    }
};
