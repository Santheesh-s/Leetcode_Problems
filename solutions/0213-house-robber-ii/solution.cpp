class Solution {
public:
    int rob(int limit, vector<int> &nums, int i, vector<int> &memo)
    {
        if (i < limit) return 0;
        if (memo[i] != -1) return memo[i];
        int skip = rob(limit, nums, i - 1, memo);
        int take = nums[i] + rob(limit, nums, i - 2, memo);
        return memo[i] = max(skip, take);
    }
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];  
        vector<int> memo1(n, -1), memo2(n, -1);
        int case1 = rob(1, nums, n - 1, memo1);
        int case2 = rob(0, nums, n - 2, memo2);
        return max(case1, case2);
    }
};

