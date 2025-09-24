class Solution {
public:
    void per(vector<int>&nums,int n,vector<vector<int>>&res)
    {
        int flag=0;
        for(int i=n-1;i>0;i--)
        {
            if(nums[i]>nums[i-1])
            {
                int max1=i;
                for(int j=n-1;j>=i;j--)
                    if(nums[i-1]<nums[j])
                    {
                        max1=j;
                        break;
                    }
                int temp=nums[i-1];
                nums[i-1]=nums[max1];
                nums[max1]=temp;
                reverse1(nums,i,n-1);
                res.push_back(nums);
                flag=1;
                break;
            }
        }
        if(flag==1)
        {
            return per(nums,n,res);
        }
    }
    void reverse1(vector<int>&nums,int l,int r)
    {
        while(l<r)
        {
            int temp=nums[l];
            nums[l]=nums[r];
            nums[r]=temp;
            l++;
            r--;
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        int n=nums.size();
        vector<vector<int>>res;
        sort(nums.begin(), nums.end());
        res.push_back(nums);
        per(nums,n,res);
        return res;
    }
};
