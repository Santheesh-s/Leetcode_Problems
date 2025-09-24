class Solution {
public:
    double max(double a,double b)
    {
        if(a>b) return a;
        return b;
    }
    double findMaxAverage(vector<int>& nums, int k) {
        int n=nums.size();
        double avg=-100000,sum=0;
        for(int left=0,right=0;right<n;right++)
        {
            if(right-left+1==k)
            {
                sum+=nums[right];
                avg=max(avg,sum/k); 
                sum-=nums[left];
                left++;

            }
            else
            {
                sum+=nums[right];
            }
        }
        return avg;
    }
};
