class Solution {
    public int countPrimeSetBits(int left, int right) {
    int count=0;
    for(int i=left;i<=right;i++)
    {
        int count1=0,a=i;
        while((a>0))
        {
            if((a&1)==1)
                count1++;
            a>>=1;
        }
        count+=santhu(count1);
    }
    return count;
    }
    int santhu(int count)
    {
        if(count == 2 || count == 3 || count == 5 || count == 7 ||
           count == 11 || count == 13 || count == 17 || count == 19)
            return 1;
        return 0;
    }
}
