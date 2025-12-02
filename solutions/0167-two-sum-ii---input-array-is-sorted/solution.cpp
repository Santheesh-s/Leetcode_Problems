class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    vector<int>a;
    int left=0,right=nums.size()-1;
    while(left<right)
    {
        int s=nums[left]+nums[right];
        if(s==target)
        {
            a.push_back(left+1);
            a.push_back(right+1);
            return a;
        }
        else if(s>target) right--;
        else left++;
    }
    return a;
    }
};
