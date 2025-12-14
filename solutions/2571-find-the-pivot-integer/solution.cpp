class Solution {
public:
    int pivotInteger(int n) {
        int a=((n+1)*n)/2;
        int b=0;
        for(int i=1;i<=n;i++)
        {
            a-=i;
            if(a==b)
                return i;
            b+=i;
        }
        return -1;
    }
};
