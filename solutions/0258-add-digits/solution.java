class Solution {
    public int addDigits(int n) {
        int rem=0,sum=0;
        while(n>9)
        {
            sum=0;
            while(n!=0)
            {
                rem=n%10;
                n=n/10;
                sum+=rem;
            }
            n=sum;
        }
        return n;
    }
}
