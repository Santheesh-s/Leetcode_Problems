class Solution {
    public int largestAltitude(int[] gain) {
        int ans=0,sum=0,n=0;
        for(int i=0;i<gain.length;i++)
        {
            sum=ans+gain[i]+sum;
            if(n<sum)
                n=sum;
        }
        return n;
    }
}
