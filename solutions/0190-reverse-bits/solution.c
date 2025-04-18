uint32_t reverseBits(uint32_t n) {
    long ans=0,i=0;
    while(i<32)
        {
            ans=ans<<1;
            ans=ans|(n&1);
            n>>=1;
            i++;
        }
        return ans;
}
