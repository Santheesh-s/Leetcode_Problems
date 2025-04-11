class Solution {
    public int arraySign(int[] nums) {
        int n=1;
        for(int a:nums)
        {    
            if(a>0)
                n*=1;
            else if(a<0)
                n*=-1;
            else
                return 0;
        }
        return n;
    }
}
