class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans=0
        i=0;
        while(i<32):
            ans=ans<<1;
            ans=ans|(n&1);
            n>>=1;
            i+=1;
        return ans;
