class Solution {
    public int[] leftRightDifference(int[] nums) {
        int num1[]=new int[nums.length];
        int num2[]=new int[nums.length];
        num1[0]=0;
        num2[nums.length-1]=0;

        for(int i=1;i<num1.length;i++)
            num1[i]=num1[i-1]+nums[i-1];

        for(int i=num2.length-2;i>=0;i--)
            num2[i]=num2[i+1]+nums[i+1];

        int num[]=new int[nums.length];

        for(int i=0;i<nums.length;i++)
            num[i]=Math.abs(num1[i]-num2[i]);
        return num;
    }
}
