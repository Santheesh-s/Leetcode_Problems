class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int[] arr=new int[nums.length];
        int k=0,n=nums.length;
        int a=n-1;
        for(int i=0;i<n;i++)
        {
            if(nums[i]%2==0)
                arr[k++]=nums[i];
            else
                arr[a--]=nums[i];
        }
        return arr;
    }
}
