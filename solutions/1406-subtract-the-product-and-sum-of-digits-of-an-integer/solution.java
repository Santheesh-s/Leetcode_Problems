class Solution {
    public int subtractProductAndSum(int n) {
        int temp=1,sum=0;
        while(n!=0)
        {
            temp*=n%10;
            sum+=n%10;
            n/=10;
        }
        return temp-sum;
    }
}
