class Solution {
    public int[] sortedSquares(int[] nums) {
        int left=0,right=nums.length-1;
        int write=right;
        int[] res = new int[right+1];
        while(left<=right)
        {
            int a=nums[left]*nums[left];
            int b=nums[right]*nums[right];
            if(a>b)
            {
                res[write]=a;
                left++;
            }
            else
            {
                res[write]=b;
                right--;
            }
            write--;
        }
        return res;
    }
}
