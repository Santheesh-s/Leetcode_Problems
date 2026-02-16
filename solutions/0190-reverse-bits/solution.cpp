class Solution {
public:
    int reverseBits(int n) 
    {
        int a=0,i=0;
        while(i<32)
        {
            
            a<<=1;
            a|=(n&1);
            n>>=1;
            i++;
        }
        return a;
    }
};
