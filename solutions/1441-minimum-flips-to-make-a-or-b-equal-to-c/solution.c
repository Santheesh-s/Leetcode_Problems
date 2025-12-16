int minFlips(int a, int b, int c){
    int count=0;
    for(int i=0;i<32;i++)
    {
        int x=c&1;
        int y=a&1;
        int z=b&1;
        if(x==0 && y!=0)
            count++;
        if(x==0 && z!=0)
            count++;
        if(x==1 && y==0 && z==0)
            count++;
        c>>=1;a>>=1;b>>=1;
    }
    return count;
}
