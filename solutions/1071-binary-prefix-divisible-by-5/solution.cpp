class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
    long long a=0;
    int n=nums.size();
    vector<bool>arr(n);
    for(int i=0;i<n;i++)
    {
        a<<=1;
        a|=nums[i];
        a%=5;
        arr[i] = (a == 0);
    }
    return arr;
    }
};
