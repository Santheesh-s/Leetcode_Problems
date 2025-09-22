class Solution {
public:
    int tribonacci(int n) {
        long int a=0,b=1,c=1,f;
    if(n==0)
        return 0;
    for(int i=0;i<n;i++)
    {
        f=a+b+c;
        a=b;b=c;c=f;
    }
    return a;
    }
};
