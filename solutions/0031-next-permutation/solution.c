
void reverse(int *nums,int left,int right)
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
void nextPermutation(int* nums, int numsSize) {
    
    int flag=0,n=numsSize;
        for(int i=n-1;i > 0;i--)
        {
            if(nums[i] > nums[i-1])
            {
                flag=1;
                int max=nums[i-1];
                for(int j=n-1;j>=i;j--)
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
                reverse(nums,i,n-1);
                break;
            }
        }
        if(flag==0)
              reverse(nums,0,n-1);
}

