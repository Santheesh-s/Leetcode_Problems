int split(int n)
{
    int sum=0,mod;
    while(n!=0)
    {
        mod=n%10;
        sum+=(mod*mod);
        n/=10;
    }
    return sum;
}

bool isHappy(int n) {
    int fast=n,slow=n;
    while(fast!=1)
    {
        slow=split(slow);
        fast=split(split(fast));
        if(fast==1 || slow==1)
            return true;
        if(slow==fast)
            return false;
    }
    return true;
}
