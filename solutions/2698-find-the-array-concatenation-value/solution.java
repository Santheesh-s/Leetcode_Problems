class Solution {
    public long findTheArrayConcVal(int[] nums) {
        long s=0;
        for(int i=0;i<nums.length/2;i++)
            s+=Integer.parseInt(String.valueOf(nums[i])+String.valueOf(nums[nums.length-(i+1)]));
        if (nums.length%2!=0)
            s+=nums[nums.length/2];
        return s;
    }
}
