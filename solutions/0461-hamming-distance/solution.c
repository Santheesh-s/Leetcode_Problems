int hammingDistance(int x, int y) {
    int count=0,r=x^y;
    while(r>0)
    {
        if(r&1)
            count++;
        r>>=1;
    }
    return count;
}
