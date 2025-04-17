int climbStairs(int n) {
    long int a=0,b=1,c=0;
    for(int i=0;i<n+1;i++)
    {
        c=a+b;
        a=b;b=c;
    }
    return a;
}
