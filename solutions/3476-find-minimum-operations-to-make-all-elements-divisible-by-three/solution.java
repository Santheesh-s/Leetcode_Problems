class Solution {
    public int minimumOperations(int[] nums) {
        int n=0;
        for(int i:nums)
            if(i%3!=0)
                n+=1;
        return n;
    }
}
