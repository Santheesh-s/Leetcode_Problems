class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] arr=new int[2];
        arr[0]=-1;arr[1]=-1;
        int flag=0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==target && flag==0)
            {
                arr[0]=i;
                flag=1;
            }
            if(flag==1 && nums[i]==target)
                arr[1]=i;
            else if(flag==1 && nums[i]!=target)
                return arr;
        }
        return arr;
    }
}
