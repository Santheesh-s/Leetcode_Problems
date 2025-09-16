class Solution {
    public void nextPermutation(int[] nums) {
        int flag=0;
        for(int i=nums.length-1;i > 0;i--)
        {
            if(nums[i] > nums[i-1])
            {
                flag=1;
                int max=nums[i-1];
                for(int j=nums.length-1;j>=i;j--)
                {
                    if(max < nums[j])
                    {
                        max=j;
                        break;
                    }
                }
                int temp=nums[i-1];
                nums[i-1]=nums[max];
                nums[max]=temp;
                reverse(nums,i,nums.length-1);
                break;
            }
        }
        if(flag==0)
              reverse(nums,0,nums.length-1);
    
    }
    void reverse(int[] nums,int left,int right)
    {
        while(left < right)
        {
            int temp = nums[left];
            nums[left]= nums[right];
            nums[right]=temp;
            left++;
            right--;
        }
    }
}
