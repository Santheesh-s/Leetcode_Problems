class Solution {
    public int[] findErrorNums(int[] nums) {
        int arr[]=new int[2];
        int a=0,flag=1,n=nums.length;
        for(int i=0;i<n;i++)
        {
            int val=Math.abs(nums[i]);
            a+=val;
            if(nums[val-1]<0 && flag-- >0)
                arr[0]=val;
            else
                nums[val-1]*=-1;
        }
        int org=(n*(n+1))/2;
        a-=arr[0];
        arr[1]=org-a;
        return arr;
    }
}
