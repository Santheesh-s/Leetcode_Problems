class Solution {
    public int[] runningSum(int[] nums) {
        int arr[]=new int[nums.length];
        int sum=0,i=0;
        for(int n:nums)
        {
            sum+=n;
            arr[i++]=sum;
        }
        return arr;
    }
}
