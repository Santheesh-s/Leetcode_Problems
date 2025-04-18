public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int ans=0,i=0;
        while(i<32)
        {
            ans<<=1;
            ans=ans|(n&1);
            n>>=1;
            i++;
        }
        return ans;
    }
}
