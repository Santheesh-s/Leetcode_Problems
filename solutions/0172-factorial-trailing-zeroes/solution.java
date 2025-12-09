class Solution {
    // int N=10000+10;
    // long long[] fact=new long long[N];
    // Solution()
    // {
    //     fact[0]=fact[1]=1;
    //     for(int i=2;i<N;i++)
    //         fact[i]=fact[i-1]*i;
    // }
    public int trailingZeroes(int n) {
        int count=0;
        while (n > 0) 
        {
            n /= 5;
            count += n;
        }
        return count;
    }
}
