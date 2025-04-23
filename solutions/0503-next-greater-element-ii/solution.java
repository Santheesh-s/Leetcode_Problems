class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n=nums.length,i=0,m;
        int[] arr=new int[n+n];
        for(i=0;i<n;i++)
        {
            arr[i]=nums[i];
            arr[i+n]=nums[i];
        }
        for(i=0;i<n;i++)
        {
            m=0;
            for(int j=i+1;j<n*2;j++)
            {
                if(arr[j]>nums[i])
                {
                    nums[i]=arr[j];
                    m=1;
                    break;
                }
            }
            if(m==0)
                nums[i]=-1;
        }
        return nums;
    }
}
