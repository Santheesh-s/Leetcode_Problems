class Solution {
    public boolean isPerfectSquare(int n) {
        if(n==1) return true;
        for(int i=0;i<n;i++)
        {
            if(i*i==n)
                return true;
            else if(i*i>n)
                break;
        }
        return false;
    }
}
