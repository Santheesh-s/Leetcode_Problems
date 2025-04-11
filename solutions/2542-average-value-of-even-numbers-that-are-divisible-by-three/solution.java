class Solution {
    public int averageValue(int[] nums) {
        int sum=0,i=0;
        for(int n:nums)
            if(n%6==0)
            {
                sum+=n;
                i++;
            }
        if(i==0)
            return 0;
        return sum/i;
    }
}
