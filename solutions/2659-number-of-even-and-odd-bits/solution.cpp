class Solution {
public:
    vector<int> evenOddBit(int n) {
        int odd=0,even=0;
        for(int i=0;i<32;i++)
        {
            if(i%2==0)
                even+=((n>>i)&1);
            else
                odd+=((n>>i)&1);
        }
        vector<int>a(2);
        a[0]=even;
        a[1]=odd;
        return a;
    }
};
