int largestAltitude(int* gain, int gainSize) {
    int ans=0,sum=0,n=0;
    for(int i=0;i<gainSize;i++)
    {
        sum=ans+gain[i]+sum;
        if(n<sum)
            n=sum;
    }
    return n;
}
