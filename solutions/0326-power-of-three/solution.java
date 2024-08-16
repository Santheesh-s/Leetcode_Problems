class Solution {
    public boolean isPowerOfThree(int n) {
        if(n>=0)
        {
            if((n&(n-1))==n-1 && 1162261467 % n == 0 )
            {
                return true;
            }
        }
        return false;
    }
}
