class Solution {
    public int[] productExceptSelf(int[] nums) {
        int pro=1,z=0;
        for(int i:nums)
        {
            if(i==0)
                z++;
            else
                pro*=i;
        }
        for (int i = 0; i < nums.length; i++) {
            if (z > 1)
                nums[i] = 0;
            else if (z == 1) 
                nums[i] = (nums[i] == 0) ? pro : 0;
            else 
                nums[i] = pro / nums[i];
        }
        return nums;
    }
}
