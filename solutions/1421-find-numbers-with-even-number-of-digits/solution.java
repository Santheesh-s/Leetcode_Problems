class Solution {
    public int findNumbers(int[] nums) {
        int i=0;
        for(int n:nums)
            if(String.valueOf(n).length()%2==0)
                i++;
        return i;
    }
}
